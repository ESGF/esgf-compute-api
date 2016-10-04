"""
NamedParameter Module.
"""

from .parameter import Parameter

class NamedParameter(Parameter):
    """ Named Parameter.

    Describes a parameter to be passed to an Operation.

    A NamedParameter with a single value.

    >>> axis = NamedParameter('axis', 'time')

    A NamedParameter with multiple values.

    >>> axes = NamedParameter('axes', 'latitude', 'longitude')

    Attributes:
        name: Name of the parameter.
        *args: Values of the parameter.
    """
    def __init__(self, name, *args):
        """ NamedParameter init. """
        super(NamedParameter, self).__init__(name)

        self.values = list(args)

    @classmethod
    def from_string(cls, name, values):
        """ Creates NamedParameter from string value. """
        return cls(name, *values.split('|'))

    def parameterize(self):
        """ Parameterizes NamedParameter for GET request. """
        if all(isinstance(x, str) for x in self.values):
            value = '|'.join(self.values)
        elif (len(self.values) == 1 and
              isinstance(self.values[0], Parameter)):
            value = self.values[0].name

        return value

    def __repr__(self):
        return 'NamedParameter(%r, %r)' % (
            self.name,
            self.values)

    def __str__(self):
        return '%s %s' % (self.name, self.values)
