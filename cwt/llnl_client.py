import logging
from urllib import parse

import cwt
from cwt import auth
from cwt import errors
import requests

logger = logging.getLogger(__name__)

DEFAULT_JOB_PATH = "/wps/api/job/"
DEFAULT_JOB_DETAIL_PATH = "/wps/api/job/{}/"


def fix_url(x):
    if "wpsapi" in x:
        # Fix for weird issue in urls from django rest framework
        x = x.replace("wpsapi", "wps/api")
    x = x[:-1] if x.endswith("/") else x

    return x


class JobWrapper(object):
    """Represents a job."""

    def __init__(self, data, headers=None):
        """JobWrapper init

        Args:
            data (dict): JSON from jobs api.
            headers (dict, optional): Headers used for communicating with the server.
        """
        if headers is None:
            headers = {}

        self.data = data
        self.headers = headers
        self.status = None

    def delete(self):
        url = fix_url(self.data["url"])

        if not url.endswith("/"):
            url = "{}/".format(url)

        response = requests.delete(url, headers=self.headers)

        response.raise_for_status()

        del self

    def _get_statuses(self):
        status = []

        for x in self.data["status_links"]:
            x = fix_url(x)
            x = "{}.json".format(x)
            response = requests.get(x, headers=self.headers)

            status.append(response.json())

        status = sorted(status, key=lambda x: x["created_date"])

        return status

    def _format_message(self, data):
        return '<td style="text-align: left">{created_date} {message} {percent}</td>'.format(
            **data
        )

    def _repr_html_(self):
        if self.status is None:
            self.status = self._get_statuses()

        row_data = []

        for s in self.status:
            data = [
                "<td>{}</td>".format(s["status"]),
                "<td>{}</td>".format(s["created_date"]),
            ]

            if "message" in s and len(s["message"]) > 0:
                messages = s["message"]

                data.append(self._format_message(messages[0]))

                row_data.append("<tr>{}</tr>".format("".join(data)))

                padding = "<td></td><td></td>"

                for x in messages[1:]:
                    row_data.append(
                        "<tr>{0}{1}</tr>".format(
                            padding, self._format_message(x)
                        )
                    )
            else:
                if "exception" in s and s["exception"] is not None:
                    data.append(
                        '<td style="text-align: left">{}</td>'.format(
                            s["exception"]
                        )
                    )
                else:
                    data.append("<td></td>")

                row_data.append("<tr>{}</tr>".format("".join(data)))

        rows = "".join(row_data)

        header = "<tr><th>Status</th><th>Created</th><th>Messages</th></tr>"

        table = "<table>{header}{rows}</table>".format(
            header=header, rows=rows
        )

        output_rows = []

        for x in self.data["output"]:
            url = x["remote"]
            filename = parse.urlparse(url).path.split("/")[-1]
            text = (
                "<tr><td><a href='{}' target='_blank'>{}</a></td><td>{}"
                "</td></tr>"
            ).format(url, filename, x["size"])

            output_rows.append(text)

        output_table_headers = "<tr><th>File</th><th>Size (MB)</th></tr>"

        output_table = "<table>{}{}</table>".format(
            output_table_headers, "".join(output_rows)
        )

        return "{}{}".format(table, output_table)


