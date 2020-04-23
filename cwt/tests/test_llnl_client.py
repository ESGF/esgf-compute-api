import json

import pytest

import cwt
from cwt import llnl_client

JOB = {
    'id': '1',
    'process': 'CDAT.workflow',
    'elapsed': '3.11234',
    'latest_status': 'ProcessCompleted',
    'accepted_on': '1990-01-01',
    'status': [
        'https://wps.io/status/1',
        'https://wps.io/status/2',
    ],
}

JOB_LIST = {
    'next': 'http://wps.io/jobs/next',
    'previous': 'http://wps.io/jobs/previous',
    'results': [
        JOB,
    ]
}

MESSAGE_STATUS = {
    'status': 'ProcessAccepted',
    'created_date': '1990-01-01',
    'messages': [
        {
            'created_date': '1990-01-01',
            'message': 'Completed',
            'percent': '100',
        },
        {
            'created_date': '1990-01-01',
            'message': 'Running',
            'percent': '50',
        },
    ],
}

OUTPUT_STATUS = {
    'status': 'ProcessAccepted',
    'created_date': '1990-01-01',
    'output': json.dumps({"uri": "file:///test1.nc"}),
}

EXCEPTION_STATUS = {
    'status': 'ProcessAccepted',
    'created_date': '1990-01-01',
    'exception': 'Exception Text',
}

DOC = '<table><tr><th>Status</th><th>Created</th><th>Output</th></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left">1990-01-01 Completed 100</td></tr><tr><td></td><td></td><td style="text-align: left">1990-01-01 Running 50</td></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left"><a href="file:///test1.nc.html" target="_blank">file:///test1.nc</a></td></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left">Exception Text</td></tr></table>'

DOC_LIST = '<table><tr><th>ID</th><th>Operation</th><th>Elapsed</th><th>Status</th><th>Accepted</th></tr><tr><td>1</td><td>CDAT.workflow</td><td>3.11234</td><td>ProcessCompleted</td><td>1990-01-01</td></tr></table>'

def test_llnl_client_job(mocker):
    mocker.patch('cwt.wps_client.WPSClient._build_process_collection')

    client = llnl_client.LLNLClient('https://wps.io/wps')

    mocker.patch.object(client, 'jobs')

    jobs = client.job(0)

    client.jobs.return_value.__getitem__.assert_called_with(0)

def test_llnl_client_jobs(mocker):
    get = mocker.patch('cwt.llnl_client.requests.get')
    mocker.patch('cwt.wps_client.WPSClient._build_process_collection')

    client = llnl_client.LLNLClient('https://wps.io/wps')

    jobs = client.jobs()

    get.assert_called_with('https://wps.io/api/jobs/', headers={})

    assert isinstance(jobs, llnl_client.JobListWrapper)

def test_llnl_client_job_url(mocker):
    mocker.patch('cwt.wps_client.WPSClient._build_process_collection')

    client = llnl_client.LLNLClient('https://wps.io/wps')

    url = client._job_url()

    assert url == 'https://wps.io/api/jobs/'

def test_llnl_authenticator_remove_stored_token(mocker):
    remove = mocker.patch('cwt.llnl_client.os.remove')

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    auth.remove_stored_token()

    remove.assert_called_with(auth.config_path)

def test_llnl_authenticator_get_token_stored(mocker):
    auth = llnl_client.LLNLAuthenticator('https://wps.io', store_token=True)

    mocker.patch.object(auth, '_load_token', return_value=None)
    mocker.patch.object(auth, '_get_token', return_value='test')
    mocker.patch.object(auth, '_store_token')

    token = auth.get_token()

    assert token == 'test'

    auth._store_token.assert_called_with('test')

def test_llnl_authenticator_get_token_not_stored(mocker):
    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    mocker.patch.object(auth, '_load_token', return_value=None)
    mocker.patch.object(auth, '_get_token', return_value='test')
    mocker.patch.object(auth, '_store_token')

    token = auth.get_token()

    assert token == 'test'

def test_llnl_authenticator_get_token(mocker):
    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    mocker.patch.object(auth, '_load_token', return_value='test')
    mocker.patch.object(auth, '_get_token')
    mocker.patch.object(auth, '_store_token')

    token = auth.get_token()

    assert token == 'test'

def test_llnl_authenticator_get_token_priv(mocker):
    input = mocker.patch('builtins.input')

    input.return_value = 'abcd'

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    mocker.patch.object(auth, '_get_openid_redirect', return_value='https://wps.io/redirect')

    token = auth._get_token()

    assert token == 'abcd'

    input.assert_called_with('Token:')

