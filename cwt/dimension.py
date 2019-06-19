"""
Dimension module.
"""

import warnings

from cwt.errors import CWTError
from cwt.errors import MissingRequiredKeyError
from cwt.parameter import Parameter

# pylint: disable=too-few-public-methods


class CRS(object):
    """ Coordinate Reference System (CRS).

    Provides information about the CRS of a dimensions values.

    Attributes:
        name: A String name of the CRS.
    """

    def __init__(self, name):
        """ CRS init. """
        self.name = name

    def to_dict(self):
        """ Returns a dictionary representation."""
        return {
            'crs': self.name,
        }

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'CRS(name={!r})'.format(self.name)


VALUES = CRS('values')
INDICES = CRS('indices')
TIMESTAMPS = CRS('timestamps')


def int_or_float(value):
    # Only attempt to convert if not already in a valid format
    if not isinstance(value, (int, float)):
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                raise CWTError('Could not convert {!r} to either int or float', value)

    return value


def get_crs_value(crs, value):
    try:
        if crs == INDICES:
            value = int(value)
        elif crs == VALUES:
            value = int_or_float(value)
        elif crs == TIMESTAMPS:
            value = value
        else:
            raise CWTError('Unknown CRS value "{!s}", available: {!s}',
                           crs, ', '.join([str(x) for x in [VALUES, INDICES, TIMESTAMPS]]))
    # Could be raised from int() conversion
    except ValueError:
        raise CWTError('Failed to parse %r from %r', crs, value)

    return value


class Dimension(Parameter):
    """ Dimension.

    Describes a dimension of a plane. This dimension can be constrained
    between two points and the length between each step can be specified or
    it will default to 1.

    There are three pre-defined CRS's; INDICES, VALUES and TIMESTAMPS.

    A dimension starting at 90, ending at -90 with step width of 0.5 degrees.

    >>> lat = Dimension('lat', 90, -90, Dimension.VALUES, step=0.5)

    A dimension representing a single point at 90.

    >>> lat = Dimension.from_single_value(90)

    A dimension with a custom name.

    >>> lat = Dimension('lat', 90, -90, Dimension.VALUES, step=0.5)

    Attributes:
        start: A (str, int, float) of the starting point.
        end: A (str, int, float) of the ending point.
        crs: The CRS of the start and end points.
        step: The distance between each step between the start and end points.
    """

    def __init__(self, name, start, end, crs=VALUES, step=None):
        """ Dimension init. """
        super(Dimension, self).__init__(name)

        self.start = start

        self.end = end

        self.step = step

        if self.step is None:
            self.step = 1

        self.crs = crs

    @classmethod
    def from_dict(cls, data, name):
        """ Create dimension from dict representation. """
        try:
            crs = CRS(data['crs'])

            start = get_crs_value(crs, data['start'])

            end = get_crs_value(crs, data['end'])
        except KeyError as e:
            raise MissingRequiredKeyError(e)

        try:
            step = int_or_float(data['step'])
        except KeyError:
            step = 1

        return cls(name, start, end, crs, step)

    @classmethod
    def from_single_index(cls, name, value, step=None):
        """ Creates dimension from single index. """
        return cls(name, value, value, INDICES, step=step)

    @classmethod
    def from_single_value(cls, name, value, step=None):
        """ Creates dimension from single value. """
        return cls(name, value, value, VALUES, step=step)

    def to_dict(self):
        data = {
            'start': self.start,
            'end': self.end,
            'step': self.step,
        }

        data.update(self.crs.to_dict())

        return data

    def parameterize(self):
        """ Parameterizes object for get queries. """
        warnings.warn('parameterize is deprecated, use to_dict instead',
                      DeprecationWarning)

        return self.to_dict()

    def __repr__(self):
        return 'Dimension(name={!r}, start={!r}, end={!r}, step={!r}, crs={!r})'.format(
            self.name, self.start, self.end, self.step, self.crs)
