""" Variable Unittest. """

import unittest

import cwt

class TestVariable(unittest.TestCase):
    """ Variable Test Case. """

    def setUp(self):
        self.data = {
            'uri': 'file:///tas.nc',
            'id': 'tas|tas1',
            'domain': 'd0',
            'mime_type': 'application/netcdf',
        }

        self.d0 = cwt.Domain(time=(1980, 2000), name='d0')

    def test_to_dict(self):
        var = cwt.Variable('file:///tas.nc', 'tas', domain=self.d0, mime_type='application/netcdf', name='tas1')

        self.assertDictContainsSubset(self.data, var.to_dict())

    def test_from_dict(self):
        var = cwt.Variable.from_dict(self.data)

        self.assertEqual(var.name, 'tas1')
        self.assertEqual(var.uri, 'file:///tas.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertEqual(var.domain, 'd0')
