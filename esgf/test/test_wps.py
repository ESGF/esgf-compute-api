"""
WPS unittest.
"""

from unittest import TestCase

from mock import call
from mock import Mock
from mock import patch
import requests

import esgf

BASE_URL = 'http://test/wps'

class ProxyResponse(object):
    def __init__(self, response, status_code):
        self._response = response
        self._status_code = status_code

    @property
    def text(self):
        return self._response

    @property
    def url(self):
        return 'Fake URL'

    @property
    def status_code(self):
        return self._status_code

    @property
    def reason(self):
        return 'Forbidden'

def read_response_file(file_path):
    data = []

    with open(file_path, 'r') as temp_file:
        data = temp_file.readlines()

    return ''.join(data)

def patch_request(request, response, status_code=200):
    proxy_response = ProxyResponse(response, status_code)

    request._session = Mock()
    request._session.get.return_value = proxy_response
    request._session.post.return_value = proxy_response

RESP_GET_CAP = read_response_file('esgf/test/test_data/get_capabilities.xml')
RESP_DESC_PROC = read_response_file('esgf/test/test_data/describe_process.xml')
RESP_EXEC = read_response_file('esgf/test/test_data/execute.xml')
RESP_EXEC_ERR = read_response_file('esgf/test/test_data/execute_error.xml')

