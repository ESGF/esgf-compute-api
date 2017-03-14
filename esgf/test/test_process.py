"""
Process Unittest.
"""

import unittest

import esgf

class TestProcess(unittest.TestCase):
    """ Process Test Case. """

    def setUp(self):
        self.process = esgf.Process(type('x', (object,), dict(identifier='test')), name='test')

    def test_parameterize(self):
        data = self.process.parameterize()

        self.assertDictContainsSubset(data, {'input': None, 'name': 'test', 'result': 'test'})

    def test_update_status_no_response(self):
        with self.assertRaises(esgf.ProcessError):
            self.process.update_status()

    def test_bad_property(self):
        with self.assertRaises(AttributeError):
            self.process.doesnt_exist
