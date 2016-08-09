"""
Mask Unittest.
"""

from unittest import TestCase

from esgf import Mask

class TestMask(TestCase):
    """ Mask Test Case. """

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
