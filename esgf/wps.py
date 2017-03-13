""" A WPS Client """

import sys
import json
import logging

import requests

from esgf import process
from esgf import named_parameter
from esgf.wps_lib import operations

logger = logging.getLogger()

class WPSHTTPError(Exception):
    pass

class WPS(object):
    def __init__(self, url, username=None, password=None, **kwargs):
        self.__url = url
        self.__username = username
        self.__password = password
        self.__version = kwargs.get('version')
        self.__language = kwargs.get('laanguage')
        self.__capabilities = None 

        if kwargs.get('log') is not None:
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            # TODO make level configurable
            logger.setLevel(logging.DEBUG)

            stream_handler = logging.StreamHandler(sys.stdout)

            stream_handler.setFormatter(formatter)

            logger.addHandler(stream_handler)

            log_file = kwargs.get('log_file')

            if log_file is not None:
                file_handler = logging.FileHandler(log_file)

                file_handler.setFormatter(formatter)

                logger.addHandler(file_handler)
    
    @property
    def capabilities(self):
        return self.__capabilities

    def __request(self, method, params=None, data=None):
        try:
            response = requests.request(method, self.__url, params=params, data=data)
        except requests.RequestException:
            logger.exception()

            raise WPSHTTPError('{0} request failed'.format(method))

        logger.debug('%s request succeeded', method)

        if response.status_code != 200:
            raise WPSHTTPError('{0} response failed with status code '
                    '{1}'.format(method, response.status_code))

        return response

    def __get_capabilities(self):
        params = {
                'service': 'WPS',
                'request': 'GetCapabilities',
                }

        if self.__version is not None:
            params['acceptversions'] = self.__version

        if self.__language is not None:
            params['language'] = self.__language

        response = self.__request('GET', params=params)

        capabilities = operations.GetCapabilitiesResponse.from_xml(response.text)

        return capabilities

    def processes(self, regex=None, refresh=False):
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities()

        return [process.Process(x) for x in self.__capabilities.process_offerings]

    def get_process(self, identifier):
        if self.__capabilities is None:
            self.__capabilities = self.__get_capabilities()

        try:
            return [process.Process(x) for x in self.__capabilities.process_offerings
                    if x.identifier == identifier][0]
        except IndexError:
            logger.debug('Failed to find process with identifier "%s"', identifier)

            return None

    def describe(self, process):
        pass

    def execute(self, process, inputs=None, domains=None, **kwargs):
        if inputs is None:
            inputs = []

        if domains is None:
            domains = []

        params = {
                'service': 'WPS',
                'request': 'Execute',
                #'version': process.version,
                'Identifier': process.identifier,
                }

        variable = [x.parameterize() for x in inputs]

        domain = [x.parameterize() for x in domains]

        parameters = [named_parameter.NamedParameter(x, *y) for x, y in kwargs.iteritems()]

        process.inputs = inputs

        process.parameters = parameters
        
        operation = [process.parameterize()]

        data_inputs = {
                'variable': variable,
                'domain': domain,
                'operation': operation
                }

        params['datainputs'] = '[{0}]'.format(';'.join('{0}={1}'.format(x, json.dumps(y))
            for x, y in data_inputs.iteritems()))

        response = self.__request('GET', params=params)

        process.response = operations.ExecuteResponse.from_xml(response.text)

if __name__ == '__main__':
    from esgf import Variable

    tas = Variable('file:///data/tas_6h.nc', 'tas')

    w = WPS('http://0.0.0.0:8000/wps', log=True)

    p = w.get_process('CDSpark.max')

    w.execute(p, inputs=[tas], axes=['x', 'y'])

    print p.status_location
