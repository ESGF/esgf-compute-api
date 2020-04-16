import json
import requests
import os
from urllib import parse

import cwt
from cwt import CWTError

DEFAULT_LOGIN_PATH = '/api/openid/login/'
DEFAULT_JOB_PATH = '/api/jobs/'
DEFAULT_OPENID_URL = 'https://esgf-node.llnl.gov/esgf-idp/openid'

class AuthenticationError(CWTError):
    pass

class JobStatusError(CWTError):
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

                    data.append('<td style="text-align: left"><a href="{uri}.html" target="_blank">{uri}</a></td>'.format(**x))
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

    def __init__(self, data, headers=None):
        """ JobListWrapper init.

        Args:
            data (dict): JSON output from jobs api.
            headers (dict, optional): Headers used to communicate with the server.
        """
        if headers is None:
            headers = {}

        self.index = 0
        self.jobs = {}
        self.pages = [data,]
        self.headers = headers

    @property
    def current(self):
        """ Returns current page.
        """
        return self.pages[self.index]

    def next(self):
        """ Retrieves the next page of jobs.
        """
        next = self.current['next']

        if next is None:
            raise CWTError('No more pages left')

        response = requests.get(next, headers=self.headers)

        response.raise_for_status()

        self.pages.append(response.json())

        self.index += 1

        return self.current

    def previous(self):
        """ Moves to the previous page.
        """
        if (self.index - 1) < 0:
            raise CWTError('No previous page available')

        self.index -= 1

        return self.current

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

        header = ''.join(['<th>{}</th>'.format(name) for (_, name) in columns])

        return '<table><tr>{header}</tr>{rows}</table>'.format(header=header, rows=rows)

    def _find_job_by_id(self, id):
        for x in self.pages:
            for y in x['results']:
                if y['id'] == id:
                    return y

        return None

    def __getitem__(self, id):
        job = self._find_job_by_id(id)

        if job is None:
            raise KeyError(id)

        if id not in self.jobs:
            self.jobs[id] = JobWrapper(job, self.headers)

        return self.jobs[id]

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

    def job(self, id):
        """ Retrieves specific job by id.

        Args:
            id (int): Identifier of the target job.
        """
        jobs = self.jobs()

        return jobs[id]

    def jobs(self):
        """ Retrieves listing of jobs.
        """
        if self._listing is None:
            job_url = self._job_url()

            response = requests.get(job_url, headers=self.headers)

            data = response.json()

            self._listing = JobListWrapper(data, self.headers)

        return self._listing

class LLNLAuthenticator(object):
    """ LLNLAuthenticator.
    """

    def __init__(self, server_url, **kwargs):
        """ LLNLAuthenticator __init__.

        Args:
            server_url (str): The base url of the WPS server.
            openid_url (str, optional): A url to the OpenID authentication server.
            verify (bool, optional): Verify SSL certificate.
            override_token (bool, optional): Will overwrite the currently stored token.
            store_token (bool, optional): Will write token to ~/.cwt.
        """
        self.login_url = parse.urljoin(server_url, DEFAULT_LOGIN_PATH)
        self.openid_url = kwargs.get('openid_url', DEFAULT_OPENID_URL)
        self.verify = kwargs.get('verify', True)
        self.override_token = kwargs.get('override_token', False)
        self.store_token = kwargs.get('store_token', False)

        self.config_path = os.path.expanduser('~/.cwt')

    def _get_openid_redirect(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'openid_url': self.openid_url,
            'response': 'json',
        }

        response = requests.post(self.login_url, data=data, headers=headers, verify=self.verify)

        response.raise_for_status()

        data = response.json()

        try:
            redirect = data['data']['redirect']
        except KeyError as e:
            raise AuthenticationError('Server response missing key {!s}', e)

        return redirect

    def _store_token(self, token):
        with open(self.config_path, 'w') as outfile:
            json.dump({'token': token}, outfile)

    def _load_token(self):
        if self.override_token:
            return None

        try:
            with open(self.config_path) as infile:
                data = json.load(infile)
        except Exception:
            token = None
        else:
            try:
                token = data['token']
            except KeyError:
                token = None

        return token

    def _get_token(self):
        url = self._get_openid_redirect()

        msg = ('Navigate to the following url in a browser and copy the "token" field from the response.\n\n'
               '{url!s}\n\n')

        print(msg.format(url=url))

        token = input('Token:')

        return token

    def remove_stored_token(self):
        """ Removes stored token.
        """
        os.remove(self.config_path)

    def get_token(self):
        """ Gets a user token.

        If the token has been stored then it will be returned. Otherwise you will be led
        through the login process and a token will be returned. You'll be prompted to enter
        the token, which will stored if configured to.
        """
        token = self._load_token()

        if token is None:
            token = self._get_token()

            if self.store_token or self.override_token:
                self._store_token(token)

        return token
