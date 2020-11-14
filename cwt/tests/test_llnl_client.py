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

DOC = '<table><tr><th>Status</th><th>Created</th><th>Output</th></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left">1990-01-01 Completed 100</td></tr><tr><td></td><td></td><td style="text-align: left">1990-01-01 Running 50</td></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left"><pre><a href="file:///test1.nc" target="_blank">file:///test1.nc</a></pre></td></tr><tr><td>ProcessAccepted</td><td>1990-01-01</td><td style="text-align: left">Exception Text</td></tr></table>'

DOC_LIST = '<div><h2>Jobs</h2></div><table><tr><th>ID</th><th>Operation</th><th>Elapsed</th><th>Status</th><th>Accepted</th></tr><tr><td>1</td><td>CDAT.workflow</td><td>3.11234</td><td>ProcessCompleted</td><td>1990-01-01</td></tr></table></div><div></div>'

def test_llnl_client_jobs(mocker):
    get = mocker.patch('cwt.llnl_client.requests.get')
    mocker.patch('cwt.wps_client.WPSClient._build_process_collection')

    client = llnl_client.LLNLClient('https://wps.io/wps')

    jobs = client.jobs()

    get.assert_called_with('https://wps.io/wps/api/job/', headers={}, params={'limit': 10})

    assert isinstance(jobs, llnl_client.JobListWrapper)

def test_llnl_client_job_url(mocker):
    mocker.patch('cwt.wps_client.WPSClient._build_process_collection')

    client = llnl_client.LLNLClient('https://wps.io/wps')

    url = client._job_url()

    assert url == 'https://wps.io/wps/api/job/'

def test_job_list_next(mocker):
    mocker.patch('cwt.llnl_client.requests')

    job = llnl_client.JobListWrapper('https://wps.io/api/jobs', JOB_LIST)

    job.next()

    assert len(job.pages) == 2

def test_job_list_repr_html():
    job = llnl_client.JobListWrapper('https://wps.io/api/jobs', JOB_LIST)

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
