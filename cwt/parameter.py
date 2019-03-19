"""
Parameter module.
"""

from uuid import uuid4 as uuid


class Parameter(object):
    """ Parameter.

    Base class for parameters. Also used as a shell when re-creating objects
    after being passed to a WPS server.

    """

    def __init__(self, name):
        """ Parameter init. """
        self.name = name

        if self.name is None:
            self.name = str(uuid())

    @classmethod
    def from_dict(cls, data):
        """ Loads a parameter from its parameter form. """
        raise NotImplementedError

    def parameterize(self):
        """ Return a representation of this parameter. """
        raise NotImplementedError
