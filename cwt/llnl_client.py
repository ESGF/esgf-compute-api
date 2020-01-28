import json
import requests
import os

from cwt import CWTError

DEFAULT_LOGIN_URL = 'https://aims2.llnl.gov/api/openid/login/'
DEFAULT_OPENID_URL = 'https://esgf-node.llnl.gov/esgf-idp/openid'

try:
    import ipywidgets
    from IPython.display import display
except ModuleNotFoundError:
    IS_IPYNB=False
else:
    IS_IPYNB=True


class AuthenticationError(CWTError):
    pass


class LLNLAuthenticator(object):
    def __init__(self, **kwargs):
        self.login_url = kwargs.get('login_url', DEFAULT_LOGIN_URL)
        self.openid_url = kwargs.get('openid_url', DEFAULT_OPENID_URL)
        self.verify = kwargs.get('verify', True)
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

        if IS_IPYNB:
            display(ipywidgets.HTML('Click "Login" button and copy the "token" field from the response.'))

            display(ipywidgets.HTML('<a class="p-Widget jupyter-widgets jupyter-button widget-button" href="{url}" target="_blank">Login</a>'.format(url=url)))
        else:
            msg = ('Navigate to the following url in a browser and copy the "token" field from the response.\n\n'
                   '{url!s}\n\n')

            print(msg.format(url=url))

        token = input('Token:')

        return token

    def remove_stored_token(self):
        os.remove(self.config_path)

    def get_token(self):
        token = self._load_token()

        if token is None:
            token = self._get_token()

            if self.store_token:
                self._store_token(token)

        return token
