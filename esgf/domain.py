"""
Domain Module.
"""

from .mask import Mask
from .errors import WPSAPIError
from .dimension import Dimension
from .parameter import Parameter

class Domain(Parameter):
    """ Domain.

    A domain consist of one or more dimensions. A mask can be associated with
    a domain, further construing the domain being represented.

    Simple domain.

    >>> domain = Domain([Dimesnion(90, -90, Dimension.values)])

    Domain with a mask.

    >>> domain = Domain([
            Dimension(90, -90, Dimension.values, name='lon'),
            Dimension(0, 90, Dimension.values, name='lat'),
        ],
        mask = Mask('http://thredds/clt.nc', 'clt', 'var_data<0.5'))

    Attributes:
        dimensions: List of Dimensions.
        mask: Mask to be applied to the domain.
        name: Name of the domain.
    """
    def __init__(self, dimensions=None, mask=None, name=None):
        """ Domain init. """
        super(Domain, self).__init__(name)

        if not dimensions:
            dimensions = []

        self._dimensions = dimensions
        self._mask = mask

    @classmethod
    def from_dict(cls, data):
        """ Creates domain from dict reperesentation. """
        blacklist = ['id', 'mask']

        name = None

        if 'id' in data:
            name = data['id']
        else:
            raise WPSAPIError('Domain must provide an id.')

        dimensions = []

        for key, value in data.iteritems():
            if key not in blacklist:
                dimensions.append(Dimension.from_dict(key, value))

        mask = None

        if 'mask' in data:
            mask = Mask.from_dict(data['mask'])

        return cls(dimensions=dimensions, mask=mask, name=name)

    @property
    def dimensions(self):
        """ Read-only access to dimensions. """
        return self._dimensions

    @property
    def mask(self):
        """ Returns associated mask. """
        return self._mask

    def add_dimension(self, dimension):
        """ Add a dimension. """
        self._dimensions.append(dimension)

    def parameterize(self):
        """ Returns parameter for GET request. """
        param = {
            'id': self.name
        }

        for dimension in self.dimensions:
            param[dimension.name] = dimension.parameterize()

        if self._mask:
            param['mask'] = self._mask.parameterize()

        return param

    def __repr__(self):
        return 'Domain(%r, %r, %r)' % (self._dimensions, self._mask, self.name)

    def __str__(self):
        return '%s %s, %s' % (self._dimensions, self._mask, self.name)
