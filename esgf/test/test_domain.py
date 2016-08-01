""" Domain Unittest """

from unittest import TestCase

from esgf import Domain
from esgf import DomainError
from esgf import Dimension

class TestDomain(TestCase):
    """ Domain Test Case """

    def test_optional_init(self):
        """ Test optional init values. """
        # Check if dimensions is empty and name is auto-generated.
        domain = Domain()

        self.assertEqual(domain.dimensions, [])
        self.assertIsNotNone(domain.name)

        # Check if we pass name to parameter class.
        domain = Domain(name='test')

        self.assertEqual(domain.name, 'test')

    def test_add_parameter(self):
        """ Tests addding parameters. """
        # Test adding single parameter.
        longitude = Dimension(-180.0, 180.0, Dimension.values, name='longitude')

        single_dimension_domain = Domain()

        single_dimension_domain.add_dimension(longitude)

        self.assertEqual(len(single_dimension_domain.dimensions), 1)

    def test_parameterize(self):
        """ Tests parameterizing a domain. """
        # Tests parameterizing with two dimensions.
        longitude = Dimension(-180.0, 180.0, Dimension.values, name='longitude')
        time = Dimension(1980, 1982, Dimension.values, name='time')

        domain = Domain([longitude, time], name='glbl')

        expected = {
            'id': 'glbl',
            'longitude': {
                'crs': 'values',
                'start': '-180.0',
                'end': '180.0',
                'step': 1,
            },
            'time': {
                'crs': 'values',
                'start': '1980',
                'end': '1982',
                'step': 1,
            }
        }

        self.assertEqual(domain.parameterize(), expected)

        # Test for DomainError on improper number of dimensions.
        with self.assertRaises(DomainError) as context:
            domain = Domain(name='glbl')

            domain.parameterize()

        self.assertEqual(context.exception.message, 'Need atleast one dimension.')
