"""
Unittest for Dimension class.
"""

import unittest

import cwt

class TestDimension(unittest.TestCase):

    def test_parameterize(self):
        expected = {'start': 0, 'end': 90, 'crs': 'values', 'step': 1}

        dim = cwt.Dimension('lat', 0, 90)

        self.assertEqual(dim.parameterize(), expected)

    def test_from_single_value(self):
        dim = cwt.Dimension.from_single_value('lat', 1000)

        self.assertEqual(dim.start, 1000)
        self.assertEqual(dim.end, 1000)
        self.assertEqual(dim.crs, cwt.CRS('values'))


    def test_from_single_index(self):
        dim = cwt.Dimension.from_single_index('lat', 1000)

        self.assertEqual(dim.start, 1000)
        self.assertEqual(dim.end, 1000)
        self.assertEqual(dim.crs, cwt.CRS('indices'))

    def test_from_dict_missing_crs(self):
        data = { 'start': 0 }

        with self.assertRaises(cwt.ParameterError):
            cwt.Dimension.from_dict(data, 'lat')

    def test_from_dict_missing_start(self):
        data = { }

        with self.assertRaises(cwt.ParameterError):
            cwt.Dimension.from_dict(data, 'lat')

    def test_from_dict(self):
        data = {
                'start': 0,
                'end': 90,
                'crs': 'values',
                'step': 2,
               }

        dim = cwt.Dimension.from_dict(data, 'lat')

        self.assertEqual(dim.name, 'lat')
        self.assertEqual(dim.start, 0)
        self.assertEqual(dim.end, 90)
        self.assertEqual(dim.crs, cwt.CRS('values'))
        self.assertEqual(dim.step, 2)

class TestCRS(unittest.TestCase):

    def test_equal(self):
        crs1 = cwt.CRS('test')

        crs2 = cwt.CRS('test')

        self.assertTrue(crs1 == crs2)

if __name__ == '__main__':
    unittest.main()
