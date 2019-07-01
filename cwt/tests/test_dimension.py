"""
Unittest for Dimension class.
"""

import mock
import unittest

import cwt
from cwt.dimension import int_or_float
from cwt.dimension import get_crs_value


class TestDimension(unittest.TestCase):

    def setUp(self):
        self.dimension_dict = {
            'start': 0,
            'end': 365,
            'step': 4,
            'crs': 'values',
        }

        self.dimension = cwt.Dimension.from_dict(self.dimension_dict, 'time')

    def test_from_dict_missing_step(self):
        del self.dimension_dict['step']

        data = self.dimension.from_dict(self.dimension_dict, 'time')

        self.assertEqual(data.step, 1)

    def test_get_crs_value_unknown(self):
        with self.assertRaises(cwt.CWTError):
            get_crs_value(cwt.CRS('new'), 'data')

    @mock.patch('cwt.dimension.int_or_float')
    def test_get_crs_value(self, mock_conv):
        mock_conv.side_effect = [2, 4]

        value = get_crs_value(cwt.TIMESTAMPS, '1980-01-01')

        self.assertEqual(value, '1980-01-01')

        value = get_crs_value(cwt.VALUES, 2)

        self.assertEqual(value, 2)

        value = get_crs_value(cwt.INDICES, 4)

        self.assertEqual(value, 4)

        self.assertEqual(mock_conv.call_count, 1)

    def test_int_or_float_not_supported(self):
        with self.assertRaises(cwt.CWTError):
            int_or_float('hello')

    def test_int_or_float_float(self):
        data = int_or_float('3.0')

        self.assertIsInstance(data, float)

    def test_int_or_float_int(self):
        data = int_or_float('3')

        self.assertIsInstance(data, int)

    def test_int_or_float_correct_format(self):
        data = int_or_float(3)

        self.assertIsInstance(data, int)
        self.assertEqual(data, 3)

        data = int_or_float(3.2)

        self.assertIsInstance(data, float)
        self.assertEqual(data, 3.2)

    def test_from_single_index(self):
        dimension = cwt.Dimension.from_single_index('time', 365, step=4)

        self.assertEqual(dimension.name, 'time')
        self.assertEqual(dimension.start, 365)
        self.assertEqual(dimension.end, 365)
        self.assertEqual(dimension.step, 4)
        self.assertEqual(dimension.crs, cwt.INDICES)

    def test_from_single_value(self):
        dimension = cwt.Dimension.from_single_value('time', 365, step=4)

        self.assertEqual(dimension.name, 'time')
        self.assertEqual(dimension.start, 365)
        self.assertEqual(dimension.end, 365)
        self.assertEqual(dimension.step, 4)
        self.assertEqual(dimension.crs, cwt.VALUES)

    def test_from_dict_invalid_step_format(self):
        self.dimension_dict['step'] = 'hello world'

        with self.assertRaises(cwt.CWTError):
            cwt.Dimension.from_dict(self.dimension_dict, 'time')

    def test_from_dict_missing_req(self):
        del self.dimension_dict['start']

        with self.assertRaises(cwt.MissingRequiredKeyError):
            cwt.Dimension.from_dict(self.dimension_dict, 'time')

    def test_from_dict(self):
        dimension = cwt.Dimension.from_dict(self.dimension_dict, 'time')

        self.assertDictContainsSubset(self.dimension_dict, dimension.to_dict())

    def test_to_dict(self):
        dimension = cwt.Dimension('time', 0, 365, step=4)

        self.assertDictContainsSubset(self.dimension_dict, dimension.to_dict())


class TestCRS(unittest.TestCase):

    def test_not_equal(self):
        crs1 = cwt.VALUES

        crs2 = cwt.CRS('indices')

        self.assertNotEqual(crs1, crs2)

    def test_equal(self):
        crs1 = cwt.VALUES

        crs2 = cwt.CRS('values')

        self.assertEqual(crs1, crs2)
