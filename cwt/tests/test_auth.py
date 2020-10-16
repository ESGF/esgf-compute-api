import pytest
import tempfile
import json
import os

from cwt import auth

@pytest.fixture
def temp_file():
    yield "cwt.json"

    if os.path.exists("cwt.json"):
        os.remove("cwt.json")

def test_token_authenticator(mocker, temp_file):
    token = auth.TokenAuthenticator('test_token', config_path=temp_file)

    headers = {}
    params = {}

    dumps = mocker.spy(json, 'dumps')

    token.prepare("key1", headers, params)

    assert 'Authorization' not in params
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Bearer test_token'

    token.prepare("key1", headers, params)

    token = auth.TokenAuthenticator('test_token', config_path=temp_file)

    token.clear("key1")

def test_authenticator(mocker, temp_file):
    class CustomAuth(auth.Authenticator):
        def _pre_prepare(self, headers, query, store):
            headers.update({"key1": "value1"})

            query.update({"key2": "value2"})

    custom = CustomAuth(config_path=temp_file)

    headers = {}
    query = {}

    custom.prepare("key1", headers, query)

    assert headers == {"key1": "value1"}
    assert query == {"key2": "value2"}
