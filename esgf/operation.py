"""
Operation Module.
"""

from uuid import uuid4

from .variable import Variable
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

        self.domain = None
        self.input = []
        self.parameters = []

        self._identifier = identifier

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

    def add_input(self, input_param):
        """ Adds input to operation. """
        self.input.append(input_param)

    def add_parameter(self, param):
        """ Adds a parameter to operation. """
        self.parameters.append(param)

    def variables(self):
        return [x for x in self.input if isinstance(x, Variable)]

    def gather(self):
        """ Gathers variables and domains. """
        var_dict = {}
        dom_dict = {}

        for param in self.parameters:
            for var in param.variables():
                var_dict[var.name] = var

            dom_dict[param.domain.name] = param.domain

        for var in self.variables():
            var_dict[var.name] = var

        if self.domain:
            dom_dict[self.domain.name] = self.domain

        return var_dict.values(), dom_dict.values()

    def flatten(self):
        """ Flattens operation tree. """
        if not len(self.parameters):
            return [self.parameterize()]

        return [param.parameterize() for param in self.parameters]

    def parameterize(self):
        """ Parameterizes the operation. """
        params = {
            'name': self._identifier,
            'input': [param.name for param in self.input],
            'result': self.name,
        }

        if self.domain:
            params['domain'] = self.domain.name

        if len(self.parameters):
            for param in self.parameters:
                params[param.name] = '|'.join(param.values)

        return params
