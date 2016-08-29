"""
Dimension module.
"""

from .utils import int_or_float
from .errors import WPSAPIError
from .parameter import Parameter

# pylint: disable=too-few-public-methods
class CRS(object):
    """ Coordinate Reference System.

    Representation of the possible Coordinate Reference System values.
    """
    def __init__(self, name):
        """ CRS init. """
        self._name = name

    @property
    def name(self):
        """ Read-only name property. """
        return self._name

    def __str__(self):
        """ String representation. """
        return self._name

    def __eq__(self, other):
        return self.name == other.name

class Dimension(Parameter):
    """ Domain dimensions.

    Represents a dimension within a domain. Most common dimensions are
    time, latitude, longitude, level. Can be created with a start and
    end value or just a single start value.

    Attributes:
        start: Index or value denoting start of the dimension.
        end: Index or value denoting end of the dimension.
        crs: Coordinate Reference System (Index or Value).
        step: Step size between each value.
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
        return cls(value, None, Dimension.indices, step=step, name=name)

    @classmethod
    def from_single_value(cls, value, step=None, name=None):
        """ Creates dimension from single value. """
        return cls(value, None, Dimension.values, step=step, name=name)

    def parameterize(self):
        """ Parameterizes object for get queries. """
        params = {
            'start': self.start,
            'end': self.end,
            'step': self.step,
            'crs': self.crs.name,
        }

        return params

    def __str__(self):
        """ String representation. """
        return 'Dimension(%s, %s, %s, step=%s, name="%s")' % (self.start, \
                                                              self.end, \
                                                              self.crs, \
                                                              self.step, \
                                                              self.name)
