"""
Parameter module.
"""

from uuid import uuid4

class Parameter(object):
    """ Parameter representation.

    Represents a parameter in a GET request. The parent class must implemnt
    parameterize which becomes the value to the parameter when use in a
    GET request.

    Attributes:
        name: Name of the parameter.
    """
    def __init__(self, name):
        """ Parameter init. """
        self._name = name

        if not self._name:
            self._name = uuid4()

    @property
    def name(self):
        """ Read-only name attribute. """
        return self._name

    def parameterize(self):
        """
        Must return a string representation of the inheriting classs that
        can be used as a value for a GET parameter.
        """
        raise NotImplementedError

    def __repr__(self):
        return 'Parameter(%r)' % self._name

    def __str__(self):
        return '%s' % self._name
