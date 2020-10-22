#! /usr/bin/env python


class CWTError(Exception):
    def __init__(self, fmt, *args, **kwargs):
        super(CWTError, self).__init__(fmt.format(*args, **kwargs))


class MissingRequiredKeyError(CWTError):
    def __init__(self, key):
        fmt = 'Missing key {!r}'

        super(MissingRequiredKeyError, self).__init__(fmt, key)

class WPSAuthError(CWTError):
    pass

class WPSClientError(CWTError):
    def __init__(self, fmt, *args, **kwargs):
        super(WPSClientError, self).__init__(fmt, *args, **kwargs)


class WPSServerError(CWTError):
    def __init__(self, fmt, *args, **kwargs):
        super(WPSServerError, self).__init__(fmt, *args, **kwargs)


class WPSTimeoutError(CWTError):
    def __init__(self, elapsed):
        fmt = 'Timed out after {!r} seconds'

        super(WPSTimeoutError, self).__init__(fmt, elapsed)
