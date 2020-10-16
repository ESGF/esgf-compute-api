import re
import hashlib
import base64
import json
import os
import random
import datetime
from http import server

import requests
from oauthlib import oauth2

class Authenticator(object):
    """Base authenticator.
    """
    def __init__(self, config_path=None, store=True):
        """Authenticator __init__.

        Args:
            config_path: File to store credentials.
            store: Store credentials in config_path
        """
        self.store = store
        self.config_path = config_path or os.path.expanduser("~/.cwt.json")

    def write(self, data):
        """Writes credentials.

        Args:
            data: Dict mapping keys to credential store.
        """
        with open(self.config_path, 'w') as fp:
            fp.write(json.dumps(data))

    def read(self):
        """Reads credentials.

        Returns:
            A dict storing credentials.
        """
        data = {}

        if os.path.exists(self.config_path):
            with open(self.config_path) as fp:
                data = fp.read()

            data = json.loads(data)

        return data

    def clear(self, key):
        """Removes a stored credential.

        Args:
            key: Identifier of credentials to remove.
        """
        data = self.read()

        if key in data:
            del data[key]

        self.write(data)

    def prepare(self, key, headers, query):
        """Retrieves credentials.

        Args:
            key: Identifier of credentials.
            headers: Dict to append authorization headers.
            query: Dict to append authorization parameters.
        """
        data = self.read()

        state = self._pre_prepare(headers, query, data.get(key, {}))

        data[key] = state

        self.write(data)

        del data

class TokenAuthenticator(Authenticator):
    """Simple token authenticator.
    """
    def __init__(self, token=None, **kwargs):
        """TokenAuthenticator __init__.

        Args:
            token: Token to place in headers.
            **kwargs: Arguments for base authenticator.
        """
        self.token = token

        super().__init__(**kwargs)

    def _pre_prepare(self, headers, query, store):
        """Prepares headers or query.

        Args:
            headers: dict to append authorization headers.
            query: dict to append authorization parameters.
            store: dict containing store credentials.
        """
        headers.update({"Authorization": f"Bearer {self.token}"})

