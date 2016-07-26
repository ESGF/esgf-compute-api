from unittest import TestLoader
from unittest import TextTestRunner

TEST_CASES = [
    'esgf.test.test_wps',
]

if __name__ == '__main__':
    suite = TestLoader().loadTestsFromNames(TEST_CASES)
    TextTestRunner(verbosity=2).run(suite)
