"""
Unittest for parameter class.
"""

import unittest

import cwt


class HelloWorld(cwt.Parameter):
    """ Test class for overriding method. """

    def __init__(self):
        """ Testimpl init. """
        super(HelloWorld, self).__init__('test')

    def parameterize(self):
        """ Overridden parameterize method. """
        return 'param'


class TestParameter(unittest.TestCase):
    """ Test Case for Parameter class. """

    def test_from_dict(self):
        """ Test from dict. """
        with self.assertRaises(NotImplementedError):
            cwt.Parameter.from_dict('test')

    def test_parameterize(self):
        """ Testing overriding parameterize method. """

        with self.assertRaises(NotImplementedError):
            param = cwt.Parameter('test')

            param.parameterize()

        over_param = HelloWorld()

        self.assertEqual(over_param.parameterize(), 'param')