class JobListWrapper(object):
    """Represents a list of jobs."""

    def __init__(self, url, data, headers=None):
        """JobListWrapper init.

        Args:
            data (dict): JSON output from jobs api.
            headers (dict, optional): Headers used to communicate with the server.
        """
        if headers is None:
            headers = {}

        self.headers = headers

        self.url = url
        self.pages = {url: data}

        self.jobs = {}

    @property
    def current(self):
        """Returns current page."""
        return self.pages[self.url]

    def next(self):
        """Loads the next page of results"""

        url = self.current.get("next", None)

        if url is None:
            return self

        self.url = url

        if self.url not in self.pages:
            self.pages[url] = self._get_url(url)

        return self

    def previous(self):
        """Returns the previous page of results"""
        url = self.current.get("previous", None)

        if url is None:
            return self

        self.url = url

        if self.url not in self.pages:
            self.pages[url] = self._get_url(url)

        return self

    def _get_url(self, url):
        response = requests.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()

    def _repr_html_(self):
        columns = (
            ("id", "ID"),
            ("identifier", "Identifier"),
            ("status", "Status"),
            ("accepted", "Accepted"),
            ("elapsed", "Elapsed"),
            ("output", "Outputs"),
        )

        row_data = []

        for x in self.current["results"]:
            data = []

            for id, _ in columns:
                if id == "output":
                    data.append(
                        "<td>{} files, total size {} MB</td>".format(
                            len(x[id]), sum([float(y["size"]) for y in x[id]])
                        )
                    )
                else:
                    data.append("<td>{}</td>".format(x[id]))

            data = "".join(data)

            row_data.append("<tr>{}</tr>".format(data))

        rows = "".join(row_data)

        table_header = "".join(
            ["<th>{}</th>".format(name) for (_, name) in columns]
        )

        table = "<table><tr>{}</tr>{}</table>".format(table_header, rows)

        comp = parse.urlparse(self.url)

        qs = parse.parse_qs(comp.query)

        offset = qs["offset"][0] if "offset" in qs else 0
        limit = qs["limit"][0] if "limit" in qs else None

        if limit is not None:
            offset = int(offset)

            limit = int(limit)

            count = self.current["count"]

            footer = "<p>Display {} - {} of {} entries</p>".format(
                offset, min(offset + limit, count), count
            )
        else:
            footer = ""

        return "<div><h2>Jobs</h2></div>{}</div><div>{}</div>".format(
            table, footer
        )

    def job(self, id):
        job = None

        for x in self.current["results"]:
            if x["id"] == id:
                job = x

        if job is None:
            try:
                job = self._get_url(
                    parse.urljoin(self.url, DEFAULT_JOB_DETAIL_PATH).format(
                        id
                    )
                )
            except Exception:
                raise errors.JobMissingError("Could not load job {}", id)

        return JobWrapper(job, self.headers)

    def __getitem__(self, id):
        return self.job(id)


class LLNLClient(cwt.WPSClient):
    """LLNLClient.

    This client is a subclass of WPSClient providing methods specific
    to the LLNL WPS implementation.
    """

    def __init__(self, *args, **kwargs):
        """LLNLClient __init__."""
        super().__init__(*args, **kwargs)

        self._listing = None

    def _job_url(self):
        parts = parse.urlparse(self.url)

        base_url = "{0}://{1}".format(parts.scheme, parts.netloc)

        return parse.urljoin(base_url, DEFAULT_JOB_PATH)

    def jobs(self, limit=10):
        """Retrieves listing of jobs."""
        job_url = self._job_url()

        headers = self.headers.copy()

        params = {
            "limit": limit or 10,
        }

        self._patch_authentication(headers, params)

        response = requests.get(job_url, headers=headers, params=params)

        response.raise_for_status()

        self._listing = JobListWrapper(response.url, response.json(), headers)

        return self._listing


class LLNLKeyCloakAuthenticator(auth.KeyCloakAuthenticator):
    """LLNL KeyCloak authenticator."""

    def __init__(self, base_url, keycloak_url, realm, *args, **kwargs):
        self._base_url = base_url.strip("/")

        super(LLNLKeyCloakAuthenticator, self).__init__(
            keycloak_url.strip("/"), realm, *args, **kwargs
        )

    def register_client(self):
        logger.info("Registering client for client credentials flow")

        client_reg_url = f"{self._base_url}/wps/auth/client_registration/"

        response = requests.get(client_reg_url, allow_redirects=False)

        if response.status_code != 302:
            raise errors.WPSAuthError(
                "Error registering client, contact server admin."
            )

        print(f"Open {response.next.url!r} in a browser")

        client_id = input("Client ID: ")

        client_secret = input("Client Secret: ")

        return client_id, client_secret

    def _pre_prepare(self, headers, query, store):
        client_id = store.get("client_id", self._client_id)

        client_secret = store.get("client_secret", self._client_secret)

        if client_id is None and client_secret is None:
            client_id, client_secret = self.register_client()

            store["client_id"] = client_id

            store["client_secret"] = client_secret

        store = super(LLNLKeyCloakAuthenticator, self)._pre_prepare(
            headers, query, store
        )

        return store
