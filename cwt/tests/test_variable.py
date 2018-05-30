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

        self.d0 = cwt.Domain([cwt.Dimension('time', 1980, 2000)], name='d0')

    def test_resolve_domains(self):
        var = cwt.Variable.from_dict(self.data)

        var.resolve_domains(dict(d0=self.d0))

        self.assertItemsEqual(var.domains, [self.d0])

    def test_parameterize(self):
        var = cwt.Variable('file:///tas.nc', 'tas', domains=[self.d0], mime_type='application/netcdf', name='tas1')

        self.assertDictContainsSubset(self.data, var.parameterize())

    def test_from_dict(self):
        var = cwt.Variable.from_dict(self.data)

        self.assertEqual(var.name, 'tas1')
        self.assertEqual(var.uri, 'file:///tas.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertIsInstance(var.domains, list)
        self.assertEqual(len(var.domains), 1)
        self.assertEqual(var.domains[0], 'd0')

if __name__ == '__main__':
    unittest.main()
