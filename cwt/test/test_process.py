"""
Process Unittest.
"""

import unittest

import cwt

class TestProcess(unittest.TestCase):
    """ Process Test Case. """

    def setUp(self):
        self.parameters = [cwt.NamedParameter(x, 'v1', 'v2') for x in ('bins', 'axes')]

        self.inputs = [cwt.Variable('path', 'tas', name='tas{}'.format(x))
                       for x in range(4)]

        self.process = cwt.Process(type('x', (object,), dict(identifier='test')), name='test')

    def test_from_dict(self):
        data = {
            'name': 'test',
            'result': 'avg',
            'input': ['tas0', 'tas2'],
            'axes': 'v1|v2'
        }

        inputs = dict((x.name, x) for x in self.inputs)

        proc = cwt.Process.from_dict(data, inputs)

        self.assertEqual(proc.name, 'avg')
        self.assertItemsEqual(proc.inputs, self.inputs[::2])
        self.assertEqual(len(proc.parameters), 1)
        self.assertEqual(proc.parameters[0], self.parameters[1])

    def test_parameters(self):
        self.process.parameters = self.parameters

        self.assertItemsEqual(self.process.parameters, self.parameters)

    def test_parameterize(self):
        self.process.inputs = self.inputs

        self.process.parameters = self.parameters

        data = self.process.parameterize()

        expected = {
            'input': ['tas0', 'tas1', 'tas2', 'tas3'],
            'name': 'test',
            'result': 'test',
            'axes': 'v1|v2',
            'bins': 'v1|v2',
        }

        self.assertDictContainsSubset(data, expected)

    def test_update_status_no_response(self):
        with self.assertRaises(cwt.ProcessError):
            self.process.update_status()

    def test_bad_property(self):
        with self.assertRaises(AttributeError):
            self.process.doesnt_exist

if __name__ == '__main__':
    unittest.main()
