import json
import logging
import requests
import os
from urllib import parse

import cwt
from cwt.auth import TokenAuthenticator
from cwt import CWTError

logger = logging.getLogger(__name__)

DEFAULT_LOGIN_PATH = '/api/openid/login/'
DEFAULT_JOB_PATH = '/api/jobs/'
DEFAULT_JOB_DETAIL_PATH = '/api/jobs/{}/'
DEFAULT_OPENID_URL = 'https://esgf-node.llnl.gov/esgf-idp/openid'

HTML = """
<pre>
Open the link below in a web browser and log into the ESGF OpenID service.

Copy the returned token and paste in the input below.

<a href="{}" target="_blank">Login</a>
</pre>
"""

PLAIN = """
Open the link below in a web browser and log into the ESGF OpenID service.

Copy the returned token and paste in the input below.

{}
"""

class AuthenticationError(CWTError):
    pass

class JobStatusError(CWTError):
    pass

class JobMissingError(CWTError):
    pass

class JobWrapper(object):
    """ Represents a job.
    """

    def __init__(self, data, headers=None):
        """ JobWrapper init

        Args:
            data (dict): JSON from jobs api.
            headers (dict, optional): Headers used for communicating with the server.
        """
        if headers is None:
            headers = {}

        self.data = data
        self.headers = headers
        self.status = None

    def _get_statuses(self):
        status = []

        for x in self.data['status']:
            x = x.replace('http://', 'https://')

            response = requests.get(x, headers=self.headers)

            status.append(response.json())

        return status

    def _format_message(self, data):
        return '<td style="text-align: left">{created_date} {message} {percent}</td>'.format(**data)

    def _repr_html_(self):
        if self.status is None:
            self.status = self._get_statuses()

        row_data = []

        for s in self.status:
            data = [
                '<td>{}</td>'.format(s['status']),
                '<td>{}</td>'.format(s['created_date']),
            ]

            if 'messages' in s and len(s['messages']) > 0:
                messages = s['messages']

                data.append(self._format_message(messages[0]))

                row_data.append('<tr>{}</tr>'.format(''.join(data)))

                padding = '<td></td><td></td>'

                for x in messages[1:]:
                    row_data.append('<tr>{0}{1}</tr>'.format(padding, self._format_message(x)))
            else:
                if 'output' in s and s['output'] is not None:
                    x = json.loads(s['output'])

                    if isinstance(x, list):
                        outputs = '\n'.join(['<a href="{uri}" target="_blank">{uri}</a>'.format(**y) for y in x])
                    else:
                        outputs = '<a href="{uri}" target="_blank">{uri}</a>'.format(**x)

                    data.append('<td style="text-align: left"><pre>{}</pre></td>'.format(outputs))
                elif 'exception' in s and s['exception'] is not None:
                    data.append('<td style="text-align: left">{}</td>'.format(s['exception']))
                else:
                    data.append('<td></td>')

                row_data.append('<tr>{}</tr>'.format(''.join(data)))

        rows = ''.join(row_data)

        header = '<tr><th>Status</th><th>Created</th><th>Output</th></tr>'

        return '<table>{header}{rows}</table>'.format(header=header, rows=rows)

