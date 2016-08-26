"""
Domain Module.
"""

from .mask import Mask
from .errors import WPSAPIError
from .dimension import Dimension
from .parameter import Parameter

class DomainError(Exception):
    """ Domain Error. """
    pass

class Domain(Parameter):
    """ Domain

    Domain represents a named collection of dimensions that will be used
    when during the evaluation of a process.
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

        if len(dimensions) < 1:
            raise WPSAPIError('Domain must provide atleast one dimension.')

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
        if len(self.dimensions) <= 0:
            raise DomainError('Need atleast one dimension.')

        param = {
            'id': self.name
        }

        for dimension in self.dimensions:
            param[dimension.name] = dimension.parameterize()

        if self._mask:
            param['mask'] = self._mask.parameterize()

        return param
