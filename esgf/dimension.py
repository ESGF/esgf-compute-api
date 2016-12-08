"""
Dimension module.
"""

from esgf import errors
from esgf import parameter
from esgf import utils

# pylint: disable=too-few-public-methods
class CRS(object):
    """ Coordinate Reference System (CRS).

    Provides information about the CRS of a dimensions values.

    Attributes:
        name: A String name of the CRS.
    """
    def __init__(self, name):
        """ CRS init. """
        self._name = name

    @property
    def name(self):
        """ Read-only name property. """
        return self._name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return 'CRS(name=%r)' % (self._name,)

    def __str__(self):
        return self._name

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

    indices = CRS('indices')
    values = CRS('values')

    def __init__(self, name, start, end, crs=values, **kwargs):
        """ Dimension init. """
        super(Dimension, self).__init__(name)

        self.start = start

        if end:
            self.end = end
        else:
            self.end = None

        self.crs = crs
        self.step = kwargs.get('step', 1)

    @classmethod
    def from_dict(cls, name, data):
        """ Create dimension from dict representation. """
        if 'start' in data:
            if isinstance(data['start'], str):
                start = utils.int_or_float(data['start'])
            else:
                start = data['start']
        else:
            raise errors.WPSAPIError('Must atleast pass a start value.')

        end = None

        if 'end' in data:
            if isinstance(data['end'], str):
                end = utils.int_or_float(data['end'])
            else:
                end = data['end']

        if 'crs' in data:
            crs = CRS(data['crs'])
        else:
            raise errors.WPSAPIError('Must provide a CRS value.')

        kwargs = {
        }

        if 'step' in data:
            kwargs['step'] = data['step']

        return cls(name, start, end, crs, **kwargs)

    @classmethod
    def from_single_index(cls, name, value, step=None):
        """ Creates dimension from single index. """
        if not step:
            return cls(name, value, value, Dimension.indices)
        else:
            return cls(name, value, value, Dimension.indices, step=step)

    @classmethod
    def from_single_value(cls, name, value, step=None):
        """ Creates dimension from single value. """
        
        if not step:
            return cls(name, value, value, Dimension.values)
        else:
            return cls(name, value, value, Dimension.values, step=step)

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

    def __str__(self):
        return 'name=%s start=%s end=%s step=%s crs=%s' % (
            self.name,
            self.start, 
            self.end, 
            self.step, 
            self.crs)
