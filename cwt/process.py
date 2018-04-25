"""
Process Module.
"""

import json
import logging

import requests

import cwt
from cwt.wps import wps

logger = logging.getLogger('cwt.process')

__all__ = ['ProcessError', 'Process']

class ProcessError(cwt.CWTError):
    pass

class Process(cwt.Parameter):
    """ A WPS Process

    Wraps a WPS Process.

    Arguments:
        process: A DescribeProcessResponse object.
        name: A string name for the process to be used as the input of another process.
    """
    def __init__(self, identifier=None, binding=None, name=None):
        super(Process, self).__init__(name)

        self.__identifier = identifier

        self.binding = binding

        self.response = None

        self.processed = False

        self.inputs = []

        self.parameters = {}

        self.domain = None

    @classmethod
    def from_identifier(cls, identifier):
        obj = cls(identifier=identifier)

        return obj

    @classmethod
    def from_binding(cls, binding):
        obj = cls(binding=binding)

        return obj

    @classmethod
    def from_dict(cls, data):
        """ Attempts to load a process from a dict. """
        obj = cls(data.get('name'), None, data.get('result'))

        obj.inputs = data.get('input', [])

        obj.domain = data.get('domain', None)

        known_keys = ('name', 'input', 'result')

        proc_params = {}

        for key in data.keys():
            if key not in known_keys:
                d = data.get(key)

                if isinstance(d, (dict)):
                    if key == 'gridder':
                        proc_params[key] = cwt.Gridder.from_dict(d)
                else:
                    proc_params[key] = cwt.NamedParameter.from_string(key, d)

        obj.parameters = proc_params

        return obj

    @property
    def identifier(self):
        if self.__identifier is not None:
            return self.__identifier

        if self.binding is not None:
            return self.binding.Identifier.value()

    @property
    def processing(self):
        """ Checks if the process is still working.

        This will update the wrapper with the latest status and return
        True if the process is waiting or running.

        Returns:
            A boolean denoting whether the process is still working.
        """
        self.update_status()

        return (self.response is not None and
                (self.response.Status.ProcessAccepted is not None or
                 self.response.Status.ProcessStarted is not None))

    @property
    def exception_message(self):
        exception = self.response.Status.ProcessFailed.ExceptionReport.Exception[0]

        return exception.ExceptionText[0]

    @property
    def is_failed(self):
        return self.response is not None and self.response.Status.ProcessFailed is not None

    @property
    def output(self):
        """ Return the output of the process if done. """
        if (self.response is None or
                self.response.ProcessOutputs is None or
                len(self.response.ProcessOutputs.Output) == 0):
            return None

        data = json.loads(self.response.ProcessOutputs.Output[0].Data.ComplexData.Data)

        var = cwt.Variable.from_dict(data)

        return var

    def set_domain(self, domain):
        self.domain = domain

    def get_parameter(self, name, required=False):
        """ Retrieves a parameter

        Args:
            name: A string name of the parameter.
            required: A boolean flag denoting whether the parameter is required.

        Returns:
            A NamedParameter object.

        Raises:
            Exception: The parameter is required and not present.
        """
        if name not in self.parameters and required:
            raise ProcessError('Parameter {} is required but not present', name)

        return self.parameters.get(name, None)

    def add_parameters(self, *args, **kwargs):
        """ Add a parameter.

        kwargs can contain two formats.

        k=v where v is a NamedParameter
        
        Args:
            args: A list of NamedParameter objects.
            kwargs: A dict of NamedParameter objects or k=v where k is the name and v is string.
        """
        for a in args:
            if not isinstance(a, cwt.NamedParameter):
                raise ProcessError('Invalid parameter type "{}", should be a cwt.NamedParameter', type(a))

            self.parameters[a.name] = a

        for k, v in kwargs.iteritems():
            if not isinstance(v, (tuple, list)):
                raise ProcessError('Invalid parameter argument type {}, should be a list or tuple', type(v))

            self.parameters[k] = cwt.NamedParameter(k, *v)

    def add_inputs(self, *args):
        """ Set the inputs of the Process. 
        
        Args:
            args: A list of Process/Variable objects.
        """
        self.inputs.extend(args)

    def resolve_inputs(self, inputs, operations):
        """ Attempts to resolve the process inputs.

        Resolves the processes inputs from strings to Process/Variable objects.

        Args:
            inputs: A dict of Variables where the key is name.
            operations: A dict of Processes where the key is name.

        """
        logger.info('Proccess {} resolving inputs {}'.format(self.identifier, self.inputs))

        temp = dict((x, None) for x in self.inputs)

        for key in temp.keys():
            if key in inputs:
                temp[key] = inputs[key]
            elif key in operations:
                if operations[key].processed:
                    raise ProcessError('Found circular loop in execution tree')

                temp[key] = operations[key]

                temp[key].processed = True

                temp[key].resolve_inputs(inputs, operations)
            else:
                raise ProcessError('Input "{}" not found', key)

        self.inputs = temp.values()

    def collect_input_processes(self, processes=None, inputs=None):
        """ Aggregates the process trees inputs.

        A DFS to collect the trees inputs into two lists, Operations and Variables.

        Args:
            processes: A list of current processes discovered.
            inputs: A list of Process/Variables to processes.

        Returns:
            A two lists, one of Processes and the other of Variables.
        """

        if processes is None:
            processes = []

        if inputs is None:
            inputs = {}

        new_processes = [x for x in self.inputs if isinstance(x, Process)]

        inputs.update(dict((x.name, x) for x in self.inputs
                           if isinstance(x, cwt.Variable)))

        for p in new_processes:
            p.collect_input_processes(processes, inputs)

        processes.extend(new_processes)

        return processes, inputs.values()

    def update_status(self):
        """ Retrieves the latest process status. """
        if self.response is None or self.response.statusLocation is None:
            return None

        try:
            response = requests.get(self.response.statusLocation)
        except requests.RequestException as e:
            raise cwt.WPSHttpError.from_request_response(e.response)

        self.response = wps.CreateFromDocument(response.text)

        if self.is_failed:
            raise cwt.WPSError('Process failed: {}'.format(self.exception_message))

    def parameterize(self):
        """ Create a dictionary representation of the Process. """
        params = {
            'name': self.identifier,
            'result': self.name
        }

        if self.domain is not None:
            params['domain'] = self.domain.name

        inputs = []

        for i in self.inputs:
            inputs.append(i.name)

        params['input'] = inputs

        if self.parameters is not None:
            for k, p in self.parameters.iteritems():
                params[k] = p.parameterize()

        return params
