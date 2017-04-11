"""
NamedParameter Module.
"""

from cwt import parameter

class NamedParameter(parameter.Parameter):
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

    @classmethod
    def from_list(cls, name, values):
        return cls(name, *values)

    def parameterize(self):
        """ Parameterizes NamedParameter for GET request. """
        if all(isinstance(x, (str, unicode)) for x in self.values):
            value = '|'.join(self.values)
        else:
            raise parameter.ParameterError('Unknow value type {}'.format(type(self.values[0])))

        return {self.name: value}

    def __eq__(self, other):
        return self.name == other.name and self.values == other.values

    def __repr__(self):
        return 'NamedParameter(name=%r, values=%r)' % (
            self.name,
            self.values)