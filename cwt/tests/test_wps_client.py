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

bds = domutils.BindingDOMSupport()

bds.declareNamespace(ows.Namespace, prefix='ows')

bds.declareNamespace(wps.Namespace, prefix='wps')

bds.declareNamespace(xlink.Namespace, prefix='xlink')

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

        description = wps.process_description('CDAT.subset', 'CDAT.subset', '1.0.0', inputs, outputs)

        self.process_descriptions = wps.process_descriptions('en-US', '1.0.0', [description])

        process = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        output = wps.output_data('output', 'Output', 'data')

        self.execute = wps.execute_response(process, wps.status_started('started', 10), '1.0.0', 'en-US', 'http://idontexist.com/', 'http://idontexist.com/status', [output])

        self.execute_failed = wps.execute_response(process, wps.status_failed('failed', 10, '1.0.0'), '1.0.0', 'en-US', 'http://idontexist.com/', 'http://idontexist.com/status', [output])

    def tearDown(self):
        bds.reset()

    @mock.patch('requests.Session.request')
    def test_ssl_verify_false(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', verify=False)

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=False)

    @mock.patch('requests.Session.request')
    def test_ssl_verify(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        client.get_capabilities()

        mock_request.assert_called_with('GET', 'http://idontexist/wps', 
                                        params={'request': 'GetCapabilities', 
                                                'service': 'WPS'}, 
                                        data=None, headers={}, verify=True)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities(method='TEST')

    @mock.patch('requests.Session.request') 
    def test_describe_process_language(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        client.describe_process(cwt.Process.from_identifier('CDAT.subset'))

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('language', params)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_language(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', language='en-US')

        client.get_capabilities()

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('language', params)

    @mock.patch('requests.Session.request') 
    def test_version(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', version='1.0.0')

        client.get_capabilities()

        params = mock_request.call_args_list[0][1]['params']

        self.assertIn('acceptversions', params)

    def test_logging(self):
        client = cwt.WPSClient('http://idontexist/wps', log=True, log_file='./wps.log')

    @mock.patch('requests.Session.request') 
    def test_csrf_cookie_pass_through(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        mock_request.return_value.cookies = {'csrftoken': 'token'}

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        client.get_capabilities()

        client.get_capabilities(refresh=True)

        args = mock_request.call_args_list[1]

        self.assertIn('headers', args[1])
        self.assertIn('X-CSRFToken', args[1]['headers'])

    @mock.patch('requests.Session.request') 
    def test_csrf_cookie(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        mock_request.return_value.cookies = {'csrftoken': 'token'}

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_invalid_status_code(self, mock_request):
        mock_request.return_value.status_code = 403

        mock_request.return_value.reason = 'Forbidden'

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_requests_exception(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        mock_request.side_effect = requests.RequestException(response=mock.MagicMock(status_code=400, reason='Not Found'))

        with self.assertRaises(cwt.WPSError):
            client.get_capabilities()

    @mock.patch('requests.Session.request') 
    def test_api_key(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps', api_key='api_key_7')

        process = cwt.Process.from_identifier('CDAT.subset')

        response = client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

    @mock.patch('requests.Session.request') 
    def test_execute_failed(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute_failed.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(Exception):
            client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

    @mock.patch('requests.Session.request') 
    def test_execute_no_inputs(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        client.execute(process, None, cwt.Domain([cwt.Dimension('time', 0, 365)]))

        self.assertIsNotNone(process.response)
        
    @mock.patch('requests.Session.request') 
    def test_execute_get(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]), method='GET')

        self.assertIsNotNone(process.response)
        
    @mock.patch('requests.Session.request') 
    def test_execute_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.WPSError):
            client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]), method='TEST')

    @mock.patch('requests.Session.request') 
    def test_execute(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.execute.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        client.execute(process, [cwt.Variable('file:///test.nc', 'tas')], cwt.Domain([cwt.Dimension('time', 0, 365)]))

        self.assertIsNotNone(process.response)

    def test_prepare_data_inputs(self):
        variable = cwt.Variable('file:///test.nc', 'tas', name='v0')

        domain = cwt.Domain([
            cwt.Dimension('time', 0, 365),
        ], name='d0')

        process = cwt.Process('CDAT.subset', name='subset')

        client = cwt.WPSClient('http://idontexist/wps')

        data_inputs = client.prepare_data_inputs(process, [variable], domain)

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

        mock_request.return_value.text = self.process_descriptions.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        description = client.describe_process(process, method='POST')

        self.assertEqual(len(description.ProcessDescription), 1)

        process_description = description.ProcessDescription[0]

        self.assertEqual(len(process_description.DataInputs.Input), 3)
        self.assertEqual(len(process_description.ProcessOutputs.Output), 1)

    @mock.patch('requests.Session.request') 
    def test_describe_process_invalid_method(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.WPSError):
            description = client.describe_process(process, method='TEST')

    @mock.patch('requests.Session.request') 
    def test_describe_process(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.process_descriptions.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = cwt.Process.from_identifier('CDAT.subset')

        description = client.describe_process(process)

        self.assertEqual(len(description.ProcessDescription), 1)

        process_description = description.ProcessDescription[0]

        self.assertEqual(len(process_description.DataInputs.Input), 3)
        self.assertEqual(len(process_description.ProcessOutputs.Output), 1)

    @mock.patch('requests.Session.request') 
    def test_get_process_indexerror(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        client.processes = mock.MagicMock()

        client.processes.return_value = []

        with self.assertRaises(cwt.WPSError):
            process = client.get_process('CDAT.subset')

    @mock.patch('requests.Session.request') 
    def test_get_process(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        process = client.get_process('CDAT.subset')

        self.assertIsNotNone(process)
        self.assertEqual(process.identifier, 'CDAT.subset')

    @mock.patch('requests.Session.request') 
    def test_processes_pattern(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        processes = client.processes('CDAT.')

        self.assertEqual(len(processes), 2)
        self.assertEqual([x.identifier for x in processes], ['CDAT.subset', 'CDAT.regrid'])

    @mock.patch('requests.Session.request') 
    def test_processes(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        processes = client.processes()

        self.assertEqual(len(processes), 3)
        self.assertEqual([x.identifier for x in processes], ['CDAT.subset', 'CDAT.regrid', 'EDAS.max'])

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_post(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        capabilities = client.get_capabilities(method='POST')

        self.assertIsNotNone(capabilities)

    @mock.patch('requests.Session.request') 
    def test_get_capabilities_get(self, mock_request):
        mock_request.return_value.status_code = 200

        mock_request.return_value.text = self.capabilities.toxml(bds=bds)

        client = cwt.WPSClient('http://idontexist/wps')

        capabilities = client.get_capabilities()

        self.assertIsNotNone(capabilities)

if __name__ == '__main__':
    unittest.main()
