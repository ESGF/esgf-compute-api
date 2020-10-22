import sys
import re
import hashlib
import base64
import json
import os
import random
import datetime
from http import server
import logging

import requests
from oauthlib import oauth2

from cwt import errors

logger = logging.getLogger("cwt.auth")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"

class Authenticator(object):
    """Base authenticator.
    """
    def __init__(self, key=None, config_path=None, store=True):
        """Authenticator __init__.

        Args:
            config_path: File to store credentials.
            store: Store credentials in config_path
        """
        self.key = key or "default"
        self.store = store
        self.config_path = config_path or os.path.expanduser("~/.cwt.json")

    def write(self, data):
        """Writes credentials.

        Args:
            data: Dict mapping keys to credential store.
        """
        logger.info("Writing credential store")

        with open(self.config_path, 'w') as fp:
            fp.write(json.dumps(data))

    def read(self):
        """Reads credentials.

        Returns:
            A dict storing credentials.
        """
        data = {}

        logger.info("Reading credential store")

        if os.path.exists(self.config_path):
            with open(self.config_path) as fp:
                data = fp.read()

            data = json.loads(data)

        return data

    def clear(self):
        """Removes a stored credential.

        Args:
            key: Identifier of credentials to remove.
        """
        data = self.read()

        if self.key in data:
            del data[self.key]

        self.write(data)

    def prepare(self, headers, query):
        """Retrieves credentials.

        Args:
            key: Identifier of credentials.
            headers: Dict to append authorization headers.
            query: Dict to append authorization parameters.
        """
        data = self.read()

        state = self._pre_prepare(headers, query, data.get(self.key, {}))

        if self.store:
            logger.info("Storing credentials")

            data[self.key] = state

            self.write(data)

        del data

class BearerToken(Authenticator):
    """Bearer token authenticator.
    """

    def __init__(self, token=None, **kwargs):
        self._token = token

        super(BearerToken, self).__init__(**kwargs)

    def _pre_prepare(self, headers, query, store):
        store["token"] = self._token

        headers["Authorization"] = "Bearer {}".format(self._token)

        return store

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
    def __init__(self, url, realm, client_id=None, client_secret=None, pkce=False, redirect_port=None, **kwargs):
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
        self._redirect_port = redirect_port or 8888
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

            logger.info("Retrieved well known document")

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
            redirect_uri=f"http://127.0.0.1:{self._redirect_port}",
            state=state,
            **kwargs)

        print(f"Open following url in a browser")
        print("")
        print(f"{auth_url}")

        try:
            listen = server.HTTPServer(("", self._redirect_port), ResponseListener)
        except PermissionError:
            print(f"""
Failed to bind redirect port {self._redirect_port}.

Try changing the redirect port.
<<< auth = LLNLKeyCloakAuthenticator(..., redirect_port=9000)

Or use client credentials method.
            """)

            sys.exit(1)

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
            redirect_uri=f"http://127.0.0.1:{self._redirect_port}",
            **kwargs)

        headers = {"Content-type": "application/x-www-form-urlencoded"}

        response = requests.post(url, data=request, headers=headers)

        response.raise_for_status()

        data = response.json()

        data["acquired"] = datetime.datetime.now().isoformat()

        return data

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

    def _refresh_token(self, known, client, refresh_token, client_secret=None):
        """Refresh access token.

        Args:
            known: Dict containing well known document.
            client: A WebApplicationClient instance.
            refresh_token: Refresh token.

        Returns:
            A dict containing a token response generated by using
            a refresh token.
        """
        logger.info("Refreshing access token")

        kwargs = {
            "client_id": self._client_id,
        }

        if client_secret is not None:
            kwargs["client_secret"] = client_secret

        url, headers, body = client.prepare_refresh_token_request(
            known["token_endpoint"],
            refresh_token=refresh_token,
            **kwargs)

        response = requests.post(url, data=body, headers=headers)

        response.raise_for_status()

        data = response.json()

        data["acquired"] = datetime.datetime.now().isoformat()

        return data

    def _check_refresh_expired(self, store):
        refresh_expires_in = None

        if "refresh_expires_in" in store:
            aquired = datetime.datetime.fromisoformat(store["acquired"])

            refresh_expires_in = aquired + datetime.timedelta(seconds=store["refresh_expires_in"])

        now = datetime.datetime.now()

        logger.info(f"Refresh token expires at {refresh_expires_in} {now}")

        if refresh_expires_in is not None and now <= refresh_expires_in:
            return False

        return True

    def _get_client_credentials_token(self, known, client, client_secret):
        logger.info("Getting client credentials")

        request_body = client.prepare_request_body(
            include_client_id=True,
            client_secret=client_secret)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(
            known["token_endpoint"],
            headers = headers,
            data = request_body)

        data = response.json()

        if "error" in data:
            raise errors.WPSAuthError(data["error_description"])

        data["acquired"] = datetime.datetime.now().isoformat()

        return data

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

        if self._client_id is not None and self._pkce:
            logger.info(f"Using authorization code flow")

            client = oauth2.WebApplicationClient(self._client_id)

            if self._check_refresh_expired(store):
                store = self._get_access_token(known, client)
            else:
                store = self._refresh_token(known, client, store["refresh_token"])
        else:
            logger.info(f"Using client credentials flow")

            client_id = store.get("client_id", self._client_id)

            client_secret = store.get("client_secret", self._client_secret)

            client = oauth2.BackendApplicationClient(client_id)

            store = self._get_client_credentials_token(known, client, client_secret)

            store["client_id"] = client_id

            store["client_secret"] = client_secret

        headers.update({
            "Authorization": f"Bearer {store['access_token']}",
        })

        return store
