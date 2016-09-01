"""
Mask Module.
"""

from uuid import uuid4

# pylint: disable=too-few-public-methods
class Mask(object):
    """ Mask class.

    Defines a mask to be used with a domain on an input variable.
    """
    def __init__(self, uri, var_name, operation, name=None):
        """ Mask Init. """
        self._uri = uri
        self._var_name = var_name
        self._operation = operation

        if not name:
            name = str(uuid4())

        self._name = name

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

    @property
    def uri(self):
        """ URI property. """
        return self._uri

    @property
    def var_name(self):
        """ Variable name. """
        return self._var_name

    @property
    def operation(self):
        """ Mask operation. """
        return self._operation

    @property
    def name(self):
        """ Mask name. """
        return self._name

    def parameterize(self):
        """ Create a parameter from mask. """
        param_id = self._var_name

        if self._name:
            param_id += '|' + self._name

        return {
            'uri': self._uri,
            'id': param_id,
            'operation': self._operation,
        }

    def __repr__(self):
        return 'Mask(%r, %r, %r, %r)' % (
            self._uri,
            self._var_name,
            self._operation,
            self._name)

    def __str__(self):
        return '%s %s %s %s' % (
            self._uri,
            self._var_name,
            self._operation,
            self._name)
