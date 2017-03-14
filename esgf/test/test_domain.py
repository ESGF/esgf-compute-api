""" Domain Unittest """

from unittest import TestCase

from esgf import Mask
from esgf import Domain
from esgf import Dimension
from esgf import ParameterError

MASK = Mask('clt.nc', 'clt', 'var_data<0.5')

LAT = Dimension('lat', 0, 90)
LON = Dimension('lon', 0, 180)

class TestDomain(TestCase):
    """ Domain Test Case """

    def test_from_dict_missing_name(self):
        with self.assertRaises(ParameterError):
            d = Domain.from_dict({})

    def test_from_dict(self):
        d = Domain.from_dict({
            'id': 'test',
            'mask': MASK.parameterize(),
            'lon': {
                'start': 0,
                'crs': 'values',
                }
            })

        self.assertEqual(d.name, 'test')
        self.assertIsInstance(d.mask, Mask)
        self.assertIsInstance(d.dimensions, list)
        self.assertEqual(len(d.dimensions), 1)
        self.assertIsInstance(d.dimensions[0], Dimension)

    def test_parameterize(self):
        d = Domain([LAT, LON], MASK, 'test')

        data = d.parameterize()

        self.assertEqual(data['id'], 'test')
        self.assertItemsEqual(data.keys(), ('lat', 'lon', 'mask', 'id'))