class JobListWrapper(object):
    """ Represents a list of jobs.
    """

    def __init__(self, url, data, headers=None):
        """ JobListWrapper init.

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
        """ Returns current page.
        """
        return self.pages[self.url]

    def next(self):
        """ Loads the next page of results
        """

        url = self.current.get('next', None)

        if url is None:
            return self

        self.url = url

        if self.url not in self.pages:
            self.pages[url] = self._get_url(url)

        return self

    def previous(self):
        """ Returns the previous page of results
        """
        url = self.current.get('previous', None)

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
            ('id', 'ID'),
            ('process', 'Operation'),
            ('elapsed', 'Elapsed'),
            ('latest_status', 'Status'),
            ('accepted_on', 'Accepted'),
        )

        row_data = []

        for x in self.current['results']:
            data = ''.join(['<td>{}</td>'.format(x[id]) for (id, _) in columns])

            row_data.append('<tr>{}</tr>'.format(data))

        rows = ''.join(row_data)

        table_header = ''.join(['<th>{}</th>'.format(name) for (_, name) in columns])

        table = '<table><tr>{}</tr>{}</table>'.format(table_header, rows)

        comp = parse.urlparse(self.url)

        qs = parse.parse_qs(comp.query)

        offset = qs['offset'][0] if 'offset' in qs else 0
        limit = qs['limit'][0] if 'limit' in qs else None

        if limit is not None:
            offset = int(offset)

            limit = int(limit)

            count = self.current['count']

            footer = '<p>Display {} - {} of {} entries</p>'.format(offset, min(offset+limit, count), count)
        else:
            footer = ''

        return '<div><h2>Jobs</h2></div>{}</div><div>{}</div>'.format(table, footer)

    def job(self, id):
        job = None

        for x in self.current['results']:
            if x['id'] == id:
                job = x

        if job is None:
            try:
                job = self._get_url(parse.urljoin(self.server_url, DEFAULT_JOB_DETAIL_PATH))
            except Exception:
                raise JobMissingError('Could not load job {}', id)

        return JobWrapper(job, self.headers)

    def __getitem__(self, id):
        return self.job(id)


class LLNLClient(cwt.WPSClient):
    """ LLNLClient.

    This client is a subclass of WPSClient providing methods specific
    to the LLNL WPS implementation.
    """
    def __init__(self, *args, **kwargs):
        """ LLNLClient __init__.
        """
        super().__init__(*args, **kwargs)

        self._listing = None

    def _job_url(self):
        parts = parse.urlparse(self.url)

        base_url = '{0}://{1}'.format(parts.scheme, parts.netloc)

        return parse.urljoin(base_url, DEFAULT_JOB_PATH)

    def jobs(self, limit=10):
        """ Retrieves listing of jobs.
        """
        if self._listing is None:
            job_url = self._job_url()

            headers = self.headers.copy()

            params = {
                'limit': limit or 10,
            }

            self.auth.prepare(headers, params)

            response = requests.get(job_url, headers=headers, params=params)

            response.raise_for_status()

            self._listing = JobListWrapper(response.url, response.json(), headers)

        return self._listing

class LLNLAuthenticator(TokenAuthenticator):
    """ LLNLAuthenticator.
    """

    def __init__(self, server_url, **kwargs):
        """ LLNLAuthenticator __init__.

        Args:
            server_url (str): The base url of the WPS server.
            openid_url (str, optional): A url to the OpenID authentication server.
            verify (bool, optional): Verify SSL certificate.
            store_token (bool, optional): Will write token to ~/.cwt.
        """
        super().__init__(key='COMPUTE_TOKEN', value='{}', **kwargs)

        self.server_url = server_url
        self.login_url = parse.urljoin(server_url, DEFAULT_LOGIN_PATH)
        self.openid_url = kwargs.get('openid_url', DEFAULT_OPENID_URL)
        self.verify = kwargs.get('verify', True)
        self.session = kwargs.get('session', None)

    def __repr__(self):
        text = 'LLNLAuthenticator(server_url={!r}, openid_url={!r}, verify={!r})'.format(
            self.server_url,
            self.openid_url,
            self.verify,
        )

        return text

    def _get_openid_redirect(self, session=None):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'openid_url': self.openid_url,
            'response': 'json',
        }

        if session is None:
            session = requests.Session()

        with session:
            response = session.get(self.login_url, headers=headers, verify=self.verify)

            try:
                headers['X-CSRFToken'] = response.cookies['csrftoken']
            except KeyError:
                logger.info('Did not find "csrftoken" in cookies')

            response = session.post(self.login_url, data=data, headers=headers, verify=self.verify)

            response.raise_for_status()

            data = response.json()

        try:
            redirect = data['data']['redirect']
        except KeyError as e:
            raise AuthenticationError('Server response missing key {!s}', e)

        return redirect

    def retrieve_token(self):
        if self.token is not None:
            return self.token

        url = self._get_openid_redirect(self.session)

        html_msg = HTML.format(url)

        plain_msg = PLAIN.format(url)

        from IPython.core.interactiveshell import InteractiveShell
        from IPython.display import display

        if not InteractiveShell.initialized():
            print(plain_msg)
        else:
            data = {'text/plain': plain_msg, 'text/html': html_msg}

            display(data, raw=True)

        token = input('Token: ')

        return token
