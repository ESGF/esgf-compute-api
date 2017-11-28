"""
Parameter module.
"""

from uuid import uuid4 as uuid

__all__ = ['ParameterError', 'Parameter']

class ParameterError(Exception):
    pass

class Parameter(object):
    """ Parameter.

    Base class for parameters. Also used as a shell when re-creating objects
    after being passed to a WPS server.

    """
    def __init__(self, name):
        """ Parameter init. """
        self._name = name

        if not self._name:
            self._name = str(uuid())[37:]

    @classmethod
    def from_dict(cls, data):
        """ Loads a parameter from its parameter form. """
        raise NotImplementedError

    @property
    def name(self):
        """ Read-only name attribute. """
        return str(self._name)

    def parameterize(self):
        """ Return a representation of this parameter. """
        raise NotImplementedError
