"""
Test runner.
"""

from unittest import TestLoader
from unittest import TextTestRunner

TEST_CASES = [
    'esgf.test.test_wps',
]

if __name__ == '__main__':
    SUITE = TestLoader().loadTestsFromNames(TEST_CASES)

    TextTestRunner(verbosity=2).run(SUITE)
