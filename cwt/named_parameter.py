"""
NamedParameter Module.
"""

import warnings

from cwt.parameter import Parameter

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
    def __init__(self, name, *values):
        """ NamedParameter init. """
        super(NamedParameter, self).__init__(name)

        self.values = values

    @classmethod
    def from_string(cls, name, data):
        """ Creates NamedParameter from string value. """
        return cls(name, *data.split('|'))

    def __eq__(self, other):
        return self.name == other.name and self.values == other.values

    def __repr__(self):
        return 'NamedParameter(name={!r}, values={!r})'.format(self.name, self.values)

    def to_dict(self):
        """ Returns dict representation."""
        return { self.name: '|'.join(self.values) }

    def parameterize(self):
        """ Parameterizes NamedParameter for GET request. """
        warnings.warn('parameterize is deprecated, use to_dict instead',
                      DeprecationWarning)

        return self.to_dict()
