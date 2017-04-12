"""
Process Unittest.
"""

import unittest

import cwt
import mock
from cwt.wps_lib.xml import XMLError

class TestProcess(unittest.TestCase):
    """ Process Test Case. """

    def setUp(self):
        self.avg = cwt.Process(type('Process', (object,), dict(identifier='CDAT.avg')), name='avg')

        self.sum = cwt.Process(type('Process', (object,), dict(identifier='CDAT.sum')), name='sum')

        self.tas = cwt.Variable('file:///tas.nc', 'tas', name='tas')

        self.clt = cwt.Variable('file:///clt.nc', 'clt', name='clt')

    @mock.patch.object(cwt.wps.requests, 'get')
    def test_update_status_malformed_execute_response(self, mock_get):
        # Mock the response object with text property
        mock_get.return_value = mock.Mock(text='</xml>')

        self.avg.response = type('Process', (object,), dict(status_location='http://doesnotexist'))

        with self.assertRaises(XMLError):
            self.avg.update_status()

    def test_update_status_location_does_not_exist(self):
        self.avg.response = type('Process', (object,), dict(status_location='http://doesnotexist'))

        with self.assertRaises(cwt.ProcessError):
            self.avg.update_status()

    def test_update_status(self):
        with self.assertRaises(cwt.ProcessError):
            self.avg.update_status()

    def test_parameterize(self):
        expected = {
                    'input': ['tas', 'sum'],
                    'axes': 'x|y', 
                    'name': 'CDAT.avg',
                    'result': 'avg'
                   }

        self.sum.inputs = [self.clt, self.tas]

        self.avg.inputs = [self.tas, self.sum]

        self.avg.parameters = [cwt.NamedParameter('axes', 'x', 'y')]

        self.assertDictContainsSubset(expected, self.avg.parameterize())

    def test_collect_input_processes(self):
        self.sum.inputs = [self.clt, self.tas]

        self.avg.inputs = [self.tas, self.sum]

        processes, inputs = self.avg.collect_input_processes()

        self.assertIsInstance(processes, list)
        self.assertEqual(len(processes), 1)
        self.assertEqual(processes[0], self.sum)

        self.assertIsInstance(inputs, list)
        self.assertEqual(len(inputs), 2)
        self.assertItemsEqual(inputs, [self.tas, self.clt])

    def test_resolve_inputs_missing(self):
        self.avg.inputs = ['tas']

        with self.assertRaises(cwt.ProcessError):
            self.avg.resolve_inputs(dict(), dict())

    def test_resolve_inputs_circular(self):
        self.avg.inputs = ['avg']

        with self.assertRaises(cwt.ProcessError):
            self.avg.resolve_inputs(dict(), dict(avg=self.avg))

    def test_resolve_inputs(self):
        self.avg.inputs = ['sum', 'tas']

        self.avg.resolve_inputs(dict(tas=self.tas), dict(sum=self.sum))

        self.assertIsInstance(self.avg.inputs, list)
        self.assertEqual(len(self.avg.inputs), 2)
        self.assertItemsEqual(self.avg.inputs, [self.sum, self.tas])

    def test_error(self):
        self.assertTrue(self.avg.error)

    def test_processing(self):
        with self.assertRaises(cwt.ProcessError):
            self.avg.processing

    def test_parameters_property(self):
        axes = cwt.NamedParameter('axes', 'x', 'y')

        self.avg.parameters = [axes]

        self.assertEqual(axes, self.avg.parameters[0])

    def test_identifier_property(self):
        self.assertEqual(self.avg.identifier, 'CDAT.avg')

    def test_missing_attribute(self):
        with self.assertRaises(AttributeError):
            self.avg.results

    def test_from_dict(self):
        data = {
                'result': 'avg1',
                'input': ['tas1'],
                'name': 'CDAT.avg',
                'axes': 'x|y',
               }

        proc = cwt.Process.from_dict(data)

        self.assertEqual(proc.name, 'avg1')
        self.assertIsInstance(proc.inputs, list)
        self.assertItemsEqual(proc.inputs, ['tas1'])
        self.assertIsInstance(proc.parameters, list)
        self.assertEqual(proc.identifier, 'CDAT.avg')

if __name__ == '__main__':
    unittest.main()
