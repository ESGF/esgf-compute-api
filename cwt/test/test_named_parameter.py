""" NamedParameter Unittest. """

import unittest

import cwt

class TestNamedParameter(unittest.TestCase):
    """ NamedParameter Test Case. """

    def test_bad_type(self):
        o = type('X', (object,), dict(test=1))

        p = cwt.NamedParameter('x', o)

        with self.assertRaises(cwt.ParameterError):
            p.parameterize()

    def test_from_string(self):
        p = cwt.NamedParameter.from_string('axes', 'x|y')

        self.assertIsInstance(p.values, list)
        self.assertEqual(len(p.values), 2)
        self.assertItemsEqual(p.values, ['x', 'y'])

if __name__ == '__main__':
    unittest.main()
