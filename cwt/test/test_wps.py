"""
WPS unittest.
"""

import os
import unittest

import cwt
import mock
from cwt.wps_lib import operations

class TestWPS(unittest.TestCase):
    """ WPS Test Case. """

    def setUp(self):
        self.wps = cwt.WPS('http://nohost/wps')

        test_path = lambda x: os.path.join(os.path.dirname(__file__), x)

        with open(test_path('data/get_capabilities_response.txt'), 'r') as infile:
            self.capabilities_data = infile.read()

        with open(test_path('data/describe_process_cdat_avg_response.txt'), 'r') as infile:
            self.describe_data = infile.read()

        with open(test_path('data/execute_cdat_avg_response.txt'), 'r') as infile:
            self.execute_data = infile.read()
        
        self.data_inputs = '[variable=[{"uri": "file:///data/tas_6h.nc", "id": "tas|tas1"}];domain=[{"id": "d0"}];operation=[{"input": ["tas1"], "domain": "d0", "name": "CDAT.avg", "result": "avg"}]]'

    def test_combine_inputs(self):
        inputs = [cwt.Variable('file:///tas.nc', 'tas{}'.format(x)) for x in range(2)]

        avg = cwt.Process(type('Process', (object,), dict(identifier='CDAT.avg')))

        avg.set_inputs(inputs[0])

        with mock.patch.object(self.wps, '_WPS__request') as m:
            m.return_value = self.execute_data

            self.wps.execute(avg, inputs=[inputs[1]])

            self.assertIn('tas0|', m.call_args_list[0][1]['data'])
            self.assertIn('tas1|', m.call_args_list[0][1]['data'])

    def test_execute(self):
        with mock.patch.object(self.wps, '_WPS__request') as m:
            m.return_value = self.execute_data

            op = cwt.Process(type('Process', (object,), dict(identifier='CDAT.avg')))

            response = self.wps.execute(op)

            self.assertIsInstance(op.response, operations.ExecuteResponse)

    def test_prepare_data_inputs(self):
        proc = cwt.Process(type('Process', (object,), dict(identifier='CDAT.avg')), name='avg')

        tas = cwt.Variable('file:///data/tas_6h.nc', 'tas', name='tas1')

        d0 = cwt.Domain(name='d0')

        data_inputs = self.wps.prepare_data_inputs(proc, [tas], d0)
       
        self.assertEqual(self.data_inputs, data_inputs)

    def test_parse_data_inputs(self):
        operations, domains, variables = cwt.WPS.parse_data_inputs(self.data_inputs)

        self.assertEqual(len(operations), 1)
        self.assertEqual(len(domains), 1)
        self.assertEqual(len(variables), 1)

    def test_describe_process(self):
        with mock.patch.object(self.wps, '_WPS__request') as m:
            m.return_value = self.describe_data

            description = self.wps.describe('CDAT.avg')

            self.assertIsNotNone(description)
            self.assertIsInstance(description, operations.DescribeProcessResponse)

    def test_get_process(self):
        with mock.patch.object(self.wps, '_WPS__request') as m:
            m.return_value = self.capabilities_data

            process = self.wps.get_process('CDAT.avg')

            self.assertIsNotNone(process)
            self.assertIsInstance(process, cwt.Process)

    def test_processes_with_capabilities(self):
        with mock.patch.object(self.wps, '_WPS__request') as m:
            m.return_value = self.capabilities_data

            processes = self.wps.processes()

            self.assertIsNotNone(processes)
            self.assertEqual(len(processes), 26)
            self.assertTrue(all(isinstance(x, cwt.Process) for x in processes))

    def test_processes(self):
        with self.assertRaises(cwt.WPSHTTPError):
            self.wps.processes()

    def test_capabilities(self):
        with self.assertRaises(cwt.WPSHTTPError):
            self.wps.capabilities

if __name__ == '__main__':
    unittest.main()
