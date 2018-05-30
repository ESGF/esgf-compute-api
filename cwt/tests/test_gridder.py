"""
Gridder Unittest
"""

import unittest

import cwt

class TestGridder(unittest.TestCase):
    """ Gridder Test Case. """

    def test_parameterize(self):
        expected = { 'tool': 'regrid2', 'method': 'linear', 'grid': 'T85' }

        gridder = cwt.Gridder()

        self.assertDictContainsSubset(expected, gridder.parameterize())

    def test_from_dict(self):
        data = { 'tool': 'A', 'method': 'B', 'grid': 'NO' }

        gridder = cwt.Gridder.from_dict(data)

        self.assertEqual(gridder.tool, 'A')
        self.assertEqual(gridder.method, 'B')
        self.assertEqual(gridder.grid, 'NO')

if __name__ == '__main__':
    unittest.main()
