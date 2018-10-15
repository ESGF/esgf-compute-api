"""
WPS client unit tests
"""

import unittest

import mock
import pyxb
import requests
from pyxb.utils import domutils

import cwt
from cwt.wps import ows
from cwt.wps import wps
from cwt.wps import xlink

class TestWPSClient(unittest.TestCase):

    def setUp(self):
        identification = ows.service_identification('title', 'abstract')

        contact = ows.service_contact()

        provider = ows.service_provider('LLNL', contact)

        get_capabilities_op = ows.operation('GetCapabilities', get='http://idontexist/wps')

        describe_process_op = ows.operation('DescribeProcess', get='http://idontexist/wps')

        execute_op = ows.operation('Execute', get='http://idontexist/wps')

        metadata = ows.operations_metadata([
            get_capabilities_op,
            describe_process_op,
            execute_op,
        ])

        offerings = wps.process_offerings([
            wps.process('CDAT.subset', 'CDAT.subset', '1.0.0'),
            wps.process('CDAT.regrid', 'CDAT.regrid', '1.0.0'),
            wps.process('EDAS.max', 'EDAS.max', '1.0.0'),
        ])

        self.capabilities = wps.capabilities(identification, provider, metadata, offerings, 'en-US', '1.0.0')

        inputs = [
            wps.data_input_description('variable', 'Variable', 'application/json', 1, 1),
            wps.data_input_description('domain', 'Domain', 'application/json', 1, 1),
            wps.data_input_description('operation', 'Operation', 'application/json', 1, 1),
        ]

        outputs = [
            wps.process_output_description('output', 'Output', 'application/json')
        ]

        description_args = [
            'CDAT.subset',
            'CDAT.subset',
            '1.0.0',
            outputs
        ]

        description = wps.process_description(*description_args, metadata={'inputs': 1}, abstract='abstract text', data_inputs=inputs)

        self.process_descriptions = wps.process_descriptions('en-US', '1.0.0', [description])

        process = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        output = wps.output_data('output', 'Output', 'data')

        self.execute = wps.execute_response(process, wps.status_started('started', 10), '1.0.0', 'en-US', 'http://idontexist.com/', 'http://idontexist.com/status', [output])

        self.execute_failed = wps.execute_response(process, wps.status_failed('failed', 10, '1.0.0'), '1.0.0', 'en-US', 'http://idontexist.com/', 'http://idontexist.com/status', [output])

    def tearDown(self):
        cwt.bds.reset()

    @mock.patch('requests.Session.request')
    def test_processes_filter_error(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        with self.assertRaises(cwt.CWTError):
            processes = client.processes('*.subset')

    @mock.patch('requests.Session.request')
    def test_processes_filter(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        processes = client.processes('.*\.subset')

        self.assertEqual(len(processes), 1)

        process = processes[0]

        self.assertEqual(process.identifier, 'CDAT.subset')
        self.assertEqual(process.title, 'CDAT.subset')
        self.assertEqual(process.version, '1.0.0')

    @mock.patch('requests.Session.request')
    def test_processes(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        processes = client.processes()

        self.assertEqual(len(processes), 3)

    @mock.patch('requests.Session.request')
    def test_timeout(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', timeout=(5, 3))

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=(5, 3),
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=True)

    @mock.patch('requests.Session.request')
    def test_ssl_cert_tuple(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', cert=('/client.crt', '/client.key'))

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        cert=('/client.crt', '/client.key'),
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=True)

    @mock.patch('requests.Session.request')
    def test_ssl_cert(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', cert='/client.pem')

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        cert='/client.pem',
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=True)

    @mock.patch('requests.Session.request')
    def test_ssl_verify_ca_false(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', verify=False, ca='/test.pem')

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=False)

    @mock.patch('requests.Session.request')
    def test_ssl_verify_ca(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', ca='/test.pem')

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify='/test.pem')

    @mock.patch('requests.Session.request')
    def test_ssl_verify_false(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', verify=False)

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=False)

    @mock.patch('requests.Session.request')
    def test_ssl_verify(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        timeout=None,
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=True)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities(method='TEST')

    @mock.patch('requests.Session.request') 
    def test_describe_process_language(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        client.describe_process(cwt.Process.from_identifier('CDAT.subset'))

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('language', params)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_language(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        client.get_capabilities()

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('language', params)

    @mock.patch('requests.Session.request') 
    def test_version(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', version='1.0.0')

        client.get_capabilities()

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('acceptversions', params)

    def test_logging(self):
        client = cwt.WPSClient('http://idontexist/wps', log=True, log_file='./wps.log')

    @mock.patch('requests.Session.request') 
    def test_csrf_cookie_pass_through(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        mock_request.return_value.cookies = {'csrftoken': 'token'}

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_csrf_cookie(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        mock_request.return_value.cookies = {'csrftoken': 'token'}

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_invalid_status_code(self, mock_request):
        mock_request.return_value.status_code = 403

        mock_request.return_value.reason = 'Forbidden'

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_requests_exception(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        mock_request.side_effect = requests.HTTPError(response=mock.MagicMock(status_code=400, reason='Not Found'))

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_api_key(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        response = client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

    @mock.patch('requests.Session.request') 
    def test_execute_failed(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute_failed.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(Exception):
            client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

    @mock.patch('requests.Session.request')
    def test_execute_no_domain(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        client.execute(process, inputs=[cwt.Variable('file:///test1.nc', 'tas')])

        self.assertIsNotNone(process.response)

    @mock.patch('requests.Session.request') 
    def test_execute_no_inputs(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        client.execute(process, None, cwt.Domain([cwt.Dimension('time', 0, 365)]))

        self.assertIsNotNone(process.response)
        
    @mock.patch('requests.Session.request') 
    def test_execute_get(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]), method='GET')

        self.assertIsNotNone(process.response)
        
    @mock.patch('requests.Session.request') 
    def test_execute_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.WPSError):
            client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]), method='TEST')

    @mock.patch('requests.Session.request') 
    def test_execute_no_duplicates(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]), axes=['time'])

        self.assertEqual(len(process.parameters), 0)
        self.assertIsNone(process.domain)
        self.assertEqual(len(process.inputs), 0)
        self.assertIsNotNone(process.response)

    @mock.patch('requests.Session.request') 
    def test_execute_block(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        type(process).output = mock.PropertyMock(return_value='test output')

        process.wait = mock.MagicMock()

        process.description = mock.MagicMock()

        result = client.execute(process, 
                                [cwt.Variable('file:///test.nc', 'tas')],
                                cwt.Domain([cwt.Dimension('time', 0, 365)]), 
                                block=True)

        process.wait.assert_called()

        self.assertEqual(result, 'test output')

    @mock.patch('requests.Session.request') 
    def test_execute(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        process.description = mock.MagicMock()

        client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

        self.assertIsNotNone(process.response)

    def test_prepare_data_inputs_parameters(self):
        variable = cwt.Variable('file:///test.nc', 'tas', name='v0')

        domain = cwt.Domain([
            cwt.Dimension('time', 0, 365),
        ], name='d0')

        process = cwt.Process('CDAT.subset', name='subset')

        process.description = mock.MagicMock()

        process.description.metadata.return_value = {}

        client = cwt.WPSClient('http://idontexist/wps')

        data_inputs = client.prepare_data_inputs_str(process, [variable],
                                                     domain, axes=['lats',
                                                                   'lons'],
                                                     weightoptions='generated',
                                                    test=cwt.NamedParameter('test',
                                                                           'True'))

        expected = '[variable=[{"uri": "file:///test.nc", "id": "tas|v0"}];domain=[{"id": "d0", "time": {"start": 0, "step": 1, "end": 365, "crs": "values"}}];operation=[{"domain": "d0", "name": "CDAT.subset", "axes": "lats|lons", "result": "subset", "weightoptions": "generated", "test": "True", "input": ["v0"]}]]'

        self.assertEqual(expected, data_inputs)

    def test_prepare_data_inputs(self):
        variable = cwt.Variable('file:///test.nc', 'tas', name='v0')

        domain = cwt.Domain([
            cwt.Dimension('time', 0, 365),
        ], name='d0')

        process = cwt.Process('CDAT.subset', name='subset')

        process.description = mock.MagicMock()

        process.description.metadata.return_value = {}

        client = cwt.WPSClient('http://idontexist/wps')

        data_inputs = client.prepare_data_inputs_str(process, [variable], domain)

        expected = '[variable=[{"uri": "file:///test.nc", "id": "tas|v0"}];domain=[{"id": "d0", "time": {"start": 0, "step": 1, "end": 365, "crs": "values"}}];operation=[{"input": ["v0"], "domain": "d0", "name": "CDAT.subset", "result": "subset"}]]'

        self.assertEqual(expected, data_inputs)

    def test_parse_data_inputs(self):
        variable = '{"id": "tas|tas", "uri": "file:///test.nc"}'

        domain = '{"id": "test", "time": {"start": 0, "end": 365, "step": 1, "crs": "values"}}'

        operation = '{"name": "CDAT.subset", "input": ["tas"], "domain": "test"}'

        data_inputs = '[variable=[{}];domain=[{}];operation=[{}]]'.format(variable, domain, operation)

        operation, domain, variable = cwt.WPSClient.parse_data_inputs(data_inputs)

        self.assertEqual(len(operation), 1)
        self.assertEqual(len(domain), 1)
        self.assertEqual(len(variable), 1)

        self.assertIsInstance(operation[0], cwt.Process)
        self.assertIsInstance(domain[0], cwt.Domain)
        self.assertIsInstance(variable[0], cwt.Variable)

    @mock.patch('requests.Session.request') 
    def test_describe_process_post(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        description = client.describe_process(process, method='POST')

	self.assertIsInstance(description, list)
        self.assertIsInstance(description[0], cwt.ProcessDescriptionWrapper)

    @mock.patch('requests.Session.request') 
    def test_describe_process_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.WPSError):
            description = client.describe_process(process, method='TEST')

    @mock.patch('requests.Session.request') 
    def test_describe_process(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        description = client.describe_process(process)

	self.assertIsInstance(description, list)
        
        subset = description[0]

        self.assertIsInstance(subset, cwt.ProcessDescriptionWrapper)
        self.assertEqual(subset.identifier, 'CDAT.subset')
        self.assertEqual(subset.title, 'CDAT.subset')
        self.assertEqual(subset.abstract, 'abstract text')
        self.assertEqual(subset.metadata, {'inputs': '1'})

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_post(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        capabilities = client.get_capabilities(method='POST')

        self.assertIsNotNone(capabilities)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_get(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=cwt.bds)

        client = cwt.WPSClient('http://idontexist/wps')

        capabilities = client.get_capabilities()

        self.assertIsNotNone(capabilities)

if __name__ == '__main__':
    unittest.main()
