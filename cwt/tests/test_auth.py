import json
import os

from cwt import auth

def test_token_authenticator(mocker):
    token = auth.TokenAuthenticator('test_token')

    if os.path.exists(token.config_path):
        os.remove(token.config_path)

    headers = {}
    params = {}

    dumps = mocker.spy(json, 'dumps')

    token.prepare(headers, params)

    assert 'Authorization' not in params
    assert 'Authorization' in headers

    assert headers['Authorization'] == 'Bearer test_token'

    dumps.assert_not_called()

def test_authenticator(mocker):
    class CustomAuthenticator(auth.Authenticator):
        def prepare(self, headers, query):
            headers['TEST'] = 'token'

            query['TEST'] = 'token'

            super().prepare(headers, query)

        def to_dict(self):
            return {'data': 'token'}

        def from_dict(self, data):
            self.data = data

    custom = CustomAuthenticator()

    expected_path = os.path.expanduser('~/.cwt.json')

    assert custom.config_path == expected_path
    assert custom.store is False

    dump = mocker.spy(json, 'dumps')

    custom.write()

    dump.assert_called_with({'data': 'token'})

    load = mocker.spy(json, 'loads')

    custom.read()

    load.assert_called_with('{"data": "token"}')

    remove = mocker.spy(os, 'remove')

    custom.clear()

    remove.assert_called_with(expected_path)

    headers = {}
    params = {}

    if os.path.exists(expected_path):
        os.path.remove(expected_path)

    custom = CustomAuthenticator(store=True)

    assert custom.store
    assert not custom.loaded

    write = mocker.spy(custom, 'write')

    custom.prepare(headers, params)

    write.assert_called()

    assert 'TEST' in headers
    assert 'TEST' in params

    custom.prepare(headers, params)

    # Shouldn't call write twice
    assert dump.call_count == 2
