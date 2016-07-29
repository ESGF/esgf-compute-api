"""
Test runner.
"""

from unittest import TestLoader
from unittest import TextTestRunner

if __name__ == '__main__':
    SUITE = TestLoader().discover('./')

    TextTestRunner(verbosity=2).run(SUITE)
