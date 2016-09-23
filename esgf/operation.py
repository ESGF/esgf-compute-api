"""
Operation Module.
"""

from uuid import uuid4

from .parameter import Parameter
from .named_parameter import NamedParameter

class Operation(Parameter):
    """ Operation class.

    Represents an operation to be performed within a process. Can exists
    by itself, have parallel operations as parameters, or even build a
    dependency tree of operations.
    """
    def __init__(self, identifier, **kwargs):
        """ Operation init. """
        super(Operation, self).__init__(kwargs.get('name', None))

        self._identifier = identifier
        self._domain = None
        self._input = []
        self._parameters = []

    @classmethod
    def from_dict(cls, data):
        """ Creates a shell for an operation using Parameters. """
        expected = ('name', 'input', 'result', 'domain')

        identifier = data['name']

        name = None

        if 'result' in data:
            name = data['result']

        obj = cls(identifier, name=name)

        for input_data in data['input']:
            obj.add_input(Parameter(input_data))

        obj.domain = Parameter(data['domain'])

        extra_keys = [key for key in data.keys() if key not in expected]

        for key in extra_keys:
            obj.add_parameter(NamedParameter(key, data[key]))

        return obj

    @property
    def identifier(self):
        """ Operation identifer. """
        return self._identifier

    def _domain(self, value):
        """ Domain setter. """
        self._domain = value

    domain = property(None, _domain)

    def add_input(self, input_param):
        """ Adds input to operation. """
        self._input.append(input_param)

    def add_parameter(self, param):
        """ Adds a parameter to operation. """
        self._parameters.append(param)

    def parameterize(self):
        """ Parameterizes the operation. """
        params = {
            'name': self._identifier,
            'input': [param.name for param in self._input],
            'result': self.name,
        }

        if self._domain:
            params['domain'] = self._domain.name

        if len(self._parameters):
            for param in self._parameters:
                if isinstance(param, NamedParameter):
                    params[param.name] = '|'.join(param.values)
                else:
                    params[param.name] = param.name

        return params
