"""
Unittest for utils.
"""

from unittest import TestCase

from esgf import utils

class TestUtils(TestCase):
    """ Test Case for utils. """

    def test_int_or_float(self):
        """ Test converting str to int or float. """
        self.assertEqual(42, utils.int_or_float("42"))

        self.assertEqual(42.0, utils.int_or_float("42.0"))

        self.assertEqual(0.42, utils.int_or_float(".42"))

        self.assertEqual(42000.0, utils.int_or_float("42e3"))

        with self.assertRaises(ValueError):
            utils.int_or_float("number")
