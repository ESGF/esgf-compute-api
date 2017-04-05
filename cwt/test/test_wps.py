"""
WPS unittest.
"""

import unittest

import cwt

class TestWPS(unittest.TestCase):
    """ WPS Test Case. """

    def test_parse_data_inputs(self):
        data_inputs = '[operation=[{"name":"test","input":["v1"],"result":"test"}];domain=[{"id":"d1","time":{"start":0,"end":1,"crs":"values"}}];variable=[{"id":"tas|v1","uri":"file:///"}]]'
        
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
