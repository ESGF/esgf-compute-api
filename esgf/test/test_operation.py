"""
Operation Unittest.
"""

import re

from unittest import TestCase

from esgf import Operation
from esgf import NamedParameter
from esgf import Variable
from esgf import Domain

class TestOperation(TestCase):
    """ Operation Test Case. """

    def test_repr(self):
        """ Tests __repr__ value."""
        result = 'Operation(\'OP.test\', [], \'test\', None, [])'

        op = Operation('OP.test', name='test')

        self.assertEqual(repr(op), result)

    def test_str(self):
        """ Tests __str__ value."""
        result = 'OP.test [] test None []'

        op = Operation('OP.test', name='test') 
        
        self.assertEquals(str(op), result)

    def test_operation_input(self):
        """ Tests passing an operation as an input. """
        result = {
            'input': ['test2'],
            'name': 'OP.test',
            'result': 'test1',
        }

        op1 = Operation('OP.test', name='test1')
        op2 = Operation('OP.test2', name='test2')

        op1.add_input(op2)

        self.assertEqual(op1.parameterize(), result)

    def test_from_dict(self):
        """ Tests creating operation from dictionary. """
        data = {
            'name': 'OP.test',
            'input': ['v0', 'v1'],
            'result': 'cycle',
            'domain': 'd0',
            'axes': 't',
            'gridder': {
                'tool': 'esmf',
                'method': 'conserve',
                'grid': 'd0',
            },
            'bins': 't|month|ave|year',
        }

        op = Operation.from_dict(data)

        self.assertDictContainsSubset(data, op.parameterize())

    def test_multiple_argument(self):
        """ Tests passing multipel arguments. """
        result = {
            'name': 'OP.test',
            'input': [],
            'axes': 'longitude|latitude',
            'bins': 't|month|ave|year',
        }

        op = Operation('OP.test')
        op.add_parameter(NamedParameter('axes', 'longitude', 'latitude'))
        op.add_parameter(NamedParameter('bins', 't', 'month', 'ave', 'year'))

        self.assertDictContainsSubset(result, op.parameterize())

    def test_single_argument(self):
        """ Tests passing single argument. """
        result = {
            'name': 'OP.test',
            'input': [],
            'axes': 'longitude|latitude',
        }

        op = Operation('OP.test')
        op.add_parameter(NamedParameter('axes', 'longitude', 'latitude'))

        self.assertDictContainsSubset(result, op.parameterize())

    def test_domain(self):
        """ Tests setting an operations domain. """
        result = {
            'name': 'OP.test',
            'input': [],
            'domain': 'd0',
        }

        domain = Domain(name='d0')

        op = Operation('OP.test')
        op.domain = domain

        self.assertDictContainsSubset(result, op.parameterize())

    def test_result(self):
        """ Tests setting an operations result identifier. """
        result = {
            'name': 'OP.test',
            'input': [],
            'result': 'cycle',
        }

        op = Operation('OP.test', name='cycle')

        self.assertEqual(op.parameterize(), result)

    def test_multiple_input(self):
        """ Tests operation with multiple input. """
        result = {
            'name': 'OP.test',
            'input': ['v0', 'v1'],
        }

        variable1 = Variable('file:///test.nc', 'tas', name='v0') 
        variable2 = Variable('file:///test.nc', 'tas', name='v1') 

        op = Operation('OP.test')
        op.add_input(variable1)
        op.add_input(variable2)

        self.assertDictContainsSubset(result, op.parameterize())

    def test_single_input(self):
        """ Tests operation with single input. """
        result = {
            'name': 'OP.test',
            'input': ['v0'],
        }

        variable = Variable('file:///test.nc', 'tas', name='v0') 

        op = Operation('OP.test')
        op.add_input(variable)

        self.assertDictContainsSubset(result, op.parameterize())

    def test_basic(self):
        """ Tests simple operation. """
        result = {
            'name': 'OP.test',
            'input': [],
        }

        op = Operation('OP.test')

        self.assertDictContainsSubset(result, op.parameterize())
