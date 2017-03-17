""" Variable Unittest. """

import json

from unittest import TestCase

from cwt import Domain
from cwt import Variable
from cwt import ParameterError

class TestVariable(TestCase):
    """ Variable Test Case. """

    def test_repr(self):
        """ Test repr value. """
        var = Variable('file:///test.nc', 'tas', name='v0',
                       mime_type='application/netcdf')

        self.assertEqual(repr(var), "Variable(name='v0', "
                         "uri='file:///test.nc', var_name='tas', "
                         "domains=None, mime_type='application/netcdf')")
        
    def test_mime_type(self):
        """ Tests mime_type. """
        output = {
            'uri': 'file:///test.nc',
            'mime_type': 'application/netcdf',
            'id': 'tas|v0',
        }

        var = Variable('file:///test.nc', 'tas', name='v0', mime_type='application/netcdf')

        self.assertEqual(var.parameterize(),
                         output)

    def test_from_dict(self):
        """ Test creating variable from dict representation. """
        single_domain = {'uri': '/test.nc', 'id': 'tas|v0', 'domain': 'd0'}
        multiple_domain = {'uri': '/test.nc', 'id': 'tas|v0',
                           'domain': ['d0', 'd1']}
        missing_uri = {'id': 'tas|v0', 'domain': 'd0'}
        missing_id = {'uri': '/test.nc', 'domain': 'd0'}
        missing_name = {'uri': '/test.nc', 'domain': 'd0', 'id': 'tas'}
        missing_domain = {'uri': '/test.nc', 'id': 'tas|v0'}

        var = Variable.from_dict(single_domain)

        self.assertEqual(var.uri, '/test.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertEqual(var.name, 'v0')
        self.assertEqual(var.domains, ['d0'])

        var = Variable.from_dict(multiple_domain)

        self.assertEqual(var.uri, '/test.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertEqual(var.name, 'v0')
        self.assertListEqual(var.domains, ['d0', 'd1'])

        with self.assertRaises(ParameterError) as ctx:
            var = Variable.from_dict(missing_uri)

        self.assertEqual(ctx.exception.message,
                         'Variable must provide a uri.')

        with self.assertRaises(ParameterError) as ctx:
            var = Variable.from_dict(missing_id)

        self.assertEqual(ctx.exception.message,
                         'Variable must provide an id.')

        with self.assertRaises(ParameterError) as ctx:
            var = Variable.from_dict(missing_name)

        self.assertEqual(ctx.exception.message,
                         'Variable id must contain a variable name and id.')

    def test_optional_init(self):
        """ Tests optional init. """
        var = Variable('file:///test.nc', 'clt')

        self.assertEqual(var.uri, 'file:///test.nc')
        self.assertEqual(var.var_name, 'clt')
        self.assertIsNone(var.domains)
        self.assertIsNotNone(var.name)
        self.assertIsNone(var.mime_type)

    def test_name(self):
        """ Providing name argument. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
        }

        var = Variable('file://test.nc', 'ta', name='v0')

        self.assertEqual(var.parameterize(), expected)

    def test_single_domain(self):
        """ Passing single domain. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
            'domain': 'glbl',
        }

        domain = Domain(name='glbl')

        variable = Variable('file://test.nc', 'ta', name='v0', domains=domain)

        self.assertEqual(variable.parameterize(), expected)

    def test_multiple_domains(self):
        """ Passing multiple domains. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
            'domain': 'glbl|glbl2',
        }

        domain0 = Domain(name='glbl')
        domain1 = Domain(name='glbl2')

        variable = Variable(
            'file://test.nc',
            'ta',
            name='v0',
            domains=[
                domain0,
                domain1
            ]
        )

        self.assertEqual(variable.parameterize(), expected)
