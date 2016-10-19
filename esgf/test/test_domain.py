""" Domain Unittest """

from unittest import TestCase

from esgf import WPSAPIError
from esgf import Mask
from esgf import Domain
from esgf import Dimension

class TestDomain(TestCase):
    """ Domain Test Case """

    def test_repr(self):
        """ Test repr value. """
        domain = Domain([], None, 'd0')

        self.assertEqual(repr(domain),
                         "Domain(dimensions=[], mask=None, name='d0')")
    
    def test_str(self):
        """ Test str value. """
        domain = Domain([], None, 'd0')

        self.assertEqual(str(domain),
                         "dimensions=[] mask=None name=d0")

    def test_from_dict(self):
        """ Create domain from dict representation. """
        single_dim = {"id": "d0",
                      "time": {"start": 1980, "end": 1982, "crs": "values"}}
        multiple_dim = {"id": "d0",
                        "time": {"start": 1980, "end": 1982, "crs": "values"},
                        "longitude": {"start": 1, "end": 2, "crs": "indices"}}
        mask = {"id": "d0",
                "time": {"start": 1980, "end": 1982, "crs": "values"},
                "mask": {"uri": "/test.nc", "id": "tas", "operation": "test_op"}}
        missing_id = {"time": {"start": 1980, "end": 1982, "crs": "values"}}
        missing_dim = {"id": "d0"}

        domain = Domain.from_dict(single_dim)

        self.assertEqual(domain.name, 'd0')
        self.assertIsNone(domain.mask)
        self.assertIsNotNone(domain.dimensions)
        self.assertEqual(len(domain.dimensions), 1)

        domain = Domain.from_dict(multiple_dim)

        self.assertEqual(domain.name, 'd0')
        self.assertIsNone(domain.mask)
        self.assertIsNotNone(domain.dimensions)
        self.assertEqual(len(domain.dimensions), 2)

        domain = Domain.from_dict(mask)

        self.assertEqual(domain.name, 'd0')
        self.assertIsNotNone(domain.mask)
        self.assertIsNotNone(domain.dimensions)
        self.assertEqual(len(domain.dimensions), 1)

        with self.assertRaises(WPSAPIError) as ctx:
            domain = Domain.from_dict(missing_id)

        self.assertEqual(ctx.exception.message,
                         'Domain must provide an id.')

    def test_mask(self):
        """ Pass domain a mask and parameterize. """
        time = Dimension(1920, 1930, Dimension.values, name='time')

        mask = Mask('file://test.nc', 'ta', 'var_data>mask_data', name='mask0')

        domain = Domain([time], mask=mask, name='d0')

        expected = {
            'id': 'd0',
            'time': {
                'crs': 'values',
                'start': 1920,
                'end': 1930,
                'step': 1
            },
            'mask': {
                'uri': 'file://test.nc',
                'id': 'ta|mask0',
                'operation': 'var_data>mask_data'
            }
        }

        self.assertEqual(domain.parameterize(), expected)

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
                'start': -180.0,
                'end': 180.0,
                'step': 1,
            },
            'time': {
                'crs': 'values',
                'start': 1980,
                'end': 1982,
                'step': 1,
            }
        }

        self.assertEqual(domain.parameterize(), expected)
