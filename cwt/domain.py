"""
Domain Module.
"""

import cwt

__all__ = ['Domain']

class Domain(cwt.Parameter):
    """ Domain.

    A domain consist of one or more dimensions. A mask can be associated with
    a domain, further construing the domain being represented.

    Simple domain.

    >>> domain = Domain([Dimesnion('lat', 90, -90, Dimension.values)])

    Domain with a mask.

    >>> domain = Domain([
            Dimension('lat', 90, -90, Dimension.values, name='lat'),
            Dimension('lon', 0, 90, Dimension.values, name='lon'),
        ],
        mask = Mask('http://thredds/clt.nc', 'clt', 'var_data<0.5'))

    Attributes:
        dimensions: List of Dimensions.
        mask: Mask to be applied to the domain.
        name: Name of the domain.
    """
    def __init__(self, dimensions=None, mask=None, name=None, **kwargs):
        """ Domain init. """
        super(Domain, self).__init__(name)

        if dimensions is None:
            dimensions = []

        for name, value in kwargs.iteritems():
            if isinstance(value, slice):
                args = [
                    name, 
                    value.start, 
                    value.stop, 
                    cwt.INDICES, 
                    value.step
                ]
            elif isinstance(value, (list, tuple)):
                if len(value) < 2:
                    raise cwt.WPSError('Must provide a minimum of two values (start, stop) for dimension "{dim}"', dim=name)

                if len(value) > 2:
                    step = value[3]
                else:
                    step = 1

                if all(isinstance(x, (float, int)) for x in value[:2]):
                    crs = cwt.VALUES
                elif all(isinstance(x, str) for x in value[:2]):
                    crs = cwt.TIMESTAMPS
                else:
                    raise cwt.WPSError('Could not determin dimension crs')

                args = [
                    name,
                    value[0],
                    value[1],
                    crs,
                    step
                ]
            else:
                raise cwt.WPSError('Dimension\'s value cannot be of type "{type}"', type=type(value))

            dimensions.append(cwt.Dimension(*args))

        self.dimensions = dimensions
        self.mask = mask

    @classmethod
    def from_dict(cls, data):
        """ Creates domain from dict reperesentation. """
        blacklist = ['id', 'mask']

        name = None

        if 'id' in data:
            name = data['id']
        else:
            raise cwt.ParameterError('Missing id attribute')

        dimensions = []

        for key, value in data.iteritems():
            if key not in blacklist:
                dimensions.append(cwt.Dimension.from_dict(value, key))

        mask_data = None

        if 'mask' in data:
            mask_data = cwt.Mask.from_dict(data['mask'])

        return cls(dimensions=dimensions, mask=mask_data, name=name)

    def get_dimension(self, names):
        if not isinstance(names, (list, tuple)):
            names = [names]

        for dim in self.dimensions:
            if dim.name in names:
                return dim

        return None

    def add_dimension(self, dimension):
        """ Add a dimension. """
        self.dimensions.append(dimension)

    def parameterize(self):
        """ Returns parameter for GET request. """
        param = {
            'id': self.name
        }

        for dimension in self.dimensions:
            param[dimension.name] = dimension.parameterize()

        if self.mask:
            param['mask'] = self.mask.parameterize()

        return param

    def __repr__(self):
        return ('Domain(dimensions=%r, mask=%r, name=%r)' %
                (self.dimensions, self.mask, self.name))
