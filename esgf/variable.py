"""
Variable module.
"""

import json

from .domain import Domain
from .parameter import Parameter

class Variable(Parameter):
    """ Variable class.

    Generic variable that can be used to describe process input or output.
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
    def from_json(cls, json_raw):
        """ Creates variable from json. """
        json_obj = json.loads(json_raw)

        domain = Domain(name=json_obj['domain'])

        return cls(
            json_obj['uri'],
            json_obj['id'],
            domains=domain,
            mime_type=json_obj['mime-type'])

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

    def parameterize(self):
        """ Parameterize variable for GET request. """
        params = {
            'uri': self.uri,
            'id': self.var_name,
        }

        if self.domains:
            params['domain'] = '|'.join(dom.name for dom in self._domains)

        if self.var_name:
            params['id'] += '|' + self.name

        return params
