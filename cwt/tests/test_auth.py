import pytest
import tempfile
import json
import os

from cwt import auth

@pytest.fixture(scope="function")
def temp_file():
    if os.path.exists("cwt.txt"):
        os.remove("cwt.txt")

    try:
        yield "cwt.txt"
    finally:
        if os.path.exists("cwt.txt"):
            os.remove("cwt.txt")

def test_custom_authenticator(mocker, temp_file):
    class CustomAuth(auth.Authenticator):
        def _pre_prepare(self, headers, query, store):
            headers["test"] = "header"

            query["test"] = "query"

            store["test"] = {
                "data": "test",
            }

            return store

    client = CustomAuth()

    headers = {}
    query = {}

    client.prepare(headers, query)

    assert headers == {"test": "header"}
    assert query == {"test": "query"}

    data = client.read()

    assert data == {"default": {"test": { "data": "test"}}}


def test_authenticator(mocker, temp_file):
    client = auth.Authenticator(key="test", config_path=temp_file)

    assert client.config_path == "cwt.txt"

    client.write({"test": "data1"})

    data = client.read()

    assert data == {"test": "data1"}

    client.clear()

    data = client.read()

    assert data == {}
