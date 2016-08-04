"""
Operation Unittest.
"""

import re

from unittest import TestCase

from esgf import Operation
from esgf import DuplicateParameterError
from esgf import NamedParameter
from esgf import Variable

class TestOperation(TestCase):
    """ Operation Test Case. """

    def test_optional_init(self):
        """ Tests optional init values. """
        test = Operation('OP', 'test')

        self.assertEqual(test.parameters, [])
        self.assertIsNotNone(test.var_name)
        self.assertEqual(test.name, 'OP.test')

    def test_add_parameter(self):
        """ Tests adding parameters. """
        test = Operation('OP', 'test')
        sub = Operation('OP', 'sub')
        mean = Operation('OP', 'mean')

        axes = NamedParameter('axes', 't')

        test.add_parameter(axes)

        # Check adding a parameter
        self.assertListEqual(test.parameters, [axes])

        # Check adding a duplicate parameter
        with self.assertRaises(DuplicateParameterError) as ctx:
            test.add_parameter(axes)

        self.assertEqual(ctx.exception.message, 'Parameter already exists.')

        test.add_parameter(sub)

        # Check adding an operation
        self.assertListEqual(test.parameters, [axes, sub])

        # Check adding a duplicate operation
        with self.assertRaises(DuplicateParameterError):
            test.add_parameter(sub)

        # Check circular dependency
        with self.assertRaises(DuplicateParameterError) as ctx:
            sub.add_parameter(test)

        self.assertEqual(ctx.exception.message, 'Circular dependency.')

        sub.add_parameter(mean)

        # Check adding additional reference of an operation
        test.add_parameter(mean)

        self.assertListEqual(test.parameters, [axes, sub, mean])

    def test_parameters(self):
        """ Test parameterizing an operation for GET request. """
        variable0 = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        test = Operation('OP', 'test', [variable0])

        expected = 'v0'

        self.assertEqual(test.parameterize(), expected)

        axes = NamedParameter('axes', 't')

        test.add_parameter(axes)

        expected += ', axes: t'

        self.assertEqual(test.parameterize(), expected)

    def test_operation(self):
        """ Test parameterizing an operation containing other operations. """
        variable0 = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        axes = NamedParameter('axes', 't')

        mean = Operation('OP', 'mean', [variable0, axes])

        test = Operation('OP', 'test', [mean])

        self.assertIsNotNone(re.match(r'(.*):OP.mean\(v0, axes: t\)',
                                      test.parameterize()))

    def test_operations_multi(self):
        """ Test parameterizing an operation containing multiple operations. """
        variable0 = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        axes = NamedParameter('axes', 't')
        bins = NamedParameter('bins', 't', 'month', 'ave', 'year')

        anomaly = Operation('OP', 'anomaly', [variable0, axes])
        binop = Operation('OP', 'bin', [variable0, axes, bins])

        test = Operation('OP', 'test', [anomaly, binop])

        self.assertIsNotNone(re.match(r'(.*):OP.anomaly\(v0, axes: t\), (.*)' +
                                      r':OP.bin\(v0, axes: t, bins: t|month|' +
                                      r'ave|year\)', test.parameterize()))

    def test_dependencies(self):
        """ Tests parameterzing and operation with dependencies. """
        variable0 = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        axes = NamedParameter('axes', 't')

        mean = Operation('OP', 'mean', [variable0, axes], var_name='vm')

        diff = Operation('OP', 'diff', [variable0, mean])

        test = Operation('OP', 'test', [mean, diff])

        self.assertIsNotNone(re.match(r'vm:OP.mean\(v0, axes: t\), (.*):OP.' +
                                      r'diff\(v0, vm\)', test.parameterize()))

    def test_complex_workflow(self):
        """ Test parallel operations with deep dependencies. """
        mean = Operation('OP', 'mean')

        diff = Operation('OP', 'diff')

        anomaly = Operation('OP', 'anomaly', [mean, diff], var_name='anom')

        bins = Operation('OP', 'bin', var_name='bins')

        subset = Operation('OP', 'subset', [bins], var_name='sub')

        subset2 = Operation('OP', 'subset', var_name='sub2')

        test = Operation('OP', 'test', [anomaly, subset, subset2, mean])

        self.assertIsNotNone(re.match(r'(.*):OP.mean\(\), (.*):OP.diff\(\), ' +
                                      r'anom:OP.anomaly\(\1, \2\), bins:OP' +
                                      r'.bin\(\), sub:OP.subset\(bins\), sub' +
                                      r'2:OP.subset\(\)', test.parameterize()))
