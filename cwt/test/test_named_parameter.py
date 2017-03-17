""" NamedParameter Unittest. """

from unittest import TestCase

from cwt import Domain
from cwt import Dimension
from cwt import NamedParameter

class TestNamedParameter(TestCase):
    """ NamedParameter Test Case. """

    def test_from_list(self):
        p = NamedParameter.from_list('axes', ['x', 'y'])

        self.assertIsInstance(p.values, list)
        self.assertEqual(len(p.values), 2)
        self.assertItemsEqual(p.values, ['x', 'y'])

    def test_from_string(self):
        p = NamedParameter.from_string('axes', 'x|y')

        self.assertIsInstance(p.values, list)
        self.assertEqual(len(p.values), 2)
        self.assertItemsEqual(p.values, ['x', 'y'])
