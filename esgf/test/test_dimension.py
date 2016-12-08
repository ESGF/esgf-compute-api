"""
Unittest for Dimension class.
"""

from unittest import TestCase

from StringIO import StringIO

from esgf import Dimension
from esgf import WPSAPIError

from mock import patch

class TestDimension(TestCase):
    """ Test Case for Dimension class. """

    def test_repr(self):
        """ Test repr value. """
        dim = Dimension("lat", 0, 10, Dimension.values)

        self.assertEqual(repr(dim), "Dimension(name='lat', start=0, end=10, step=1, "
                         "crs=CRS(name='values'))")

    def test_str(self):
        """ Test str value. """
        dim = Dimension("lat", 0, 10, Dimension.values)

        self.assertEqual(str(dim), "name=lat start=0 end=10 step=1 crs=values")

    def test_from_dict(self):
        """ Create Dimension from dict representation. """

        indices = {"start": 1, "end": 2, "step": 2, "crs": "indices"}
        values = {"start": 1980, "end": 1982, "step": 10, "crs": "values"}
        string_values = {"start": "1980",
                         "end": "1982",
                         "step": 10,
                         "crs": "values"}
        missing_start = {"end": 1982, "crs": "values"}
        missing_step = {"start": 1980, "end": 1982, "crs": "values"}
        missing_crs = {"start": 1980, "end": 1982}

        dim = Dimension.from_dict('time', indices)

        self.assertEqual(dim.start, 1)
        self.assertEqual(dim.end, 2)
        self.assertEqual(dim.step, 2)
        self.assertEqual(dim.crs, Dimension.indices)

        dim = Dimension.from_dict('time', values)

        self.assertEqual(dim.start, 1980)
        self.assertEqual(dim.end, 1982)
        self.assertEqual(dim.step, 10)
        self.assertEqual(dim.crs, Dimension.values)

        dim = Dimension.from_dict('time', string_values)

        self.assertEqual(dim.start, 1980)
        self.assertEqual(dim.end, 1982)
        self.assertEqual(dim.step, 10)
        self.assertEqual(dim.crs, Dimension.values)

        with self.assertRaises(WPSAPIError) as ctx:
            dim = Dimension.from_dict('time', missing_start)

        dim = Dimension.from_dict('time', missing_step)

        self.assertEqual(dim.start, 1980)
        self.assertEqual(dim.end, 1982)
        self.assertEqual(dim.step, 1)
        self.assertEqual(dim.crs, Dimension.values)

        with self.assertRaises(WPSAPIError) as ctx:
            dim = Dimension.from_dict('time', missing_crs)

        self.assertEqual(ctx.exception.message,
                         'Must provide a CRS value.')

    @patch('esgf.parameter.uuid')
    def test_optional_init(self, mock_uuid4):
        """ Testing optional arguments. """
        mock_uuid4.return_value = 'Unique'

        dim = Dimension("dim", 1, 2, Dimension.indices)

        self.assertEqual(dim.step, 1)
        self.assertIsNotNone(dim.name)

        dim = Dimension("mydim", 1, None, Dimension.indices)

        self.assertEqual(dim.end, None)

        dim = Dimension("myotherdim", 1, 2, Dimension.indices, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension("longitude", 1, 2, Dimension.indices)

        self.assertEqual(dim.name, 'longitude')

    def test_indices(self):
        """ Testing creating from indices. """
        dim = Dimension("adim", 1, 2, Dimension.indices)

        self.assertEqual(dim.start, 1)
        self.assertEqual(dim.end, 2)
        self.assertEqual(dim.crs, Dimension.indices)

        dim = Dimension("somedim", '1', '2', Dimension.indices)

        self.assertEqual(dim.start, '1')
        self.assertEqual(dim.end, '2')

    def test_values(self):
        """ Testing creating from values. """
        dim = Dimension("adim", -180, 180, Dimension.values)

        self.assertEqual(dim.start, -180)
        self.assertEqual(dim.end, 180)
        self.assertEqual(dim.crs, Dimension.values)

        dim = Dimension("another_dim", -180.0, 180.0, Dimension.values)

        self.assertEqual(dim.start, -180.0)
        self.assertEqual(dim.end, 180.0)

        dim = Dimension("myotherdim", '-180.0', '180.0', Dimension.values)

        self.assertEqual(dim.start, '-180.0')
        self.assertEqual(dim.end, '180.0')

    def test_single_index(self):
        """ Testing creating from single index. """
        dim = Dimension.from_single_index("mydim", 1)

        self.assertEqual(dim.start, 1)
        self.assertEqual(dim.end, 1)
        self.assertEqual(dim.crs, Dimension.indices)
        self.assertEqual(dim.step, 1)
        self.assertIsNotNone(dim.name)

        dim = Dimension.from_single_index("somedim", 1, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension.from_single_index('longitude', 1)

        self.assertEqual(dim.name, 'longitude')

    def test_single_value(self):
        """ Testing creating from single value. """
        dim = Dimension.from_single_value("mydimension", -180)

        self.assertEqual(dim.start, -180)
        self.assertEqual(dim.end, -180)
        self.assertEqual(dim.crs, Dimension.values)
        self.assertEqual(dim.step, 1)
        self.assertIsNotNone(dim.name)

        dim = Dimension.from_single_value("somedim", -180, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension.from_single_value("longitude", -180)

        self.assertEqual(dim.name, 'longitude')

    def test_parameterize(self):
        """ Testing parameterization. """
        dim = Dimension("longitude", 1, 2, Dimension.values, step=1)

        param = dim.parameterize()

        self.assertEqual(param, \
                         {'start': 1, 'step': 1, 'end': 2, 'crs': 'values'})
