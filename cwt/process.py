"""
Process Module.
"""

import logging

import requests

from cwt import parameter
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
        self.__inputs = None
        self.__params = None

    def __getattr__(self, name):
        if hasattr(self.__process, name):
            return getattr(self.__process, name)

        if hasattr(self.__response, name):
            return getattr(self.__response, name)
        
        raise AttributeError(name)

    def __set_inputs(self, inputs):
        self.__inputs = [x.name for x in inputs]

    inputs = property(None, __set_inputs)

    def __set_parameters(self, params):
        self.__params = [x.parameterize() for x in params]

    parameters = property(None, __set_parameters)

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
                'input': self.__inputs,
                'result': self.name
                }

        if self.__params is not None:
            for p in self.__params:
                params.update(p)

        return params

#if __name__ == '__main__':
#    import wps
#
#    w = wps.WPS('http://0.0.0.0:8000/wps')
#
#    p = w.get_process('CDSpark.min')
#
#    import variable
#
#    tas = variable.Variable('file:///data/tas_6h.nc', 'tas')
#
#    w.execute(p, inputs=[tas], axes=['x', 'y'])
#
#    import time
#
#    print 'STARTED', p.status
#
#    while p.processing:
#        print 'Processing'
#
#        time.sleep(1)
#
#    print 'DONE', p.status
