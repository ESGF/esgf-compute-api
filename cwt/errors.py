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
    def __init__(self, fmt, *args, **kwargs):
        super(WPSError, self).__init__(fmt, *args, **kwargs)

class WPSHttpError(WPSError):
    @classmethod
    def from_request_response(cls, response):
        fmt = 'Response code {status_code}: {reason}'

        return cls(fmt, status_code=response.status_code, reason=response.reason)

class WPSExceptionError(WPSError):
    @classmethod
    def from_binding(cls, binding):
        fmt = 'Code: {code} Message: {message}'

        code = binding.Exception[0].exceptionCode

        message = ', '.join(binding.Exception[0].ExceptionText)

        obj = cls(fmt, code=code, message=message)

        obj.binding = binding

        return obj
