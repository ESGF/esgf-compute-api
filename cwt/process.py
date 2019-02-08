"""
Process Module.
"""

import json
import logging 
import time
import datetime
import warnings

from cwt.errors import CWTError
from cwt.errors import MissingRequiredKeyError
from cwt.errors import WPSTimeoutError
from cwt.named_parameter import NamedParameter
from cwt.parameter import Parameter
from cwt.variable import Variable

logger = logging.getLogger('cwt.process')

def input_output_to_dict(value):
    data = value.__dict__

    data['metadata'] = [x.__dict__ for x in data['metadata']]

    # Included from ComplexData
    try:
        data['defaultValue'] = data['defaultValue'].__dict__
    except KeyError:
        pass

    try:
        data['supportedValues'] = [x.__dict__ for x in data['supportedValues']]
    except KeyError:
        pass

    return data

class StatusTracker(object):
    def __init__(self, stale_threshold):
        self.history = {}
        self.start = None
        self.stale = 0
        self.stale_threshold = stale_threshold

    @property
    def elapsed(self):
        elapsed = datetime.datetime.now() - self.start

        return elapsed.total_seconds()

    def update(self, message):
        now = datetime.datetime.now()

        if self.start is None:
            self.start = now

        if message in self.history:
            self.stale += 1

            if self.stale >= self.stale_threshold:
                raise CWTError('Timing out due to staleness, no new message {!r} queries', self.stale)
        else:
            self.history[message] = now

        print message

        logger.info(message)

