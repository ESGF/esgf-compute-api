""" Testing module. """

import sys

from StringIO import StringIO

# pylint: disable=too-few-public-methods
class MockPrint(object):
    """ Class to mock stdout. """
    def __init__(self):
        self._old_stdout = None
        self._buffer = StringIO()

    @property
    def value(self):
        """ Read-only value from mocked stdout. """
        return self._buffer.getvalue().replace('/n', '')

    def __enter__(self):
        """ Enter context. """
        self._old_stdout = sys.stdout
        sys.stdout = self._buffer

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Exit context. """
        sys.stdout = self._old_stdout
