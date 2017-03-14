"""
Unittest for Dimension class.
"""

import unittest

from esgf import CRS
from esgf import Dimension
from esgf import ParameterError

class TestDimension(unittest.TestCase):

    def test_from_dict_float(self):
        d = Dimension.from_dict('lat', {'start': '1.45', 'end': '2.36', 'crs': 'values'})

        self.assertEqual(d.start, 1.45)
        self.assertEqual(d.end, 2.36)

    def test_from_dict_int(self):
        d = Dimension.from_dict('lat', {'start': '1', 'end': '2', 'crs': 'values'})

        self.assertEqual(d.start, 1)
        self.assertEqual(d.end, 2)

    def test_from_dict_missing_crs(self):
        with self.assertRaises(ParameterError):
            d = Dimension.from_dict('lat', {'start': 1})

    def test_from_dict_missing_start(self):
        with self.assertRaises(ParameterError):
            d = Dimension.from_dict('lat', {})

    def test_parameterize(self):
        data = {
                'start': 1,
                'end': 2,
                'crs': 'values',
                'step': 10
                }

        d = Dimension.from_dict('lat', data)

        self.assertDictContainsSubset(data, d.parameterize())

    def test_from_dict(self):
        data = {
                'start': 1,
                'end': 2,
                'crs': 'values',
                'step': 10
                }

        d = Dimension.from_dict('lat', data)

        self.assertEqual(d.name, 'lat')
        self.assertEqual(d.start, 1)
        self.assertEqual(d.end, 2)
        self.assertEqual(d.step, 10)

class TestCRS(unittest.TestCase):
    
    def test_custom(self):
        c = CRS('test')

        self.assertEqual(c.name, 'test')
