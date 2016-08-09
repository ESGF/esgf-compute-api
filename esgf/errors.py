"""
Errors Module.
"""
class WPSClientError(Exception):
    """ WPS Client-side error. """
    pass

class WPSServerError(Exception):
    """ WPS Server-side error. """
    pass
