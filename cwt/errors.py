#! /usr/bin/env python

class CWTError(Exception):
    def __init__(self, fmt, *args, **kwargs):
        super(CWTError, self).__init__(fmt.format(*args, **kwargs))

class MissingRequiredKeyError(CWTError):
    def __init__(self, *args):
        fmt = 'Missing key {!r}'

        super(MissingRequiredKeyError, self).__init__(fmt, *args)

class WPSClientError(CWTError):
    def __init__(self, fmt, *args, **kwargs):
        super(WPSClientError, self).__init__(fmt, *args, **kwargs)
