"""
Test runner.
"""

from unittest import TestLoader
from unittest import TextTestRunner

import sys

if __name__ == '__main__':
    SUITE = TestLoader().discover('./')

    ret = TextTestRunner(verbosity=2).run(SUITE).wasSuccessful()

    sys.exit(0 if ret else 1)
