"""
Mask Module.
"""

from uuid import uuid4

# pylint: disable=too-few-public-methods
class Mask(object):
    """ Mask class.

    Defines a mask to be used with a domain on an input variable.
    """
    def __init__(self, uri, var_name, operation, name=None):
        """ Mask Init. """
        self._uri = uri
        self._var_name = var_name
        self._operation = operation

        if not name:
            name = str(uuid4())

        self._name = name

    def parameterize(self):
        """ Create a parameter from mask. """
        param_id = self._var_name

        if self._name:
            param_id += '|' + self._name

        return {
            'uri': self._uri,
            'id': param_id,
            'operation': self._operation,
        }
