"""
Unittest for Dimension class.
"""

from unittest import TestCase

from StringIO import StringIO

from esgf import Dimension

from mock import patch

class TestDimension(TestCase):
    """ Test Case for Dimension class. """

    @patch('esgf.parameter.uuid4')
    def test_optional_init(self, mock_uuid4):
        """ Testing optional arguments. """
        mock_uuid4.return_value = 'Unique'

        dim = Dimension(1, 2, Dimension.indices)

        self.assertEqual(dim.step, 1)
        self.assertIsNotNone(dim.name)
        self.assertEqual(capture_str_stdout(dim), \
            'Dimension(1, 2, indices, step=1, name="Unique")')

        dim = Dimension(1, 2, Dimension.indices, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension(1, 2, Dimension.indices, name='longitude')

        self.assertEqual(dim.name, 'longitude')

    def test_indices(self):
        """ Testing creating from indices. """
        dim = Dimension(1, 2, Dimension.indices)

        self.assertEqual(dim.start, '1')
        self.assertEqual(dim.end, '2')
        self.assertEqual(dim.crs, Dimension.indices)

        dim = Dimension('1', '2', Dimension.indices)

        self.assertEqual(dim.start, '1')
        self.assertEqual(dim.end, '2')

    def test_values(self):
        """ Testing creating from values. """
        dim = Dimension(-180, 180, Dimension.values)

        self.assertEqual(dim.start, '-180')
        self.assertEqual(dim.end, '180')
        self.assertEqual(dim.crs, Dimension.values)

        dim = Dimension(-180.0, 180.0, Dimension.values)

        self.assertEqual(dim.start, '-180.0')
        self.assertEqual(dim.end, '180.0')

        dim = Dimension('-180.0', '180.0', Dimension.values)

        self.assertEqual(dim.start, '-180.0')
        self.assertEqual(dim.end, '180.0')

    def test_single_index(self):
        """ Testing creating from single index. """
        dim = Dimension.from_single_index(1)

        self.assertEqual(dim.start, '1')
        self.assertIsNone(dim.end)
        self.assertEqual(dim.crs, Dimension.indices)
        self.assertIsNone(dim.step)
        self.assertIsNotNone(dim.name)

        dim = Dimension.from_single_index(1, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension.from_single_index(1, name='longitude')

        self.assertEqual(dim.name, 'longitude')

        self.assertEqual(capture_str_stdout(dim), \
            'Dimension(1, None, indices, step=None, name="longitude")')

    def test_single_value(self):
        """ Testing creating from single value. """
        dim = Dimension.from_single_value(-180)

        self.assertEqual(dim.start, '-180')
        self.assertIsNone(dim.end)
        self.assertEqual(dim.crs, Dimension.values)
        self.assertIsNone(dim.step)
        self.assertIsNotNone(dim.name)

        dim = Dimension.from_single_index(-180, step=2)

        self.assertEqual(dim.step, 2)

        dim = Dimension.from_single_index(-180, name='longitude')

        self.assertEqual(dim.name, 'longitude')

    def test_parameterize(self):
        """ Testing parameterization. """
        dim = Dimension(1, 2, Dimension.values, step=1, name='longitude')

        param = dim.parameterize()

        self.assertEqual(param, \
                     {'start': '1', 'step': 1, 'end': '2', 'crs': 'values'})

    def test_str(self):
        """ Testing str. """
        dim = Dimension(1, 2, Dimension.values, step=2, name='longitude')

        self.assertEqual(capture_str_stdout(dim), \
             'Dimension(1, 2, values, step=2, name="longitude")')

def capture_str_stdout(obj):
    """ Helper method emulates printing to stdout. """
    output = StringIO()

    print >>output, obj

    return output.getvalue().replace('\n', '')