class TestWPS(TestCase):
    """ WPS Test Case. """

    def test_wps_iter(self):
        """ Check process listing """
        wps = esgf.WPS(BASE_URL)

        patch_request(wps._service, RESP_GET_CAP)

        procs = [x for x in wps]

        self.assertEqual(len(procs), 6)
        self.assertEqual(procs, [
            'test.passthrough',
            'test.sleep',
            'test.echo',
            'cdat.aggregate',
            'cdat.ensemble',
            'cdat.averager',
        ])

    def test_wps_get_process(self):
        """ Process creation. """
        wps = esgf.WPS(BASE_URL)

        patch_request(wps._service, RESP_GET_CAP)

        with self.assertRaises(esgf.WPSClientError):
            proc = wps.get_process('cdat.averager2')

        proc = wps.get_process('cdat.averager')

        self.assertIsNotNone(proc)
        self.assertIsInstance(proc, esgf.Process)

    def test_wps_get_capabilities(self):
        """ Check GetCapbilities identification and provider response parsing. """
        wps = esgf.WPS(BASE_URL)

        patch_request(wps._service, RESP_GET_CAP)

        self.assertIsNotNone(wps.identification)
        self.assertIsNotNone(wps.provider)

    def test_wps_init(self):
        """ Call init """
        wps = esgf.WPS(BASE_URL)

        with self.assertRaises(esgf.WPSRequestError):
            wps.init()

        patch_request(wps._service, RESP_GET_CAP)

        wps.init()

        self.assertIsNotNone(wps._capabilities)
        self.assertIsInstance(wps._capabilities,
                              esgf.wps._WPSGetCapabilitiesResponse)

    def test_wps_log(self):
        """ Enable logging """
        wps = esgf.WPS(BASE_URL, log=True, log_file='test.log')

        self.assertEqual(len(esgf.wps.logger.handlers), 2)

    def test_wps_accept_versions(self):
        """ Specify acceptable server versions """
        wps = esgf.WPS(BASE_URL, accept_versions='1.0.0')

        patch_request(wps._service, RESP_GET_CAP)

        result = wps._service.get_capabilities()

        params = wps._service._session.get.mock_calls[-1][2]['params']

        self.assertEqual(params['AcceptedVersions'], '1.0.0')

    def test_wps(self):
        """ General creation """
        wps = esgf.WPS(BASE_URL)

        self.assertIsNotNone(wps)

    def test_wps_execute_input(self):
        """ Pass input to execute call """
        wps = esgf.WPS(BASE_URL)

        patch_request(wps._service, RESP_EXEC)

        tas = esgf.Variable('file:///tas.nc', 'tas', name='tas')

        op = esgf.Operation('cdat.averager', inputs=[tas], name='avg')

        wps.execute_op(op, method='GET')

        params = wps._service._session.get.mock_calls[-1][2]['params']

        expected = ('[variable=[{"uri":"file:///tas.nc","id":"tas|tas"}];'
                    'domain=[];'
                    'operation=[{"input":["tas"],"name":"cdat.averager","result":"avg"}]]')

        self.assertEquals(params['DataInputs'], expected)

    def test_request_load_xml(self):
        """ Load XML into response object """
        request = esgf.wps._WPSResponse()

        with self.assertRaises(esgf.WPSResponseError):
            request.load_xml(None)

        with self.assertRaises(esgf.WPSResponseError):
            request.load_xml('')

    def test_request_execute_output(self):
        """ Retrieve process output """
        request = esgf.wps._WPSRequest(BASE_URL)

        patch_request(request, RESP_EXEC)

        result = request.execute('cdat.averager', inputs={})

        with self.assertRaises(esgf.WPSClientError):
            result.output 

    def test_request_execute_error(self):
        """ Handle server side error response """
        request = esgf.wps._WPSRequest(BASE_URL)

        patch_request(request, RESP_EXEC_ERR)

        with self.assertRaises(esgf.WPSResponseError):
            request.execute('cdat.averager', inputs={})

    def test_request_execute_bad_method(self):
        """ Use a unsupported HTTP method """
        request = esgf.wps._WPSRequest(BASE_URL)

        patch_request(request, RESP_EXEC)

        with self.assertRaises(esgf.UnsupportedMethodError):
            result = request.execute('cdat.averager', inputs={}, method='UPDATE')

    def test_request_execute_status_store(self):
        """ Specify status and storeExecuteResponse flags """
        request = esgf.wps._WPSRequest(BASE_URL)

        patch_request(request, RESP_EXEC)

        result = request.execute('cdat.averager',
                                 inputs={},
                                 status=True,
                                 store=True,
                                 method='GET')

        params = request._session.get.mock_calls[-1][2]['params']

        self.assertEquals(params['status'], True)
        self.assertEquals(params['storeExecuteResponse'], True)

    def test_request_bad_status_code(self):
        """ Handle bad response status code """
        request = esgf.wps._WPSRequest(BASE_URL)

        patch_request(request, RESP_EXEC, 400)

        with self.assertRaises(esgf.WPSResponseError):
            request.execute('cdat.averager', inputs={}, method='GET')

        with self.assertRaises(esgf.WPSResponseError):
            request.execute('cdat.averager', inputs={})

    def test_request_auth(self):
        """ Pass authentication information """
        request = esgf.wps._WPSRequest(BASE_URL,
                                       username='wps_test',
                                       password='Abc123!!')

        patch_request(request, RESP_GET_CAP)

        request.get_capabilities()

        auth = request._session.get.mock_calls[-1][2]['auth']

        self.assertIsInstance(auth, requests.auth.HTTPBasicAuth)
        self.assertEqual(auth.username, 'wps_test')
        self.assertEqual(auth.password, 'Abc123!!')

    def test_request_language(self):
        """ Specify service language """
        request = esgf.wps._WPSRequest(BASE_URL, language='en-CA')

        patch_request(request, RESP_GET_CAP)

        request.get_capabilities()

        params = request._session.get.mock_calls[-1][2]['params']

        self.assertEqual(params['language'], 'en-CA')

    def test_execute_post(self):
        """ POST request execute """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.WPSRequestError):
            result = request.execute('cdat.averager', inputs={})

        patch_request(request, RESP_EXEC)

        result = request.execute('cdat.averager', inputs={})

        self.assertIsInstance(result, esgf.wps._WPSExecuteResponse)
        self.assertEqual(result.message, 'PyWPS Process cdat.averager successfully calculated')
        self.assertEqual(result.percent, 0)
        self.assertEqual(result.status, 'ProcessSucceeded')
        self.assertEqual(result.status_location, None)

    def test_execute_get(self):
        """ GET request execute """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.WPSRequestError):
            result = request.execute('cdat.averager', inputs={}, method='GET')

        patch_request(request, RESP_EXEC)

        result = request.execute('cdat.averager', inputs={}, method='GET')

        self.assertIsInstance(result, esgf.wps._WPSExecuteResponse)
        self.assertEqual(result.message, 'PyWPS Process cdat.averager successfully calculated')
        self.assertEqual(result.percent, 0)
        self.assertEqual(result.status, 'ProcessSucceeded')
        self.assertEqual(result.status_location, None)

    def test_describe_process_post(self):
        """ POST request DescribeProcess """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.UnsupportedMethodError):
            result = request.describe_process('cdat.averager', method='POST')

    def test_describe_process_get(self):
        """ GET request DescribeProcess """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.WPSRequestError):
            result = request.describe_process('cdat.averager')

        patch_request(request, RESP_DESC_PROC)

        result = request.describe_process('cdat.averager')

        self.assertIsInstance(result, esgf.wps._WPSDescribeProcessResponse)
        self.assertEqual(result.abstract, None)
        self.assertEqual(result.identifier, 'cdat.averager')
        self.assertEqual(result.status, True)
        self.assertEqual(result.store, True)
        self.assertEqual(result.title, 'CDUtil Averager')
        self.assertEqual(result.version, None)

    def test_get_capabilities_post(self):
        """ POST request GetCapabilities """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.UnsupportedMethodError):
            result = request.get_capabilities(method='POST')
    
    def test_get_capabilities_get(self):
        """ GET request GetCapabilities """
        request = esgf.wps._WPSRequest(BASE_URL)

        with self.assertRaises(esgf.WPSRequestError):
            result = request.get_capabilities()

        patch_request(request, RESP_GET_CAP)

        result = request.get_capabilities()

        self.assertIsInstance(result, esgf.wps._WPSGetCapabilitiesResponse)
        self.assertIsNotNone(result.identification)
        self.assertIsNotNone(result.provider)
        self.assertEqual(result.processes, [
            'test.passthrough',
            'test.sleep',
            'test.echo',
            'cdat.aggregate',
            'cdat.ensemble',
            'cdat.averager',
        ])
