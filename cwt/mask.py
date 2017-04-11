"""
Mask Module.
"""

from uuid import uuid4 as uuid

# pylint: disable=too-few-public-methods
class Mask(object):
    """ Mask.
    
    Describes a mask to be applied to a give domain.

    There are some resvered words.

    - var_data
    - mask_data
    - sin
    - cos
    - tan

    *var_data:* refers to the data in the variable that the domain is being
        applied to.

    *mask_data:* refers to the data in masks URI.

    Masks out points in the domain where the mask_data of the location
    is less than 0.5.

    >>> lsm = Mask('http://thredds/clt.nc', 'clt', 'mask_data<0.5')

    Attributes:
        uri: URI of the file containing the mask.
        var_name: Name of the variable that will be used in the operation.
        operation: Expression that defines where the mask is activate.
        name: Custom name for the mask.
    """
    def __init__(self, uri, var_name, operation, name=None):
        """ Mask Init. """
        self.uri = uri
        self.var_name = var_name
        self.operation = operation

        if not name:
            name = str(uuid())

        self.name = name

    @classmethod
    def from_dict(cls, data):
        """ Create mask from dict representation. """
        uri = None

        if 'uri' in data:
            uri = data['uri']

        name = None
        var_name = None

        if 'id' in data:
            if '|' in data['id']:
                var_name, name = data['id'].split('|')
            else:
                var_name = data['id']

        operation = None

        if 'operation' in data:
            operation = data['operation']

        return cls(uri, var_name, operation, name)

    def parameterize(self):
        """ Create a parameter from mask. """
        param_id = self.var_name

        if self.name:
            param_id += '|' + self.name

        return {
            'uri': self.uri,
            'id': param_id,
            'operation': self.operation,
        }

    def __repr__(self):
        return 'Mask(uri=%r, var_name=%r, operation=%r, name=%r)' % (
            self._uri,
            self._var_name,
            self._operation,
            self._name)
