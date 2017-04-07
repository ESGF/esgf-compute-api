"""
WPS unittest.
"""

import unittest

import mock

import cwt

class TestWPS(unittest.TestCase):
    """ WPS Test Case. """

    def setUp(self):
        self.sample_data_inputs = '[variable=[{"uri": "file:///", "id": "tas0|tas0"}, {"uri": "file:///", "id": "tas1|tas1"}];domain=[];operation=[{"input": ["tas0", "proc1"], "name": "test", "result": "proc0"}, {"input": ["tas1"], "name": "test", "result": "proc1"}]]'

        self.inputs = [cwt.Variable('file:///', 'tas{}'.format(x), name='tas{}'.format(x)) for x in range(4)]

        self.processes = [cwt.Process(type('Process', (object,), dict(identifier='test')), name='proc{}'.format(x)) for x in range(4)]

    def test_prepare_data_inputs_tree(self):
        wps = cwt.WPS('http://test')

        mpatch1 = mock.patch.object(wps, '_WPS__request', return_value='hello')
        mpatch2 = mock.patch.object(wps, '_WPS__parse_response', return_value='goodbye')

        with mpatch1 as patch1, mpatch2 as patch2:
            p = self.processes[0]

            self.processes[1].inputs = [self.inputs[1]]
            
            wps.execute(p, [self.inputs[0], self.processes[1]], method='GET') 

            self.assertEqual(patch1.call_args[1]['params']['datainputs'], self.sample_data_inputs)

    def test_parse_data_inputs(self):
        operation, domain, variable = cwt.WPS.parse_data_inputs(self.sample_data_inputs)

        self.assertIsInstance(operation, list)
        self.assertEqual(len(operation), 2)
        self.assertTrue(all([isinstance(x, cwt.Process) for x in operation]))

        self.assertIsInstance(domain, list)
        self.assertEqual(len(domain), 0)

        self.assertIsInstance(variable, list)
        self.assertEqual(len(variable), 2)
        self.assertTrue(all([isinstance(x, cwt.Variable) for x in variable]))

if __name__ == '__main__':
    unittest.main()
