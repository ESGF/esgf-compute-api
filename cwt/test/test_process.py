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

    def test_resolve_inputs_missing(self):
        proc_sum = cwt.Process(type('Process', (object,), {}), name='sum')

        proc_avg = cwt.Process(type('Process', (object,), {}), name='avg')

        proc_sum.inputs = ['avg']

        with self.assertRaises(cwt.ProcessError):
            proc_sum.resolve_inputs({}, {})

    def test_resolve_inputs_circle(self):
        proc_sum = cwt.Process(type('Process', (object,), {}), name='sum')

        proc_avg = cwt.Process(type('Process', (object,), {}), name='avg')

        proc_sum.inputs = ['avg']

        proc_avg.inputs = ['sum']

        with self.assertRaises(cwt.ProcessError):
            proc_avg.resolve_inputs({}, {'sum': proc_sum, 'avg': proc_avg})

    def test_resolve_inputs(self):
        proc_sum = cwt.Process(type('Process', (object,), {}), name='sum')

        proc_sum.inputs = ['tas0']

        proc_avg = cwt.Process(type('Process', (object,), {}), name='avg')

        proc_avg.inputs = ['sum', 'tas1']

        inputs = dict((x.name, x) for x in self.inputs)

        operations = { 'sum' : proc_sum }

        proc_avg.resolve_inputs(inputs, operations)

        find_input = lambda x, y: [z for z in x if z.name == y][0]

        test_input_1 = find_input(proc_avg.inputs, 'tas1')

        self.assertIsInstance(test_input_1, cwt.Variable)

        test_input_2 = find_input(proc_avg.inputs, 'sum')

        self.assertIsInstance(test_input_2, cwt.Process)

        test_input_3 = find_input(proc_sum.inputs, 'tas0')

        self.assertIsInstance(test_input_3, cwt.Variable)

    def test_input_process(self):
        proc_avg = cwt.Process(type('Process', (object,), dict(identifier='avg')))

        proc_sum = cwt.Process(type('Process', (object,), dict(identifier='sum')))

        proc_sum.inputs = [proc_avg]

        data = proc_sum.parameterize()

        expected = {
                    'name': 'sum',
                    'input': [ proc_avg.name ],
                    'result': proc_sum.name
                   }

        self.assertEqual(data, expected)

    def test_from_dict(self):
        data = {
                'name': 'test',
                'result': 'avg',
                'input': ['tas0', 'tas2'],
                'axes': 'v1|v2'
               }

        proc = cwt.Process.from_dict(data)

        self.assertEqual(proc.name, 'avg')
        self.assertItemsEqual(proc.inputs, ['tas0', 'tas2'])
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
