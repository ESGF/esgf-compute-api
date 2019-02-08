"""
Variable module.
"""

import warnings

from cwt.parameter import Parameter

class Variable(Parameter):
    """ Variable.
    
    Describes a variable to be used by an Operation.

    >>> tas = Variable('http://thredds/tas.nc', 'tas', name='tas')

    Attributes:
        uri: A String URI for the file containing the variable data.
        var_name: A String name of the variable.
        domains: List of Domain objects to constrain the variable data.
        mime_type: A String name of the URI mime-type.
        name: Custom name of the Variable.
    """
    def __init__(self, uri, var_name, **kwargs):
        """ Variable init. """
        super(Variable, self).__init__(kwargs.get('name', None))

        self.uri = uri
        self.var_name = var_name
        self.domain = kwargs.get('domain', None)
        self.mime_type = kwargs.get('mime_type', None)

    @classmethod
    def from_dict(cls, data):
        """ Create variable from dict representation. """
        try:
            uri = data['uri']
        except KeyError as e:
            raise MissingRequiredKeyError(e)

        try:
            var_name, name = data['id'].split('|')
        except KeyError as e:
            raise MissingRequiredKeyError(e)
        except ValueError:
            raise CWTError('Could not split variable name and identifier from {!r}', data['id'])

        domain = data.get('domain', None)

        try:
            mime_type = data['mime_type']
        except KeyError:
            mime_type = None

        return cls(uri, var_name, domain=domain, name=name, mime_type=mime_type)

    def resolve_domains(self, domains):
        """ Resolves the domain identifiers to objects. """

        if self.domains is None:
            return
    
        new_domains = []

        for d in self.domains:
            if d not in domains:
                raise Exception('Could not find domain {}'.format(d))

            new_domains.append(domains[d])

        self.domains = new_domains

    def to_dict(self):
        data = {
            'uri': self.uri,
            'id': self.var_name,
        }

        if self.domain:
            try:
                data['domain'] = self.domain.name
            except AttributeError:
                data['domain'] = self.domain

        if self.var_name:
            data['id'] += '|' + str(self.name)

        if self.mime_type:
            data['mime_type'] = self.mime_type

        return data

    def parameterize(self):
        """ Parameterize variable for GET request. """
        warnings.warn('parameterize is deprecated, use to_dict instead',
                      DeprecationWarning)

        return self.to_dict()

    def __repr__(self):
        return ('Variable(name=%r, uri=%r, var_name=%r, domains=%r, '
                'mime_type=%r)').format( self.name, self.uri, self.var_name, 
                                        self.domains, self.mime_type)
