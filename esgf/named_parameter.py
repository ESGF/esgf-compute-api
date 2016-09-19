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
        if all(isinstance(x, str) for x in self.values):
            value = '|'.join(self.values)
        elif (len(self.values) == 1 and
              isinstance(self.values[0], Parameter)):
            value = self.values[0].name

        return '%s: %s' % (self.name, value)

    def __repr__(self):
        return 'NamedParameter(%r, %r)' % (
            self.name,
            self.values)

    def __str__(self):
        return '%s %s' % (self.name, self.values)
