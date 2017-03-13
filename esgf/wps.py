""" A WPS Client """

import json
import logging
import sys

import requests
from lxml import etree

from esgf import named_parameter
from esgf import process
from esgf.wps_lib import metadata
from esgf.wps_lib import operations

logger = logging.getLogger()

class WPSError(Exception):
    pass

class WPSHTTPError(Exception):
    pass

class WPSHTTPMethodError(Exception):
    pass

class WPS(object):
    def __init__(self, url, username=None, password=None, **kwargs):
        self.__url = url
        self.__username = username
        self.__password = password
        self.__version = kwargs.get('version')
        self.__language = kwargs.get('laanguage')
        self.__capabilities = None 
        self.__csrf_token = None
        self.__client = requests.Session()

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
        url = self.__url

        if method.lower() == 'post' and self.__url[-1] != '/':
            url = '{0}/'.format(self.__url)

        headers = {}

        if self.__csrf_token is not None:
            headers['X-CSRFToken'] = self.__csrf_token
        
        try:
            response = self.__client.request(method, url, params=params, data=data, headers=headers)
        except requests.RequestException:
            logger.exception('%s request failed', method)

            raise WPSHTTPError('{0} request failed'.format(method))

        logger.debug('%s request succeeded', method)

        logger.debug('Response headers %s', response.headers)

        logger.debug('Response cookies %s', response.cookies)

        if 'csrftoken' in response.cookies:
            self.__csrf_token = response.cookies['csrftoken']

        if response.status_code != 200:
            raise WPSHTTPError('{0} response failed with status code '
                    '{1} {2}'.format(method, response.status_code, response.content))

        return response

    def __get_capabilities(self, method='GET'):
        params = {
                'service': 'WPS',
                'request': 'GetCapabilities',
                }

        if self.__version is not None:
            params['acceptversions'] = self.__version

        if self.__language is not None:
            params['language'] = self.__language

        if method.lower() == 'get':
            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            request = operations.GetCapabilitiesRequest()

            data = request(**params)

            response = self.__request(method, data=data)
        else:
            raise WPSHTTPMethodError('{0} is an unsupported method'.format(method))

        try:
            capabilities = operations.GetCapabilitiesResponse.from_xml(response.text)
        except etree.XMLSyntaxError:
            logger.exception('Failed to parse XML response')

            raise WPSError('Failed to parse XML response')

        return capabilities

    def processes(self, regex=None, refresh=False, method='GET'):
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities(method)

        return [process.Process(x) for x in self.__capabilities.process_offerings]

    def get_process(self, identifier, method='GET'):
        if self.__capabilities is None:
            self.__capabilities = self.__get_capabilities(method)

        try:
            return [process.Process(x) for x in self.__capabilities.process_offerings
                    if x.identifier == identifier][0]
        except IndexError:
            logger.debug('Failed to find process with identifier "%s"', identifier)

            return None

    def describe(self, process, method='GET'):
        params = {
                'service': 'wps',
                'request': 'describeprocess',
                'version': '1.0.0',
                'identifier': process.identifier,
                }

        if self.__language is not None:
            params['language'] = self.__language

        if method.lower() == 'get':
            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            request = operations.DescribeProcess()

            data = request(**params)

            resposne = self.__request(method, data=data)
        else:
            raise WPSHTTPMethodError('{0} is an unsupported method'.format(method))

        try:
            desc = operations.DescribeProcessResponse.from_xml(response.text)
        except etree.XMLSyntaxError:
            logger.exception('Failed to parse XML response')

            raise WPSError('Failed to parse XML response')

        return desc

    def execute(self, process, inputs=None, domains=None, method='POST', **kwargs):
        if inputs is None:
            inputs = []

        if domains is None:
            domains = []

        params = {
                'service': 'WPS',
                'request': 'Execute',
                'version': '1.0.0',
                'identifier': process.identifier,
                }

        variables = [x.parameterize() for x in inputs]

        domains = [x.parameterize() for x in domains]

        parameters = [named_parameter.NamedParameter(x, *y) for x, y in kwargs.iteritems()]

        process.inputs = inputs

        process.parameters = parameters
        
        operation = [process.parameterize()]

        data_inputs = {
                'variable': variables,
                'domain': domains,
                'operation': operation
                }

        if method.lower() == 'get':
            params['datainputs'] = '[{0}]'.format(';'.join('{0}={1}'.format(x, json.dumps(y))
                for x, y in data_inputs.iteritems()))

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            request = operations.ExecuteRequest()

            params['data_inputs'] = []

            for key, value in data_inputs.iteritems():
                inp = metadata.Input()

                inp.identifier = key

                inp_data = metadata.ComplexData()

                inp_data.value = '{0}'.format(value)

                inp.data = inp_data

                params['data_inputs'].append(inp) 

            data = request(**params) 

            response = self.__request(method, data=data)
        else:
            raise WPSHTTPMethodError('{0} is an unsupported method'.format(method))

        try:
            process.response = operations.ExecuteResponse.from_xml(response.text)
        except etree.XMLSyntaxError:
            logger.exception('Failed to parse XML response')

            raise WPSError('Failed to parse XML response')

if __name__ == '__main__':
    w = WPS('http://0.0.0.0:8000/wps')

    from variable import Variable

    tas = Variable('file:///data/tas_6h.nc', 'tas')

    p = w.get_process('CDSpark.min')

    w.describe(p)
    #w.execute(p, inputs=[tas])
