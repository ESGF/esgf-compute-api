"""
Mask Unittest.
"""

import unittest

import cwt


class TestMask(unittest.TestCase):
    """ Mask Test Case. """

    def parameterize(self):
        expected = {
            "uri": "file:///test.nc",
            "id": "tas|tas1",
            "operation": "var_data>0.5",
        }

        mask = cwt.Mask("file:///test.nc", "tas", "var_data>0.5", "tas1")

        self.assertDictContainsSubset(expected, mask.parameterize())

    def test_from_dict(self):
        data = {
            "uri": "file:///test.nc",
            "id": "tas|tas1",
            "operation": "var_data>0.5",
        }

        mask = cwt.Mask.from_dict(data)

        self.assertEqual(mask.uri, "file:///test.nc")
        self.assertEqual(mask.var_name, "tas")
        self.assertEqual(mask.operation, "var_data>0.5")


if __name__ == "__main__":
    unittest.main()
