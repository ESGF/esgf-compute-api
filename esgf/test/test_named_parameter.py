""" NamedParameter Unittest. """

from unittest import TestCase

from esgf import Domain
from esgf import Dimension
from esgf import NamedParameter

class TestNamedParameter(TestCase):
    """ NamedParameter Test Case. """

    def test_repr(self):
        """ Test repr value. """
        axes = NamedParameter('axes', 'x', 'y')

        self.assertEqual(repr(axes),
                         """NamedParameter('axes', ['x', 'y'])""")

    def test_str(self):
        """ Test str value. """
        axes = NamedParameter('axes', 'x', 'y')

        self.assertEqual(str(axes),
                         """axes ['x', 'y']""")

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

    def test_parameter(self):
        """ Test passing parameter in constructor. """
        time = Dimension.from_single_index(2, name='time')

        domain = Domain([time], name='d0')

        named = NamedParameter('domain', domain)

        self.assertEqual(named.parameterize(), 'd0')
