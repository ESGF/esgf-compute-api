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

def test_authenticator(mocker, temp_file):
    class CustomAuth(auth.Authenticator):
        def _pre_prepare(self, headers, query, store):
            headers.update({"key1": "value1"})

            query.update({"key2": "value2"})

    custom = CustomAuth(config_path=temp_file)

    headers = {}
    query = {}

    custom.prepare(headers, query)

    assert headers == {"key1": "value1"}
    assert query == {"key2": "value2"}
