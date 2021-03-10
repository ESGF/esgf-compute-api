# Authentication

* [BearerTokenAuthenticator](#BearerTokenAuthenticator)
* [LLNLKeyCloakAuthenticator](#LLNLKeyCloakAuthenticator)
* [CustomAuthenticator](#CustomAuthenticator)

## BearerTokenAuthenticator

This authenticator works by taking a token and passing it an `Authorization: bearer` header with the execute request.

```python
import cwt
from cwt import auth

bearer = auth.BearerTokenAuthenticator(token="abcd")

client = cwt.WPSClient("https://wps.io/wps", auth=auth)

client.execute(...)
```

## LLNLKeyCloakAuthenticator

To use the LLNLKeyCloakAuthenticator you will need the following information:

- Base url for the WPS compute node.
- Url to the keycloak instance.
- Realm name being used.

### Authorization Code with PKCE

This authentication flow requires a KeyCloak public client to be configured for OAuth2 Authorization Code flow with PKCE. Once `execute` is called the user will be presented with a link. Upon opening the link in a browser they'll be redirect to authenticate with keycloak, once successfully authenticated they'll be redirect to a local URL and the job will execute.

***WARNING*** This authentication method will only work if performed on a host system where port `8888` by default is open, this port can be changed.

***Note*** The client id is required.

```python
from cwt import llnl_client

auth = llnl_client.LLNLKeyCloakAuthenticator(
    base_url="https://compute.node",
    keycloak_url="https://compute.node/auth",
    realm="compute-cluster",
    client_id="wps",
    pkce=True
)

client = llnl_client.LLNLClient("https://aims2.llnl.gov/wps", auth=auth)

client.execute(...)
```

#### Alternative port

```python
auth = llnl_client.LLNLKeyCloakAuthenticator(..., pkce=True, redirect_port=8000)
```

### Client Credentials

This authentication flow requires a KeyCloak confidential client to be configured for OAuth2 Client Credentials flow. Once `execute` is called the user will be presented with a link. Upon opening this link in a browser they'll be redirect to authenticate with keycloak, once successfully authenticated they'll be issued a *Client ID* and *Client Secret*, these are to be kept secret. The user will be prompted for both items and once entered the job will execute.

```python
from cwt import llnl_client

auth = llnl_client.LLNLKeyCloakAuthenticator(
    base_url="https://compute.node",
    keycloak_url="https://compute.node/auth",
    realm="compute-cluster",
)

client = llnl_client.LLNLClient("https://aims2.llnl.gov/wps", auth=auth)

client.execute(...)
```

## CustomAuthenticator

A custom authenticator can be implemented by subclassing `Authenticator` and implementing the `_pre_prepare(self, headers, query, store)` method. In this method you can mutate `headers` and `query` with which will be amended to the HTTP request headers and query parameters. The authenticator can choose to store information for later calls using the `store` variable.

```python
from cwt import auth

class CustomAuthenticator(auth.Authenticator):
  def __init__(self, secret):
    self.secret = secret

    super(CustomAuthenticator).__init__()

  def use_secret(self):
    ...

  def _pre_prepare(self, headers, query, store):
    # Get previouse stored code or get the code
    code = store.get("code", self.use_secret())

    # Mutate the HTTP headers
    headers["TOKEN"] = code

    # Store the code for later
    store["code"] = code

    return store
```
