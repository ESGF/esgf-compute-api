"""
Operation Module.
"""

from uuid import uuid4

from .parameter import Parameter
from .named_parameter import NamedParameter

class DuplicateParameterError(Exception):
    """ Duplicate Parameter Error

    Raised when a duplicate parameter is present in current Operation or
    if a circular dependency is found.
    """
    pass

class Operation(Parameter):
    """ Operation class.

    Represents an operation to be performed within a process. Can exists
    by itself, have parallel operations as parameters, or even build a
    dependency tree of operations.
    """
    def __init__(self, module, kernel, parameters=None, var_name=None):
        """ Operation init. """
        super(Operation, self).__init__('%s.%s' % (module, kernel))

        self.resolved = False

        self._parameters = []

        if parameters:
            for param in parameters:
                self.add_parameter(param)

        if not var_name:
            var_name = str(uuid4())

        self._var_name = var_name

    @property
    def parameters(self):
        """ Read-only parameters. """
        return self._parameters

    @property
    def var_name(self):
        """ Read-only var_name. """
        return self._var_name

    def parameterize(self):
        """ Wrapper method to add extra parameter to method. """
        return self.process()

    def process(self, root=True):
        """ Overriden parent method. """
        ops_length = len(self.filter_operations())

        if ops_length == 0:
            args = self._build_arguments()
        elif ops_length == len(self._parameters):
            args = self._build_operations(root)
        else:
            args = self._build_mixed_params()

        return args

    def add_parameter(self, parameter):
        """ Adds a parameter to an operation. """
        if parameter in self._parameters:
            raise DuplicateParameterError('Parameter already exists.')

        if isinstance(parameter, Operation):
            operations = parameter.filter_operations()

            if self in operations:
                raise DuplicateParameterError('Circular dependency.')

        self._parameters.append(parameter)

    def _build_mixed_params(self):
        """
        Builds an argument string for an operation containing mixed parameter
        types. Can have parameters, named parameters and operations which are
        represented by their var_name.
        """
        params = tuple(x.name for x in self._filter_params())
        params_ops = tuple(x.var_name for x in self.filter_operations())
        named_params = tuple(x.parameterize() for x in self._filter_named_params())

        return ', '.join(params + params_ops + named_params)

    def _build_operations(self, root):
        """
        Builds an argument string for an operation containing only other
        operations. Each operation is presented as *name*(...args...) and
        concatenated to a list. We track already resolved operations to prevent
        duplicate entries.
        """
        dependencies = ()

        # Builds an ordered dependency list of all child operations
        for param in self.filter_operations():
            dependencies += param.resolve_dependencies()

        operation_list = []

        for operation in dependencies:
            if not operation.resolved:
                op_var_name = ''

                if operation.var_name:
                    op_var_name = operation.var_name + ':'

                op_str = '%s%s(%s)' % (
                    op_var_name,
                    operation.name,
                    operation.process(False))

                operation.resolved = True

                operation_list.append(op_str)
            elif operation.resolved and not root:
                op_str = operation.var_name if operation.var_name else 'fixme'

                operation_list.append(op_str)

        return ', '.join(operation_list)

    def resolve_dependencies(self):
        """ Builds ordered dependency list. """
        operations = self.filter_operations()

        if len(operations) == 0:
            return (self,)

        resolved = ()

        for param in operations:
            resolved += param.resolve_dependencies()

        return resolved + (self,)

    def _build_arguments(self):
        """
        Builds an argument string for an operation containing only parameters
        and named parameters that are concatenated together.
        """
        params = tuple(x.name for x in self._filter_params())
        named_params = tuple(x.parameterize() for x in self._filter_named_params())

        return ', '.join(params + named_params)

    def _filter_params(self):
        """ Filters parameters that are not named or operations. """
        return [x for x in self._parameters
                if not isinstance(x, NamedParameter)
                and not isinstance(x, Operation)]

    def _filter_named_params(self):
        """ Filters named parameters only. """
        return [x for x in self._parameters if isinstance(x, NamedParameter)]

    def filter_operations(self):
        """ Filters operation parameters only. """
        return [x for x in self._parameters if isinstance(x, Operation)]
