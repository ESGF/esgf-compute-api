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
