#! /usr/bin/env python
""" Testing module. """

import unittest

suite = unittest.TestLoader().discover('./')

unittest.TextTestRunner(verbosity=2).run(suite)
