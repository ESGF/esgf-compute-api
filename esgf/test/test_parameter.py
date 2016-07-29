"""
Unittest for parameter class.
"""

from unittest import TestCase

from esgf import Parameter

class TestParameter(TestCase):
    """ Test Case for Parameter class. """

    def test_parameterize(self):
        """ Testing overriding parameterize method. """

        with self.assertRaises(NotImplementedError):
            param = Parameter('test')
            param.parameterize()

        class TestImpl(Parameter):
            """ Test class for overriding method. """
            def __init__(self):
                """ Testimpl init. """
                super(TestImpl, self).__init__('test')

            def parameterize(self):
                """ Overridden parameterize method. """
                return 'param'

        over_param = TestImpl()

        self.assertEqual(over_param.parameterize(), 'param')