def test_llnl_authenticator_load_token_override_token(mocker):
    auth = llnl_client.LLNLAuthenticator('https://wps.io', override_token=True)

    token = auth._load_token()

    assert token is None

def test_llnl_authenticator_load_token_open_error(mocker):
    _json = mocker.patch('cwt.llnl_client.json')
    open = mocker.patch('builtins.open')

    open.side_effect = Exception()

    _json.load.return_value = {'token': 'test'}

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    token = auth._load_token()

    assert token is None

def test_llnl_authenticator_load_token_malformed(mocker):
    _json = mocker.patch('cwt.llnl_client.json')
    open = mocker.patch('builtins.open')

    _json.load.return_value = {'token2': 'test'}

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    token = auth._load_token()

    assert token is None

def test_llnl_authenticator_load_token(mocker):
    _json = mocker.patch('cwt.llnl_client.json')
    open = mocker.patch('builtins.open')

    _json.load.return_value = {'token': 'test'}

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    token = auth._load_token()

    assert token == 'test'

    open.assert_called_with(auth.config_path)

    _json.load.assert_called_with(open.return_value.__enter__.return_value)

def test_llnl_authenticator_store_token(mocker):
    _json = mocker.patch('cwt.llnl_client.json')

    open = mocker.patch('builtins.open')

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    auth._store_token('test')

    open.assert_called_with(auth.config_path, 'w')

    _json.dump.assert_called_with({'token': 'test'}, open.return_value.__enter__.return_value)

def test_llnl_authenticator_bad_response(mocker):
    session = mocker.patch('cwt.llnl_client.requests.Session')

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    session.return_value.post.return_value.json.return_value = {"data": {}}

    with pytest.raises(llnl_client.AuthenticationError):
        redirect = auth._get_openid_redirect()

def test_llnl_authenticator_redirect(mocker):
    session = mocker.patch('cwt.llnl_client.requests.Session')

    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    session.return_value.post.return_value.json.return_value = {"data": {"redirect": "https://wps.io/redirect"}}

    redirect = auth._get_openid_redirect()

    session.return_value.post.assert_called()

    assert redirect == 'https://wps.io/redirect'

def test_llnl_authenticator():
    auth = llnl_client.LLNLAuthenticator('https://wps.io')

    assert auth.login_url == 'https://wps.io/api/openid/login/'
    assert auth.openid_url == 'https://esgf-node.llnl.gov/esgf-idp/openid'

def test_job_list_previous_no_previous(mocker):
    job = llnl_client.JobListWrapper(JOB_LIST)

    with pytest.raises(cwt.CWTError):
        job.previous()

def test_job_list_previous(mocker):
    job = llnl_client.JobListWrapper(JOB_LIST)

    job.index = 1

    job.pages.append(mocker.MagicMock())

    prev = job.previous()

    assert isinstance(prev, dict)
    assert job.index == 0

def test_job_list_next_no_next(mocker):
    mocker.patch('cwt.llnl_client.requests')

    mocker.patch.dict(JOB_LIST, {'next': None})

    job = llnl_client.JobListWrapper(JOB_LIST)

    with pytest.raises(cwt.CWTError):
        job.next()

def test_job_list_next(mocker):
    mocker.patch('cwt.llnl_client.requests')

    job = llnl_client.JobListWrapper(JOB_LIST)

    job.next()

    assert job.index == 1
    assert len(job.pages) == 2

def test_job_list_repr_html():
    job = llnl_client.JobListWrapper(JOB_LIST)

    data = job._repr_html_()

    assert data == DOC_LIST

def test_job_repr_html():
    job = llnl_client.JobWrapper(JOB)

    job.status = [MESSAGE_STATUS, OUTPUT_STATUS, EXCEPTION_STATUS]

    data = job._repr_html_()

    assert data == DOC

def test_job_wrapper_format_message():
    job = llnl_client.JobWrapper(JOB)

    msg = job._format_message({'created_date': '1990-01-01', 'message': 'Complete', 'percent': '50'})

    assert msg == '<td style="text-align: left">1990-01-01 Complete 50</td>'

def test_job_wrapper_get_statuses(mocker):
    r = mocker.patch('cwt.llnl_client.requests')

    job = llnl_client.JobWrapper(JOB)

    job._get_statuses()

    r.get.assert_called()
    r.get.return_value.json.assert_called()
