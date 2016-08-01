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
        self.assertIsNone(var.domain)
        self.assertIsNotNone(var.name)

    def test_parameterize(self):
        """ Test parameterizing variable for GET request. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
        }

        var = Variable('file://test.nc', 'ta', name='v0')

        self.assertEqual(var.parameterize(), expected)

        # Update expected with domain.
        expected['domain'] = 'glbl'

        domain = Domain(name='glbl')

        var = Variable('file://test.nc', 'ta', domain=domain, name='v0')

        self.assertEqual(var.parameterize(), expected)
