import os
import pytest

from cwt import llnl_client

@pytest.mark.live_server
def test_llnl_authenticator_redirect(mocker):
    auth = llnl_client.LLNLAuthenticator(login_url='https://nimbus16.llnl.gov:8443/api/openid/login/', verify=False)

    redirect = auth._get_openid_redirect()

    assert 'https://esgf-node.llnl.gov/esgf-idp/idp/openidServer.htm' in redirect


def test_store_load_token():
    auth = llnl_client.LLNLAuthenticator(login_url='https://nimbus16.llnl.gov:8443/api/openid/login/', verify=False)

    if os.path.exists(auth.config_path):
        os.remove(auth.config_path)

    auth._store_token('data')

    token = auth._load_token()

    assert token == 'data'

def test_get_token(mocker):
    mocker.patch('requests.post')

    mocker.patch('cwt.llnl_client.input', lambda *args, **kwargs: 'data')

    auth = llnl_client.LLNLAuthenticator(login_url='https://nimbus16.llnl.gov:8443/api/openid/login/', verify=False)

    if os.path.exists(auth.config_path):
        os.remove(auth.config_path)

    token = auth.get_token()

    assert token == 'data'
