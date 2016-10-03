"""
Variable module.
"""
from StringIO import StringIO

import os
import json
import requests

from .errors import WPSAPIError
from .errors import WPSClientError
from .domain import Domain
from .parameter import Parameter

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

        self._uri = uri
        self._var_name = var_name

        domains = kwargs.get('domains', None)

        if domains and isinstance(domains, Domain):
            domains = [domains]

        self._domains = domains
        self._mime_type = kwargs.get('mime_type', None)

    @classmethod
    def from_dict(cls, data, domains_dict):
        """ Create variable from dict representation. """
        uri = None

        if 'uri' in data:
            uri = data['uri']
        else:
            raise WPSAPIError('Variable must provide a uri.')

        name = None
        var_name = None

        if 'id' in data:
            if '|' in data['id']:
                var_name, name = data['id'].split('|')
            else:
                raise WPSAPIError('Variable id must contain a variable name and id.')
        else:
            raise WPSAPIError('Variable must provide an id.')

        domains = []

        if 'domain' in data:
            if not isinstance(data['domain'], (list, tuple)):
                domain_data = [data['domain']]
            else:
                domain_data = data['domain']

            domains = [domains_dict[x] for x in domain_data]

        mime_type = None

        if 'mime_type' in data:
            mime_type = data['mime_type']

        return cls(uri, var_name, domains=domains, name=name, mime_type=mime_type)

    @property
    def uri(self):
        """ Uri to file. """
        return self._uri

    @property
    def var_name(self):
        """ Variable name in uri. """
        return self._var_name

    @property
    def domains(self):
        """ Associated domain. """
        return self._domains

    @property
    def mime_type(self):
        """ Mime-type of uri. """
        return self._mime_type

    def _download_http(self, output, chunk_size):
        """ HTTP download. """
        if not chunk_size:
            chunk_size = 1024

        response = requests.get(self._uri, stream=True)

        for chunk in response.iter_content(chunk_size):
            output.write(chunk)

    def download(self, out_path, chunk_size=None):
        """ Factory download method. """
        download_fn = None

        if self._uri[:4] == 'http':
            download_fn = self._download_http
        else:
            raise WPSClientError('Unsupported uri %s' % (self._uri,))

        with open(out_path, 'wb') as out_file:
            download_fn(out_file, chunk_size)

        return os.path.abspath(out_path)

    def parameterize(self):
        """ Parameterize variable for GET request. """
        params = {
            'uri': self.uri,
            'id': self.var_name,
        }

        if self.domains:
            params['domain'] = '|'.join(dom.name for dom in self._domains)

        if self.var_name:
            params['id'] += '|' + str(self.name)

        if self.mime_type:
            params['mime_type'] = self.mime_type

        return params

    def __repr__(self):
        return 'Variable(%r %r %r %r %r)' % (
            self.name,
            self._uri,
            self._var_name,
            self._domains,
            self._mime_type)

    def __str__(self):
        return '%s %s %s %s %s' % (
            self.name,
            self._uri,
            self._var_name,
            self._domains,
            self._mime_type)
