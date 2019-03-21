"""
WPS client unit tests
"""

import unittest

import mock

import cwt


class TestWPSClient(unittest.TestCase):

    def setUp(self):
        self.client = cwt.WPSClient('https://0.0.0.0:10000/wps')

        # Mock owslib.WebProcessingService
        self.client.client = mock.MagicMock()

        subset = mock.MagicMock()
        type(subset).identifier = mock.PropertyMock(return_value='CDAT.subset')
        type(subset).title = mock.PropertyMock(return_value='CDAT.subset')
        type(subset).processVersion = mock.PropertyMock(return_value='1.0.0')

        metrics = mock.MagicMock()
        type(metrics).identifier = mock.PropertyMock(
            return_value='CDAT.metrics')
        type(metrics).title = mock.PropertyMock(return_value='CDAT.metrics')
        type(metrics).processVersion = mock.PropertyMock(return_value='1.0.0')

        type(self.client.client).processes = mock.PropertyMock(return_value=[
            subset,
            metrics,
        ])

        self.process = cwt.Process.from_dict({
            'name': 'CDAT.subset',
            'input': [],
            'domain': None,
            'result': 'p0',
        })

        self.domain = cwt.Domain(time=(0, 365), name='d0')

        self.variable = cwt.Variable('file:///test.nc', 'tas', name='v0')

    def test_processes_filter_error(self):
        with self.assertRaises(cwt.CWTError):
            self.client.processes(r'*.\.aggregate')

    def test_processes_filter(self):
        processes = self.client.processes(r'.*\.subset')

        self.assertEqual(len(processes), 1)

        process = processes[0]

        self.client.client.getcapabilities.assert_called()

        self.assertEqual(process.identifier, 'CDAT.subset')
        self.assertEqual(process.title, 'CDAT.subset')
        self.assertEqual(process.process_version, '1.0.0')

    def test_processes(self):
        processes = self.client.processes()

        self.assertEqual(len(processes), 2)

    def test_execute_no_domain(self):
        with mock.patch.object(self.client, 'prepare_data_inputs') as mock_prepare:
            self.client.execute(self.process, [self.variable])
            mock_prepare.assert_called_with(
                self.process, [self.variable], None)

        self.assertIsNone(self.process.domain)

    def test_execute_no_inputs(self):
        with mock.patch.object(self.client, 'prepare_data_inputs') as mock_prepare:
            self.client.execute(self.process, domain=self.domain)

            mock_prepare.assert_called_with(self.process, [], self.domain)

        self.assertEqual(self.process.inputs, [])

    def test_execute_exception(self):
        self.client.client.execute.side_effect = Exception()

        with self.assertRaises(cwt.WPSClientError):
            self.client.execute(self.process)

    def test_execute(self):
        with mock.patch.object(self.client, 'prepare_data_inputs', return_value='data_inputs'):
            self.client.execute(self.process, [self.variable], self.domain)

        self.client.client.execute.assert_called_with(
            self.process.identifier, 'data_inputs')

        self.assertEqual(
            self.client.client.execute.return_value,
            self.process.context)

    def test_prepare_data_inputs(self):
        data_inputs = self.client.prepare_data_inputs(
            self.process, [self.variable], self.domain, axes='lats')

        self.assertEqual(len(data_inputs), 3)

        self.assertEqual(data_inputs[0][0], 'variable')
        self.assertIn(self.variable.name, data_inputs[0][1].value)

        self.assertEqual(data_inputs[1][0], 'domain')
        self.assertIn(self.domain.name, data_inputs[1][1].value)

        self.assertEqual(data_inputs[2][0], 'operation')
        self.assertIn(self.process.name, data_inputs[2][1].value)

    def test_parse_data_inputs(self):
        variable = '{"id": "tas|tas", "uri": "file:///test.nc", "result": "v0"}'

        domain = '{"id": "test", "time": {"start": 0, "end": 365, "step": 1, "crs": "values"}}'

        operation = '{"name": "CDAT.subset", "input": ["tas"], "domain": "test", "result": "subset"}'

        data_inputs = '[variable=[{}];domain=[{}];operation=[{}]]'.format(
            variable, domain, operation)

        operation, domain, variable = cwt.WPSClient.parse_data_inputs(
            data_inputs)

        self.assertEqual(len(operation), 1)
        self.assertEqual(len(domain), 1)
        self.assertEqual(len(variable), 1)

        self.assertIsInstance(operation[0], cwt.Process)
        self.assertIsInstance(domain[0], cwt.Domain)
        self.assertIsInstance(variable[0], cwt.Variable)

    def test_describe_process(self):
        self.process.inputs = [self.variable]

        self.process.domain = self.domain

        self.process.add_parameters(axes=['time'])

        new_process = self.client.describe_process(self.process)

        self.assertNotEqual(self.process, new_process)

        self.assertEqual(new_process.inputs, [self.variable])
        self.assertEqual(new_process.domain, self.domain)
        self.assertEqual(new_process.parameters, self.process.parameters)

    def test_get_capabilities(self):
        self.client.get_capabilities()

        self.client.client.getcapabilities.assert_called()
