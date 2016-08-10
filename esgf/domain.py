"""
Domain Module.
"""

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

    @property
    def dimensions(self):
        """ Read-only access to dimensions. """
        return self._dimensions

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
