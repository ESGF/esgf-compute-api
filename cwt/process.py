"""
Process Module.
"""

import json
import logging

import requests

from cwt import parameter
from cwt import named_parameter
from cwt import variable
from cwt import gridder
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger('cwt.process')

__all__ = ['ProcessError', 'Process']

class ProcessError(Exception):
    pass

class Process(parameter.Parameter):
    """ A WPS Process

    Wraps a WPS Process.

    Arguments:
        process: A DescribeProcessResponse object.
        name: A string name for the process to be used as the input of another process.
    """
    def __init__(self, identifier=None, process=None, name=None):
        super(Process, self).__init__(name)

        self.__process = process
        self.__identifier = identifier

        self.response = None
        self.processed = False
        self.inputs = []
        self.parameters = {}
        self.domain = None
        self.hrefs = {}

    @classmethod
    def from_dict(cls, data):
        """ Attempts to load a process from a dict. """
        obj = cls(data.get('name'), None, data.get('result'))

        obj.inputs = data.get('input', [])

        obj.domain = data.get('domain')

        known_keys = ('name', 'input', 'result')

        proc_params = {}

        for key in data.keys():
            if key not in known_keys:
                d = data.get(key)

                if isinstance(d, (dict)):
                    if key == 'gridder':
                        proc_params[key] = gridder.Gridder.from_dict(d)
                else:
                    proc_params[key] = named_parameter.NamedParameter.from_string(key, d)

        obj.parameters = proc_params

        return obj

    def __getattr__(self, name):
        """ Fallthrough attribute lookup.

        If the attribute is not contained in the current object then we search
        the __process and response objects.

        """
        if hasattr(self.__process, name):
            return getattr(self.__process, name)

        if hasattr(self.response, name):
            return getattr(self.response, name)
        
        raise AttributeError(name)

    def __get_identifier(self):
        """ Returns the processes identifier. """
        return self.__process.identifier if self.__process is not None else self.__identifier

    def __set_identifier(self, value):
        """ Sets the processes identifier. """
        self.__identifier = value

    identifier = property(__get_identifier, __set_identifier)

    @property
    def processing(self):
        """ Checks if the process is still working.

        This will update the wrapper with the latest status and return
        True if the process is waiting or running.

        Returns:
            A boolean denoting whether the process is still working.
        """
        self.update_status()

        return self.status.__class__ in (metadata.ProcessAccepted, metadata.ProcessStarted)

    @property
    def error(self):
        """ Check if the process has errored. """
        return True if (self.response is None or
                        (self.response is not None and
                         isinstance(self.status, metadata.ProcessFailed))) else False

    @property
    def output(self):
        """ Return the output of the process if done. """
        if self.response is None:
            return None

        if self.response.output is None or len(self.response.output) == 0:
            return None

        data = json.loads(self.response.output[0].data.value)

        var = variable.Variable.from_dict(data)

        return var

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
            raise Exception('The parameter {} is not present and is required.'.format(name))

        if name in self.parameters:
            return self.parameters[name]

        return None

    def add_parameters(self, *args, **kwargs):
        """ Add a parameter.

        kwargs can contain two formats.

        k=v where v is a NamedParameter
        k=v where v is a string in the format of 'x|y|z'
        
        Args:
            args: A list of NamedParameter objects.
            kwargs: A dict of NamedParameter objects or k=v where k is the name and v is string.
        """
        for a in args:
            if isinstance(a, named_parameter.NamedParameter):
                self.parameters[a.name] = a
            else:
                raise ProcessError('Cannot add parameter of type {}'.format(type(a)))

        for k, v in kwargs.iteritems():
            if isinstance(v, (list, tuple)):
                self.parameters[k] = named_parameter.NamedParameter(k, *v)
            elif isinstance(v, str):
                self.parameters[k] = cwt.NamedParameter.from_string(k, v)
            else:
                raise ProcessError('Cannot add parameter of type {}'.format(type(v)))

    def set_inputs(self, *args):
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
                raise ProcessError('Input "{}" not found'.format(key))

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
                           if isinstance(x, variable.Variable)))

        for p in new_processes:
            p.collect_input_processes(processes, inputs)

        processes.extend(new_processes)

        return processes, inputs.values()


    def download_result(self):
        status_href = self.hrefs.get("status")


    def update_status(self):
        """ Retrieves the latest process status. """
        if self.response is None or self.status_location is None:
            raise ProcessError('Process does not support status updates')

        try:
            response = requests.get(self.status_location)
        except requests.RequestException:
            logger.exception('Error retrieving job status')

            raise ProcessError('Error retrieving job status')

        self.response = operations.ExecuteResponse.from_xml(response.text)

        if isinstance(self.status, metadata.ProcessFailed):
            raise ProcessError('Process failed with exception report:\n{}'
                               .format(str(self.status.exception_report)))

    def parameterize(self):
        """ Create a dictionary representation of the Process. """
        params = {
            'name': self.identifier,
            'result': self.name
        }

        if self.domain is not None:
            if isinstance(self.domain, (str, unicode)):
                params['domain'] = self.domain
            else:
                params['domain'] = self.domain.name

        inputs = []

        for i in self.inputs:
            if isinstance(i, (str, unicode)):
                inputs.append(i)
            else:
                inputs.append(i.name)

        params['input'] = inputs

        if self.parameters is not None:
            for k, p in self.parameters.iteritems():
                params[k] = p.parameterize()

        return params
