#! /usr/bin/env python

__ALL__ = [
    'CWTError',
    'WPSError',
    'WPSHTTPError',
]

class CWTError(Exception):
    def __init__(self, fmt, *args, **kwargs):
        super(CWTError, self).__init__(fmt.format(*args, **kwargs))

class WPSError(CWTError):
    pass

class WPSHttpError(WPSError):
    @classmethod
    def from_request_response(cls, response):
        fmt = 'Response code {status_code}: {reason}'

        return cls(fmt, status_code=response.status_code, reason=response.reason)
