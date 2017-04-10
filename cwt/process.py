"""
Process Module.
"""

import logging

import requests

from cwt import parameter
from cwt import named_parameter
from cwt import variable
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger(__name__)

class ProcessError(Exception):
    pass

class Process(parameter.Parameter):
    def __init__(self, process, name=None):
        super(Process, self).__init__(name)

        self.__process = process
        self.__identifier = None
        self.__response = None
        self.__params = {}

        self.processed = False
        self.inputs = []

    @classmethod
    def from_dict(cls, data):
        obj = cls(None, data.get('result'))

        obj.inputs = data.get('input', [])

        obj.identifier = data.get('name')

        known_keys = ('name', 'input', 'result')

        proc_params = []

        for key in data.keys():
            if key not in known_keys:
                proc_params.append(named_parameter.NamedParameter(key, *data[key].split('|')))

        obj.parameters = proc_params

        return obj

    def __getattr__(self, name):
        if hasattr(self.__process, name):
            return getattr(self.__process, name)

        if hasattr(self.__response, name):
            return getattr(self.__response, name)
        
        raise AttributeError(name)

    def __get_identifier(self):
        return self.__process.identifier if self.__process is not None else self.__identifier

    def __set_identifier(self, value):
        self.__identifier = value

    identifier = property(__get_identifier, __set_identifier)

    def __get_parameters(self):
        return self.__params.values()

    def __set_parameters(self, params):
        self.__params = dict((x.name, x) for x in params)

    parameters = property(__get_parameters, __set_parameters)

    def __set_response(self, response):
        self.__response = response

    def __get_response(self):
        return self.__response

    response = property(__get_response, __set_response)

    @property
    def processing(self):
        self.update_status()

        return self.status.__class__ in (metadata.ProcessAccepted, metadata.ProcessStarted)

    @property
    def error(self):
        return True if (self.__response is not None and
                isinstance(self.status, metadata.ProcessFailed)) else False

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
            inputs = []

        new_processes = [x for x in self.inputs if isinstance(x, Process)]

        inputs.extend([x for x in self.inputs if isinstance(x, variable.Variable)])

        for p in new_processes:
            p.collect_input_processes(processes, inputs)

        processes.extend(new_processes)

        return processes, inputs

    def update_status(self):
        if self.__response is None or self.status_location is None:
            raise ProcessError('Process does not support status updates')

        try:
            response = requests.get(self.status_location)
        except requests.RequestException:
            logger.exception('Error retrieving job status')

            raise ProcessError('Error retrieving job status')

        self.__response = operations.ExecuteResponse.from_xml(response.text)

        if isinstance(self.status, metadata.ProcessFailed):
            raise ProcessError('Process failed with exception report:\n{}'
                               .format(str(self.status.exception_report)))

    def parameterize(self):
        params = {
            'name': self.identifier,
            'input': [x.name for x in self.inputs],
            'result': self.name
        }

        if self.__params is not None:
            for _, p in self.__params.iteritems():
                params.update(p.parameterize())

        return params
