"""
Process Module.
"""

import logging

import requests

from cwt import parameter
from cwt import named_parameter
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger(__name__)

class ProcessError(Exception):
    pass

class Process(parameter.Parameter):
    def __init__(self, process, name=None):
        super(Process, self).__init__(name)

        self.__process = process
        self.__response = None
        self.__params = {}

        self.inputs = []

    @classmethod
    def from_dict(cls, data, inputs):
        obj = cls(None, data.get('result'))

        proc_inputs = []
            
        for i in data.get('input', []):
            if i not in inputs:
                raise ProcessError('Input "{}" is not present in the input dictionary'.format(i))

            proc_inputs.append(inputs[i])

        obj.inputs = proc_inputs

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
            'name': self.__process.identifier,
            'input': [x.name for x in self.inputs],
            'result': self.name
        }

        if self.__params is not None:
            for _, p in self.__params.iteritems():
                params.update(p.parameterize())

        return params
