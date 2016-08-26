"""
Mask Unittest.
"""

from unittest import TestCase

from esgf import Mask

class TestMask(TestCase):
    """ Mask Test Case. """

    def test_from_dict(self):
        """ Create Mask from dict representation. """
        valid = {"uri": "/test.nc", "id": "tas|m0", "operation": "test_op"}

        mask = Mask.from_dict(valid)

        self.assertEqual(mask.uri, '/test.nc')
        self.assertEqual(mask.name, 'm0')
        self.assertEqual(mask.var_name, 'tas')
        self.assertEqual(mask.operation, 'test_op')

    # pylint: disable=protected-access
    def test_mask(self):
        """ Check mask parameterization. """
        mask = Mask('file://test.nc', 'ta', 'var_data>mask_data')

        self.assertIsNotNone(mask._name)

        mask = Mask('file://test.nc', 'ta', 'var_data>mask_data', name='test')

        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|test',
            'operation': 'var_data>mask_data',
        }

        self.assertEqual(mask.parameterize(), expected)
