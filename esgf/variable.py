"""
Variable module.
"""

from esgf import domain
from esgf import parameter

class Variable(parameter.Parameter):
    """ Variable.
    
    Describes a variable to be used by an Operation.

    >>> tas = Variable('http://thredds/tas.nc', 'tas', name='tas')

    Attributes:
        uri: A String URI for the file containing the variable data.
        var_name: A String name of the variable.
        domains: List of domain.Domain objects to constrain the variable data.
        mime_type: A String name of the URI mime-type.
        name: Custom name of the Variable.
    """
    def __init__(self, uri, var_name, **kwargs):
        """ Variable init. """
        super(Variable, self).__init__(kwargs.get('name', None))

        self.uri = uri
        self._var_name = var_name

        domains = kwargs.get('domains', None)

        if domains and isinstance(domains, domain.Domain):
            domains = [domains]

        self.domains = domains
        self._mime_type = kwargs.get('mime_type', None)

    @classmethod
    def from_dict(cls, data):
        """ Create variable from dict representation. """
        uri = None

        if 'uri' in data:
            uri = data['uri']
        else:
            raise parameter.ParameterError('Variable must provide a uri.')

        name = None
        var_name = None

        if 'id' in data:
            if '|' in data['id']:
                var_name, name = data['id'].split('|')
            else:
                raise parameter.ParameterError('Variable id must contain a variable name and id.')
        else:
            raise parameter.ParameterError('Variable must provide an id.')

        domains = None

        if 'domain' in data:
            domains = data['domain']

            if not isinstance(domains, (list, tuple)):
                domains = [domains]

        mime_type = None

        if 'mime_type' in data:
            mime_type = data['mime_type']

        return cls(uri, var_name, domains=domains, name=name, mime_type=mime_type)

    @property
    def var_name(self):
        """ Variable name in uri. """
        return self._var_name

    @property
    def mime_type(self):
        """ Mime-type of uri. """
        return self._mime_type

    def parameterize(self):
        """ Parameterize variable for GET request. """
        params = {
            'uri': self.uri,
            'id': self.var_name,
        }

        if self.domains:
            params['domain'] = '|'.join(dom.name for dom in self.domains)

        if self.var_name:
            params['id'] += '|' + str(self.name)

        if self.mime_type:
            params['mime_type'] = self.mime_type

        return params

    def __repr__(self):
        return ('Variable(name=%r, uri=%r, var_name=%r, domains=%r, '
                'mime_type=%r)' % (self.name, self.uri, self._var_name,
                                   self.domains, self._mime_type))
