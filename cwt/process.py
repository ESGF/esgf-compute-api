"""
Process Module.
"""

import json
import logging 
import time
import datetime

import requests

import cwt
from cwt.wps import wps

logger = logging.getLogger('cwt.process')

__all__ = ['ProcessError', 'Process']

class ProcessError(cwt.CWTError):
    pass

class ValidationError(cwt.CWTError):
    def __init__(self, fmt, *args):
        self.msg = fmt.format(*args)

    def __str__(self):
        return self.msg

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

        self.description = None

        self.response = None

        self.processed = False

        self.inputs = []

        self.parameters = {}

        self.domain = None

        self.__client = None

    def __repr__(self):
        return 'Process(identifier=%r, name=%r, num_inputs=%r)' % (
            self.identifier,
            self.name,
            len(self.inputs))

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
    def title(self):
        try:
            return self.binding.Title.value()
        except AttributeError:
            raise ProcessError('Binding has not been set')

    @property
    def version(self):
        try:
            return self.binding.processVersion
        except AttributeError:
            raise ProcessError('Binding has not been set')

    @property
    def abstract(self):
        try:
            return self.description.abstract
        except AttributeError:
            raise ProcessError('Abstract is not available')

    @property
    def metadata(self):
        try:
            return self.description.metadata
        except AttributeError:
            raise ProcessError('Metadata is not available')

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
    def has_status(self):
        return (self.response is not None and
                self.response.Status is not None)

    @property
    def accepted(self):
        return (self.has_status and
                self.response.Status.ProcessAccepted is not None)

    @property
    def started(self):
        return (self.has_status and
                self.response.Status.ProcessStarted is not None)

    @property
    def paused(self):
        return (self.has_status and
                self.response.Status.ProcessPaused is not None)

    @property
    def failed(self):
        return (self.has_status and
                self.response.Status.ProcessFailed is not None)

    @property
    def succeeded(self):
        return (self.has_status and
                self.response.Status.ProcessSucceeded is not None)

    @property
    def output(self):
        """ Return the output of the process if done. """
        if (self.response is None or
                self.response.ProcessOutputs is None or
                len(self.response.ProcessOutputs.Output) == 0):
            return None

        data = json.loads(
            self.response.ProcessOutputs.Output[0].Data.ComplexData.orderedContent()[0].value)

        if 'uri' in data:
            output_data = cwt.Variable.from_dict(data)
        elif 'outputs' in data:
            output_data = [cwt.Variable.from_dict(x) for x in data['outputs']]
        else:
            output_data = data

        return output_data

    @property
    def status(self):
        if self.response is not None and self.response.Status is not None:
            if self.response.Status.ProcessAccepted is not None:
                return 'ProcessAccepted {}'.format(self.response.Status.ProcessAccepted)
            elif self.response.Status.ProcessStarted is not None:
                message = self.response.Status.ProcessStarted.value()

                percent = self.response.Status.ProcessStarted.percentCompleted

                return 'ProcessStarted {} {}'.format(message, percent)
            elif self.response.Status.ProcessPaused is not None:
                message = self.response.Status.ProcessPaused.value()

                percent = self.response.Status.ProcessPaused.percentCompleted

                return 'ProcessStarted {} {}'.format(message, percent)
            elif self.response.Status.ProcessFailed is not None:
                raise cwt.WPSError('ProcessFailed {}'.format(self.exception_message))
            elif self.response.Status.ProcessSucceeded is not None:
                return 'ProcessSucceeded {}'.format(self.response.Status.ProcessSucceeded)

        return 'No Status'

    def wait(self, stale_threshold=4):
        status_hist = {}

        stale_count = 0

        last_update = None

        def update_history(status):
            global stale_count

            if status not in status_hist:
                status_hist[status] = True

                print status

                stale_count = 0

                last_update = datetime.datetime.now()
            else:
                stale_count += 1

                if stale_count > stale_threshold:
                    raise cwt.WPSError('Job appears to be stale no update since {!s}', last_update)

        update_history(self.status)

        while self.processing:
            update_history(self.status)

            time.sleep(1)

        update_history(self.status)

        return True if self.succeeded else False

    def validate(self):
        input_limit = None

        if self.metadata is None:
            return

        if 'inputs' in self.metadata:
            if self.metadata['inputs'] != '*':
                input_limit = int(self.metadata['inputs'])

        if input_limit is not None and len(self.inputs) > input_limit:
            raise ValidationError('Invalid number of inputs, expected "{}", got "{}"', input_limit, len(self.inputs))
        
    def set_client(self, client):
        self.__client = client

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
                v = [v]

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

        response = self.__client.http_request('GET', self.response.statusLocation, {}, {}, {})

        self.response = wps.CreateFromDocument(response)

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
