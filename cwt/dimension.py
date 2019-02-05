"""
Dimension module.
"""

from cwt import parameter

__all__ = ['CRS', 'VALUES', 'INDICES', 'Dimension']

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

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __repr__(self):
        return 'CRS(name={})'.format(self.name)

VALUES = CRS('values')
INDICES = CRS('indices')
TIMESTAMPS = CRS('timestamps')

def int_or_float(data):
    try:
        return int(data)
    except ValueError:
        return float(data)

class Dimension(parameter.Parameter):
    """ Dimension.

    Describes a dimension of a plane. This dimension can be constrained 
    between two points and the length between each step can be specified or
    it will default to 1.

    There are two pre-defined CRS's; indices and values.

    A dimension starting at 90, ending at -90 with step width of 0.5 degrees.

    >>> lat = Dimension(90, -90, Dimension.values, step=0.5)

    A dimension representing a single point at 90.

    >>> lat = Dimension.from_single_value(90)

    A dimension with a custom name.

    >>> lat = Dimension(90, -90, Dimension.values, step=0.5, name='lat')

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

        if end is not None:
            self.end = end
        else:
            self.end = None

        self.step = step

        if self.step is None:
            self.step = 1

        self.crs = crs

    @classmethod
    def from_dict(cls, data, name):
        """ Create dimension from dict representation. """
        if 'crs' in data:
            crs = CRS(data['crs'])
        else:
            raise parameter.ParameterError('Must provide a CRS value.')

        if 'start' in data:

            if isinstance(data['start'], str) and crs != TIMESTAMPS:
                start = int_or_float(data['start'])
            else:
                start = data['start']
        else:
            raise parameter.ParameterError('Must provide a start value.')

        end = None

        if 'end' in data:


            if isinstance(data['end'], str) and crs != TIMESTAMPS:
                end = int_or_float(data['end'])
            else:
                end = data['end']

        step = None

        if 'step' in data:
            step = data['step']
        
        return cls(name, start, end, crs, step)

    @classmethod
    def from_single_index(cls, name, value, step=None):
        """ Creates dimension from single index. """
        return cls(name, value, value, INDICES, step=step)

    @classmethod
    def from_single_value(cls, name, value, step=None):
        """ Creates dimension from single value. """
        return cls(name, value, value, VALUES, step=step)

    def parameterize(self):
        """ Parameterizes object for get queries. """
        params = {
            'start': self.start,
            'end': self.end,
            'step': self.step,
            'crs': self.crs.name,
        }

        return params

    def __repr__(self):
        return 'Dimension(name=%r, start=%r, end=%r, step=%r, crs=%r)' % (
            self.name,
            self.start,
            self.end,
            self.step,
            self.crs)
