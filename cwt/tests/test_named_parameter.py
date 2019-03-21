""" NamedParameter Unittest. """

import unittest

import cwt


class TestNamedParameter(unittest.TestCase):
    """ NamedParameter Test Case. """

    def test_from_string(self):
        p = cwt.NamedParameter.from_string('axes', 'x|y')

        self.assertIsInstance(p.values, tuple)
        self.assertEqual(len(p.values), 2)
        self.assertEqual(p.values, ('x', 'y'))
