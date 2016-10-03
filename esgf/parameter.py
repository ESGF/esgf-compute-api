"""
Parameter module.
"""

from uuid import uuid4

class Parameter(object):
    """ Parameter.

    Base class for parameters. Also used as a shell when re-creating objects
    after being passed to a WPS server.

    """
    def __init__(self, name):
        """ Parameter init. """
        self._name = name

        if not self._name:
            self._name = uuid4()

    @property
    def name(self):
        """ Read-only name attribute. """
        return str(self._name)

    def parameterize(self):
        """
        Must return a string representation of the inheriting classs that
        can be used as a value for a GET parameter.
        """
        raise NotImplementedError

    def __repr__(self):
        return 'Parameter(%r)' % self.name

    def __str__(self):
        return '%s' % self.name
