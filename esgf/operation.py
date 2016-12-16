"""
Operation Module.
"""

import json
from tempfile import NamedTemporaryFile

from esgf import domain
from esgf import gridder
from esgf import named_parameter
from esgf import parameter
from esgf import variable

class Operation(parameter.Parameter):
    """ Operation.

    Describes an operation supported by the WPS server.

    >>> averager = Operation(
        'averager',
        domain = Domain([
            Dimension(90, -90, Dimension.values, name='lat'),
            Dimension(90, -90, Dimesnion.values, name='lon'),
        ]),
        inputs = [
            Variable('http://thredds/tas.nc', 'tas', name='tas'),
        ],
        parameters = [
            NamedParameter('axes', 'longitude', 'latitude'), 
        ])

    Attributes:
        identifier: A String identifer of the operation.
        domain: A Domain to be used by the operation.
        inputs: A List of inputs to the operation, can be a Variable or another 
        operation.
        parameters: A List of additional parameters to be passed to the
        operation.
        name: Custom name to be referenced by other operations.
    """
    def __init__(self, identifier, inputs=None, parameters=None, domain=None, name=None, **kwargs):
        """ Operation init. """
        super(Operation, self).__init__(name)

        if not inputs:
            inputs = []

        if not parameters:
            parameters = {}
        # Build dict from list of NamedParamters
        elif isinstance(parameters, (list, tuple)):
            parameters = dict((x.name, x) for x in parameters)

        # Any kwargs are treated like parameters
        for k, w in kwargs.iteritems():
            if isinstance(w, parameter.Parameter):
                parameters[k] = w
            else:
                parameters[k] = named_parameter.NamedParameter(k, w)

        self.domain = domain
        self.inputs = inputs
        self.parameters = parameters

        self._identifier = identifier
        self._result = None

    @classmethod
    def from_dict(cls, data):
        """ Creates a shell for an operation using Parameters. """
        expected = ('name', 'input', 'result', 'domain')

        identifier = data['name']

        name = None

        if 'result' in data:
            name = data['result']

        obj = cls(identifier, name=name)

        for input_data in data.get('input', []):
            obj.add_input(parameter.Parameter(input_data))

        if 'domain' in data:
            obj.domain = parameter.Parameter(data['domain'])

        extra_keys = [key for key in data.keys() if key not in expected]

        for key in extra_keys:
            if 'gridder' == key:
                obj.add_parameter(gridder.Gridder.from_dict(data[key]))
            else:
                obj.add_parameter(
                    named_parameter.NamedParameter.from_string(key, data[key]))

        return obj

    @property
    def identifier(self):
        """ Operation identifier """
        return self._identifier

    def _set_result(self, value):
        self._result = value

    result = property(None, _set_result)

    def add_input(self, input_param):
        """ Adds input to operation. """
        self.inputs.append(input_param)

    def add_parameter(self, param):
        """ Adds a parameter to operation. """
        self.parameters[param.name] = param

    @property
    def variables(self):
        return [x for x in self.inputs if isinstance(x, variable.Variable)]

    @property
    def output(self):
        """ Operation output. """
        if self._result.status != 'ProcessSucceeded':
            raise errors.WPSServerError(
                'Process has no output, possibly process execution error.')

        return self._result.output

    def gather(self):
        """ Gathers variables and domains. """
        var_dict = {}
        dom_dict = {}

        for inp in self.inputs:
            if isinstance(inp, Operation):
                op_var, op_dom = inp.gather()

                for k, v in op_var.iteritems():
                    var_dict[k] = v

                for k, v in op_dom.iteritems():
                    dom_dict[k] = v

        if self.variables:
            for var in self.variables:
                var_dict[var.name] = var

                if var.domains:
                    for dom in var.domains:
                        if dom.name not in dom_dict:
                            dom_dict[dom.name] = dom

        if self.domain:
            dom_dict[self.domain.name] = self.domain

        if self.parameters:
            for name, param in self.parameters.iteritems():
                if isinstance(param, gridder.Gridder):
                    if isinstance(param.grid, variable.Variable):
                        var_dict[param.grid.name] = param.grid
                    elif isinstance(param.grid, domain.Domain):
                        dom_dict[param.grid.name] = param.grid

        return var_dict, dom_dict

    def flatten(self, root=True):
        """ Flattens operation tree. """
        operations = []

        if root:
            operations.append(self.parameterize())

        # Recursively call flatten on child operations.
        for inp in self.inputs:
            if isinstance(inp, Operation):
                op_flat = inp.flatten(False)

                operations.extend(op_flat)

        return operations

    def parameterize(self):
        """ Parameterizes the operation. """
        params = {}
        params['name'] = self._identifier
        params['input'] = [param.name for param in self.inputs]
        params['result'] = self.name

        if self.domain:
            params['domain'] = self.domain.name

        if len(self.parameters):
            for name, param in self.parameters.iteritems():
                params[name] = param.parameterize()

        return params

    def __repr__(self):
        return ('Operation(identifier=%r, inputs=%r, name=%r, domain=%r, '
                'parameters=%r)' % (self._identifier, self.inputs, self.name, 
                                    self.domain, self.parameters))

    def __str__(self):
        return 'identifier=%s inputs=%s name=%s domain=%s parameters=%s' % (
            self._identifier, self.inputs, self.name, self.domain,
            self.parameters)
