""" NamedParameter Unittest. """

from unittest import TestCase

from esgf import NamedParameter

class TestNamedParameter(TestCase):
    """ NamedParameter Test Case. """

    def test_optional_init(self):
        """ Tests optional init values. """
        named = NamedParameter('axis')

        self.assertEqual(named.values, [])

        named = NamedParameter('axis', 'x', 'y')

        self.assertEqual(named.values, ['x', 'y'])

    def test_parameterize(self):
        """ Test parameterizing NamedParameter for GET request. """
        named = NamedParameter('axis', 'x', 'y')

        self.assertEqual(named.parameterize(), 'x|y')