class Process(Parameter):
    """ A WPS Process

    Wraps a WPS Process.

    Arguments:
        process: A DescribeProcessResponse object.
        name: A string name for the process to be used as the input of another process.
    """
    def __init__(self, process=None, name=None):
        super(Process, self).__init__(name)

        self.process = process

        self.context = None

        self.processed = False

        self.inputs = []

        self.parameters = {}

        self.domain = None

        self.status_tracker = None

        self._identifier = None
        self._title = None
        self._process_outputs = None
        self._data_inputs = None
        self._status_supported = None
        self._store_supported = None
        self._process_version = None
        self._abstract = None
        self._metadata = None

    def __repr__(self):
        return ('Process(identifier={!r}, title={!r}, status_supported={!r}, '
                'store_supported={!r}, process_version={!r}, abstract={!r}, '
                'metadata={!r})').format(self.identifier, self.title, self.status_supported,
                                        self.store_supported, self.process_version,
                                        self.abstract, self.metadata)

    @classmethod
    def from_owslib(cls, process):
        obj = cls(process)

        obj._identifier = process.identifier

        obj._title = process.title

        obj._process_outputs = [input_output_to_dict(x) 
                                for x in process.processOutputs]

        obj._data_inputs = [input_output_to_dict(x)
                            for x in process.dataInputs]

        obj._status_supported = process.statusSupported

        obj._store_supported = process.storeSupported

        obj._process_version = process.processVersion

        obj._abstract = process.abstract

        obj._metadata = [x.__dict__ for x in process.metadata]

        return obj

    @classmethod
    def from_dict(cls, data):
        """ Attempts to load a process from a dict. """
        obj = cls()

        try:
            obj._identifier = data['name']

            obj.name = data['result']

            obj.inputs = data['input']

            obj.domain = data['domain']
        except KeyError as e:
            raise MissingRequiredKeyError(e)

        ignore = ('name', 'input', 'result', 'domain')

        for name, value in data.iteritems():
            if name not in ignore:
                if name == 'gridder':
                    obj.parameters[name] = Gridder.from_dict(value)
                else:
                    obj.parameters[name] = NamedParameter.from_string(name, value)

        return obj

    @property
    def identifier(self):
        return self._identifier

    @property
    def title(self):
        return self._title

    @property
    def process_outputs(self):
        return self._process_outputs

    @property
    def data_inputs(self):
        return self._data_inputs

    @property
    def status_supported(self):
        return self._status_supported

    @property
    def store_supported(self):
        return self._store_supported

    @property
    def process_version(self):
        return self._process_version

    @property
    def abstract(self):
        return self._abstract

    @property
    def metadata(self):
        return self._metadata

    @property
    def processing(self):
        """ Checks if the process is still working.

        This will update the wrapper with the latest status and return
        True if the process is waiting or running.

        Returns:
            A boolean denoting whether the process is still working.
        """
        self.context.checkStatus(sleepSecs=0)

        return self.accepted or self.started

    @property
    def exception_dict(self):
        if self.errored:
            return [x.__dict__ for x in self.context.errors]

        return None

    @property
    def accepted(self):
        return self.check_context_status('ProcessAccepted')

    @property
    def started(self):
        return self.check_context_status('ProcessStarted')

    @property
    def paused(self):
        return self.check_context_status('ProcessPaused')

    @property
    def failed(self):
        return self.check_context_status('ProcessFailed')

    @property
    def succeeded(self):
        return self.check_context_status('ProcessSucceeded')

    @property
    def errored(self):
        return self.check_context_status('Exception')

    @property
    def output(self):
        """ Return the output of the process if done. """
        if not self.succeeded:
            raise CWTError('No output available process has not succeeded')

        # CWT only expects a single output in json format
        data = json.loads(self.context.processOutputs[0].data[0])

        if 'uri' in data:
            output_data = Variable.from_dict(data)
        elif 'outputs' in data:
            output_data = [Variable.from_dict(x) for x in data['outputs']]
        else:
            output_data = data

        return output_data

    @property
    def status(self):
        msg = None

        if self.accepted:
            msg = 'ProcessAccepted {!s}'.format(self.context.statusMessage)
        elif self.started:
            msg = 'ProcessStarted {!s} {!s}'.format(self.context.statusMessage, 
                                                    self.context.percentCompleted)
        elif self.paused:
            msg = 'ProcessPaused {!s} {!s}'.format(self.context.statusMessage,
                                                   self.context.percentCompleted)
        elif self.failed:
            msg = 'ProcessFailed {!s}'.format(self.context.statusMessage)
        elif self.succeeded:
            msg = 'ProcessSucceeded {!s}'.format(self.context.statusMessage)
        elif self.errored:
            exception_msg = '->'.join([x['text'] for x in self.exception_dict])

            msg = 'Exception {!s}'.format(exception_msg)
        else:
            msg = 'Status unavailable'

        return msg

    def check_context_status(self, value):
        try:
            return self.context.status == value
        except AttributeError:
            raise CWTError('Process is missing a context')

    def wait(self, stale_threshold=None, timeout=None, sleep=None):
        if stale_threshold is None:
            stale_threshold = 4

        self.status_tracker = StatusTracker(stale_threshold)

        if sleep is None:
            sleep = 1.0

        self.status_tracker.update(self.status)

        while self.processing:
            self.status_tracker.update(self.status)

            time.sleep(sleep)

            if timeout is not None and self.status_tracker.elapsed > timeout:
                raise WPSTimeoutError(self.status_tracker.elapsed)

        self.status_tracker.update(self.status)

        return self.succeeded
        
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
            raise CWTError('Parameter {} is required but not present', name)

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
            if not isinstance(a, NamedParameter):
                raise CWTError('Invalid parameter type "{}", should be a NamedParameter', type(a))

            self.parameters[a.name] = a

        for name, value in kwargs.iteritems():
            if not isinstance(value, (list, tuple)):
                value = [value]

            self.parameters[name] = NamedParameter(name, *value)

    def add_inputs(self, *args):
        """ Set the inputs of the Process. 
        
        Args:
            args: A list of Process/Variable objects.
        """
        self.inputs.extend(args)

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
                           if isinstance(x, Variable)))

        for p in new_processes:
            p.collect_input_processes(processes, inputs)

        processes.extend(new_processes)

        return processes, inputs.values()

    def to_dict(self):
        """ Returns a dictionary representation."""
        data = {
            'name': self.identifier,
            'result': self.name
        }

        if self.domain is not None:
            try:
                data['domain'] = self.domain.name
            except AttributeError:
                data['domain'] = self.domain

        inputs = []

        for i in self.inputs:
            try:
                inputs.append(i.name)
            except AttributeError:
                inputs.append(i)

        data['input'] = inputs

        for name, value in self.parameters.iteritems():
            data.update(value.to_dict())

        return data

    def parameterize(self):
        """ Create a dictionary representation of the Process. """
        warnings.warn('parameterize is deprecated, use to_dict instead',
                      DeprecationWarning)

        return self.to_dict()
