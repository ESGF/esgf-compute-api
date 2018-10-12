"""
Process Unittest.
"""

import unittest

import mock
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

class TestProcess(unittest.TestCase):
    """ Process Test Case. """

    def setUp(self):
        process = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        started = wps.status_started('started', 10)

        output = wps.output_data('output', 'Output', '{"id": "tas|tas", "uri": "file:///test.nc"}')

        self.execute = wps.execute_response(process, started, '1.0.0', 'en-US', 'http://idontexist.com/wps', 'http://idontexist.com/status', [output])

        failed = wps.status_failed('error', '10', '1.0.0')

        self.execute_failed = wps.execute_response(process, failed, '1.0.0', 'en-US', 'http://idontexist.com/wps', 'http://idontexist.com/status', [output])

        self.binding = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

    def tearDown(self):
        bds.reset()

    @mock.patch('cwt.process.logger')
    def test_wait_duplicate_status(self, mock_logger):
        process = cwt.Process.from_identifier('CDAT.subset')

        type(process).processing = mock.PropertyMock(side_effect=[True, True, False])

        type(process).status = mock.PropertyMock(side_effect=['status 1',
                                                              'status 2',
                                                              'status 2',
                                                              'status 4'])

        type(process).succeeded = mock.PropertyMock(return_value=True)

        result = process.wait()

        self.assertTrue(result)

        self.assertEqual(mock_logger.info.call_count, 3)

    def test_wait_no_success(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        type(process).processing = mock.PropertyMock(side_effect=[True, True, False])

        type(process).status = mock.PropertyMock(side_effect=['status 1',
                                                              'status 2',
                                                              'status 3',
                                                              'status 4',
                                                              'status 5'])

        type(process).succeeded = mock.PropertyMock(return_value=False)

        result = process.wait()

        self.assertFalse(result)

    def test_wait(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        type(process).processing = mock.PropertyMock(side_effect=[True, True, False])

        type(process).status = mock.PropertyMock(side_effect=['status 1',
                                                              'status 2',
                                                              'status 3',
                                                              'status 4',
                                                              'status 5'])

        type(process).succeeded = mock.PropertyMock(return_value=True)

        result = process.wait()

        self.assertTrue(result)

    def test_parameterize(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.set_domain(cwt.Domain([
            cwt.Dimension('time', 0, 365),
        ]))

        process.add_parameters(test=['value1'])

        process.add_inputs(cwt.Variable('file:///test.nc', 'tas'))

        data = process.parameterize()

    def test_update_status(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        self.assertIsNone(process.update_status())

    def test_collect_input_processes(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process1 = cwt.Process.from_identifier('CDAT.regrid')

        process1.add_inputs(cwt.Variable('file:///test.nc', 'tas'))

        process.add_inputs(process1, cwt.Variable('file:///test1.nc', 'tas'))

        processes, variables = process.collect_input_processes()

        self.assertEqual(len(processes), 1)

        self.assertEqual(len(variables), 2)

    def test_resolve_inputs_missing(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.inputs = ['subset']

        with self.assertRaises(cwt.ProcessError):
            process.resolve_inputs({}, {})

    def test_resolve_inputs_circular(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.inputs = ['subset']

        with self.assertRaises(cwt.ProcessError):
            process.resolve_inputs({}, {'subset': process })

    def test_resolve_inputs(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.inputs = ['v0', 'subset']

        variables = {
            'v0': cwt.Variable('file:///v0.nc', 'tas'),
        }

        operations = {
            'subset': cwt.Process.from_identifier('CDAT.subset'),
        }

        process.resolve_inputs(variables, operations)

        self.assertIn(variables['v0'], process.inputs)

        self.assertIn(operations['subset'], process.inputs)

    def test_add_inputs(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.add_inputs(cwt.Variable('file:///test.nc', 'tas'))

        self.assertEqual(len(process.inputs), 1)

    def test_add_parameter_key_value(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.add_parameters(test=['value1'])

        self.assertEqual(len(process.parameters), 1)

    def test_add_parameter_invalid_argument_type(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.ProcessError):
            process.add_parameters(test='test')
        
    def test_add_parameter_invalid_type(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        with self.assertRaises(cwt.ProcessError):
            process.add_parameters('test')

    def test_add_parameter(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.add_parameters(cwt.NamedParameter('test', 'value1'))

        self.assertEqual(len(process.parameters), 1)

    def test_get_parameter_missing_required(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.parameters['test'] = cwt.NamedParameter('test', 'value1')

        with self.assertRaises(cwt.ProcessError):
            process.get_parameter('test2', True)

    def test_get_parameter_missing(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.parameters['test'] = cwt.NamedParameter('test', 'value1')

        self.assertIsNone(process.get_parameter('test2'))

    def test_get_parameter(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.parameters['test'] = cwt.NamedParameter('test', 'value1')

        param = process.get_parameter('test')

        self.assertEqual(param.name, 'test')

    def test_output_not_available(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        self.assertIsNone(process.output)

    def test_output(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        process.response = self.execute

        self.assertIsInstance(process.output, cwt.Variable)

    def test_processing(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        mock_client = mock.MagicMock()

        mock_client.http_request.return_value = self.execute.toxml(bds=bds)

        process.set_client(mock_client)

        process.response = self.execute

        self.assertTrue(process.processing)

    def test_from_dict(self):
        data = {
            'name': 'CDAT.subset',
            'result': 'subset',
            'input': ['v0'],
            'domain': 'd0',
            'gridder': {
                'grid': 'T21',
            }
        }

        process = cwt.Process.from_dict(data)

        self.assertEqual(process.identifier, 'CDAT.subset')
        self.assertEqual(process.inputs, ['v0'])
        self.assertEqual(process.domain, 'd0')


    def test_from_binding(self):
        process = cwt.Process.from_binding(self.binding)

        self.assertEqual(process.identifier, 'CDAT.subset')

    def test_from_identifier(self):
        process = cwt.Process.from_identifier('CDAT.subset')

        self.assertEqual(process.identifier, 'CDAT.subset')

if __name__ == '__main__':
    unittest.main()
