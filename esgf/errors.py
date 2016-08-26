"""
Errors Module.
"""
class WPSAPIError(Exception):
    """ General API error."""
    pass

class WPSClientError(Exception):
    """ WPS Client-side error. """
    pass

class WPSServerError(Exception):
    """ WPS Server-side error. """
    pass
