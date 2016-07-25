import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('esgf/test', pattern='*.py')

    unittest.TextTestRunner().run(suite)
