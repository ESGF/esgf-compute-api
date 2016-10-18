"""
Dimension module.
"""

from .utils import int_or_float
from .errors import WPSAPIError
from .parameter import Parameter

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
        return 'CRS(%r)' % (self._name,)

    def __str__(self):
        return self._name

class Dimension(Parameter):
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

    def __init__(self, start, end, crs, **kwargs):
        """ Dimension init. """
        super(Dimension, self).__init__(kwargs.get('name', None))

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
                start = int_or_float(data['start'])
            else:
                start = data['start']
        else:
            raise WPSAPIError('Must atleast pass a start value.')

        end = None

        if 'end' in data:
            if isinstance(data['end'], str):
                end = int_or_float(data['end'])
            else:
                end = data['end']

        if 'crs' in data:
            crs = CRS(data['crs'])
        else:
            raise WPSAPIError('Must provide a CRS value.')

        kwargs = {
            'name': name,
        }

        if 'step' in data:
            kwargs['step'] = data['step']

        return cls(start, end, crs, **kwargs)

    @classmethod
    def from_single_index(cls, value, step=None, name=None):
        """ Creates dimension from single index. """
        if not step:
            return cls(value, value, Dimension.indices, name=name)
        else:
            return cls(value, value, Dimension.indices, step=step, name=name)

    @classmethod
    def from_single_value(cls, value, step=None, name=None):
        """ Creates dimension from single value. """
        
        if not step:
            return cls(value, value, Dimension.values, name=name)
        else:
            return cls(value, value, Dimension.values, step=step, name=name)

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
        return 'Dimension(%r, %r, %r, %r, %r)' % (
            self.start,
            self.end,
            self.step,
            self.crs,
            self.name)

    def __str__(self):
        return '%s %s %s %s %s' % (
            self.start, 
            self.end, 
            self.step, 
            self.crs, 
            self.name)
