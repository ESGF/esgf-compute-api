"""
WPS unittest.
"""

import unittest

import mock

import cwt

class TestWPS(unittest.TestCase):
    """ WPS Test Case. """

    def setUp(self):
        self.inputs = [cwt.Variable('file:///', 'tas{}'.format(x), name='tas{}'.format(x)) for x in range(4)]

        self.processes = [cwt.Process(type('Process', (object,), dict(identifier='test')), name='proc{}'.format(x)) for x in range(4)]

    def test_prepare_data_inputs_tree(self):
        wps = cwt.WPS('http://test')

        expected = '[variable=[{"uri": "file:///", "id": "tas0|tas0"}, {"uri": "file:///", "id": "tas1|tas1"}];domain=[];operation=[{"input": ["tas0", "proc1"], "name": "test", "result": "proc0"}, {"input": ["tas1"], "name": "test", "result": "proc1"}]]'

        mpatch1 = mock.patch.object(wps, '_WPS__request', return_value='hello')
        mpatch2 = mock.patch.object(wps, '_WPS__parse_response', return_value='goodbye')

        with mpatch1 as patch1, mpatch2 as patch2:
            p = self.processes[0]

            self.processes[1].inputs = [self.inputs[1]]
            
            wps.execute(p, [self.inputs[0], self.processes[1]], method='GET') 

            self.assertEqual(patch1.call_args[1]['params']['datainputs'], expected)

    def test_parse_data_inputs(self):
        data_inputs = ('[operation=[{"name":"test","input":["v1"],"result":'
        '"test"}];domain=[{"id":"d1","time":{"start":0,"end":1,"crs":"values"'
        '}}];variable=[{"id":"tas|v1","uri":"file:///"}]]')
        
        operation, domain, variable = cwt.WPS.parse_data_inputs(data_inputs)

        self.assertIsInstance(operation, list)
        self.assertEqual(len(operation), 1)
        self.assertIsInstance(operation[0], cwt.Process)

        self.assertIsInstance(domain, list)
        self.assertEqual(len(domain), 1)
        self.assertIsInstance(domain[0], cwt.Domain)

        self.assertIsInstance(variable, list)
        self.assertEqual(len(variable), 1)
        self.assertIsInstance(variable[0], cwt.Variable)

if __name__ == '__main__':
    unittest.main()