class ResponseListener(server.BaseHTTPRequestHandler):
    """Callback server for authorization request.
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Success</title></head><body>You can now close the tab/window</body></html>")

        ResponseListener.uri = self.path

class KeyCloakAuthenticator(Authenticator):
    """KeyCloak authenticator.
    """
    def __init__(self, url, realm, client_id, client_secret=None, pkce=False, **kwargs):
        """KeyCloakAuthenticator __init__.

        Args:
            url: Base url to KeyCloak instance.
            realm: Authentication realm.
            client_id: OAuth2 client id.
            client_secret: OAuth2 client secret used with confidential client.
            pkce: Use PKCE with public client.
            **kwargs: Arguments for Authenticator class.
        """
        self._url = url if url[-1] != "/" else url[:-1]
        self._realm = realm
        self._client_id = client_id
        self._client_secret = client_secret
        self._pkce = pkce
        self._well_known = None

        super().__init__(**kwargs)

    def _get_well_known(self):
        """Retrieves well known document.

        Returns:
            A dict containing the well known document.
        """
        if self._well_known is None:
            response = requests.get(f"{self._url}/realms/{self._realm}/.well-known/openid-configuration")

            response.raise_for_status()

            self._well_known = response.json()

        return self._well_known

    def _code_verifier(self):
        """Generates code verifier for PKCE.

        Returns:
            A str containing code verififer.
        """
        verifier = base64.urlsafe_b64encode(os.urandom(40)).decode("utf-8")

        return re.sub("[^a-zA-Z0-9]+", "", verifier)

    def _code_challenge(self, code_verififer):
        """Generates code challenge for PKCE.

        Args:
            code_verifier: Code verifier to create challenge with.

        Returns:
            A str containing the code challenge.
        """
        challenge = hashlib.sha256(code_verififer.encode("utf-8")).digest()

        challenge = base64.urlsafe_b64encode(challenge).decode("utf-8")

        return challenge.replace("=", "")

    def _get_auth_response(self, client, url, **kwargs):
        """Gets authorization response.

        Args:
            client: A WebApplicationClient instance.
            url: URL for authorization endpoint.
            **kwargs: Additional arguments used generate authorization request.

        Returns:
            A dict containing the authorization response.
        """
        state = ''.join([str(random.randint(0, 9)) for i in range(16)])

        auth_url = client.prepare_request_uri(
            url,
            redirect_uri="http://127.0.0.1:8888",
            state=state,
            **kwargs)

        print(f"Open following url in a browser")
        print("")
        print(f"{auth_url}")

        listen = server.HTTPServer(("", 8888), ResponseListener)
        listen.handle_request()
        listen.server_close()

        auth_response = client.parse_request_uri_response(
            ResponseListener.uri,
            state=state)

        return auth_response

    def _get_token_response(self, client, code, url, **kwargs):
        """Gets token response.

        Args:
            client: A WebApplicationClient instance.
            code: Authorization code.
            url: URL for token endpoint.
            **kwargs: Additional arguments used to generate token request.

        Returns:
            A dict containing the token response.
        """
        request = client.prepare_request_body(
            code,
            redirect_uri="http://127.0.0.1:8888",
            **kwargs)

        headers = {"Content-type": "application/x-www-form-urlencoded"}

        response = requests.post(url, data=request, headers=headers)

        response.raise_for_status()

        return response.json()

    def _authorization_code_pkce(self, known, client):
        """Performs authorization code flow with PKCE.

        Args:
            known: Dict containing well known document.
            client: A WebApplicationClient instance.

        Returns:
            A dict containing token response.
        """
        if self._client_secret is not None:
            logger.warning("Ignoring 'client_secret', preferring PKCE.")

        verifier = self._code_verifier()

        challenge = self._code_challenge(verifier)

        auth_response = self._get_auth_response(
            client,
            known["authorization_endpoint"],
            code_challenge=challenge,
            code_challenge_method="S256")

        token_response = self._get_token_response(
            client,
            auth_response["code"],
            known["token_endpoint"],
            code_verifier=verifier)

        return token_response

    def _authorization_code(self, known, client):
        """Peforms authorization code flow.

        Args:
            known: Dict containing well known document.
            client: A WebApplicationClient instance.

        Returns:
            A dict containing a token response.
        """
        if self._client_secret is None:
            raise WPSAuthenticationError("Must pass 'client_secret' if not using PKCE.")

        auth_response = self._get_auth_response(
            client,
            known["authorization_endpoint"],
            client_secret=self._client_secret)

        token_response = self._get_token_response(
            client,
            auth_response["code"],
            known["token_endpoint"])

        return token_response

    def _get_access_token(self, known, client):
        """Performs specific authorization code flow.

        Args:
            known: Dict containing well known document.
            client: A WebApplicationClient instance.

        Returns:
            A dict containing a token response.
        """
        if self._pkce:
            kwargs = self._authorization_code_pkce(known, client)
        else:
            kwargs = self._authorization_code(known, client)

        return kwargs

    def _refresh_token(self, known, client, refresh_token):
        """Refresh access token.

        Args:
            known: Dict containing well known document.
            client: A WebApplicationClient instance.
            refresh_token: Refresh token.

        Returns:
            A dict containing a token response generated by using
            a refresh token.
        """
        url, headers, body = client.prepare_refresh_token_request(
            known["token_endpoint"],
            refresh_token=refresh_token,
            client_id=self._client_id)

        response = requests.post(url, data=body, headers=headers)

        response.raise_for_status()

        return response.json()

    def _pre_prepare(self, headers, query, store):
        """Prepares authorization headers.

        Args:
            headers: Dict to store authorization headers.
            query: Dict to store authorization query parameters.
            store: Dict storing existing credentials.

        Returns:
            A dict containing updated credentials to be stored.
        """
        known = self._get_well_known()

        client = oauth2.WebApplicationClient(self._client_id)

        refresh_expires_in = None if "refresh_expires_in" not in store else \
            datetime.datetime.fromisoformat(store["refresh_expires_in"])

        now = datetime.datetime.now()

        if refresh_expires_in is not None and now <= refresh_expires_in:
            store = self._refresh_token(known, client, store["refresh_token"])
        else:
            store = self._get_access_token(known, client)

        headers.update({
            "Authorization": f"Bearer {store['access_token']}",
        })

        return store
