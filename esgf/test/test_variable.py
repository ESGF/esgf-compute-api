""" Variable Unittest. """

from unittest import TestCase

from esgf import Domain
from esgf import Variable

class TestVariable(TestCase):
    """ Variable Test Case. """

    def test_optional_init(self):
        """ Tests optional init. """
        var = Variable('file:///test.nc')

        self.assertEqual(var.uri, 'file:///test.nc')
        self.assertIsNone(var.var_name)
        self.assertIsNone(var.domain)
        self.assertIsNotNone(var.name)

    def test_parameterize(self):
        """ Test parameterizing variable for GET request. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'tas',
        }

        var = Variable('file://test.nc', name='tas')

        self.assertEqual(var.parameterize(), expected)

        # Update expected with domain.
        expected['domain'] = 'glbl'

        domain = Domain(name='glbl')

        var = Variable('file://test.nc', domain=domain, name='tas')

        self.assertEqual(var.parameterize(), expected)

        # Update expected with variable name.
        expected['id'] += '|var1'

        var = Variable('file://test.nc', domain=domain, name='tas', var_name='var1')

        self.assertEqual(var.parameterize(), expected)
