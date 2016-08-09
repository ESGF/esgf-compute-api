"""
Variable module.
"""

from .domain import Domain
from .parameter import Parameter

class Variable(Parameter):
    """ Variable class

    Acts as an input variable for a WPS process. The only required argument
    is a uri.

    Attributes:
        uri: URI for the file to be used.
        var_name: Variable name in the file that will be processed.
        domain: Domain used to define which data is processed.
    """
    def __init__(self, uri, var_name, domains=None, name=None):
        """ Variable init. """
        super(Variable, self).__init__(name)

        self._uri = uri
        self._var_name = var_name

        if (domains and isinstance(domains, Domain)):
            domains = [domains]

        self._domains = domains

    @property
    def uri(self):
        """ Read-only uri. """
        return self._uri

    @property
    def var_name(self):
        """ Read-only variable name. """
        return self._var_name

    @property
    def domains(self):
        """ Read-only domain. """
        return self._domains

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
