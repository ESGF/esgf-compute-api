"""
NamedParameter Module.
"""

from .parameter import Parameter

class NamedParameter(Parameter):
    """ Named Parameter class

    A NamedParameter is used to define a keyword argument that can be passed
    to an Operation.
    """
    def __init__(self, name, *args):
        """ NamedParameter init. """
        super(NamedParameter, self).__init__(name)

        self.values = list(args)

    def parameterize(self):
        """ Parameterizes NamedParameter for GET request. """
        return ''.join(self.values)
