"""
Process Module.
"""

import json
import logging

import requests

from cwt import parameter
from cwt import named_parameter
from cwt import variable
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger(__name__)

__all__ = ['ProcessError', 'Process']

class ProcessError(Exception):
    pass

class Process(parameter.Parameter):
    def __init__(self, process, name=None):
        super(Process, self).__init__(name)

        self.__process = process
        self.__identifier = None
        self.__response = None

        self.response = None
        self.processed = False
        self.inputs = []
        self.parameters = {}
        self.domain = None

    @classmethod
    def from_dict(cls, data):
        obj = cls(None, data.get('result'))

        obj.inputs = data.get('input', [])

        obj.identifier = data.get('name')

        obj.domain = data.get('domain')

        known_keys = ('name', 'input', 'result')

        proc_params = {}

        for key in data.keys():
            if key not in known_keys:
                proc_params[key] = named_parameter.NamedParameter.from_string(key, data.get(key))

        obj.parameters = proc_params

        return obj

    def __getattr__(self, name):
        if hasattr(self.__process, name):
            return getattr(self.__process, name)

        if hasattr(self.response, name):
            return getattr(self.response, name)
        
        raise AttributeError(name)

    def __get_identifier(self):
        return self.__process.identifier if self.__process is not None else self.__identifier

    def __set_identifier(self, value):
        self.__identifier = value

    identifier = property(__get_identifier, __set_identifier)

    @property
    def processing(self):
        self.update_status()

        return self.status.__class__ in (metadata.ProcessAccepted, metadata.ProcessStarted)

    @property
    def error(self):
        return True if (self.response is None or
                        (self.response is not None and
                         isinstance(self.status, metadata.ProcessFailed))) else False

    @property
    def output(self):
        if self.__response is None:
            return None

        if self.__response.output is None or len(self.__response.output) == 0:
            return None

        data = json.loads(self.__response.output[0].data.value)

        var = variable.Variable.from_dict(data)

        return var

    def add_parameters(self, *args, **kwargs):
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
        self.inputs.extend(args)

    def resolve_inputs(self, inputs, operations):
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

    def update_status(self):
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
            for _, p in self.parameters.iteritems():
                params.update(p.parameterize())

        return params
