""" Variable Unittest. """

from unittest import TestCase

from esgf import Domain
from esgf import Variable

class TestVariable(TestCase):
    """ Variable Test Case. """

    def test_optional_init(self):
        """ Tests optional init. """
        var = Variable('file:///test.nc', 'clt')

        self.assertEqual(var.uri, 'file:///test.nc')
        self.assertEqual(var.var_name, 'clt')
        self.assertIsNone(var.domains)
        self.assertIsNotNone(var.name)

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
