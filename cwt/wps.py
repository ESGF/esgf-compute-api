""" A WPS Client """

import json
import logging
import re
import sys

import requests
from lxml import etree

import cwt
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger(__name__)

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
        self.__api_key = kwargs.get('api_key')
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
        else:
            logger.addHandler(logging.NullHandler())
    
    @property
    def capabilities(self):
        if self.__capabilities == None:
            self.__capabilites = self.__get_capabilities()

        return self.__capabilities

    def __http_request(self, method, url, params, data, headers):
        if self.__api_key is not None:
            if params is None:
                params = {}

            params['api_key'] = self.__api_key

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

        return response.text

    def __request(self, method, params=None, data=None):
        url = self.__url

        if method.lower() == 'post' and self.__url[-1] != '/':
            url = '{0}/'.format(self.__url)

        headers = {}

        if self.__csrf_token is not None:
            headers['X-CSRFToken'] = self.__csrf_token
       
        response = self.__http_request(method, url, params, data, headers)

        logger.info('{}'.format(response))

        return response

    def __parse_response(self, response, response_type):
        data = None

        try:
            data = response_type.from_xml(response)
        except Exception:
            logger.exception('Failed to parse CDAS2 response.')
        else:
            return data

        if data is None:
            try:
                data = metadata.ExceptionReport.from_xml(response)
            except Exception:
                logger.exception('Failed to parse ExceptionReport')

                raise WPSError('Failed to parse server response')
            else:
                raise WPSError(data)

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

        capabilities = self.__parse_response(response, operations.GetCapabilitiesResponse)

        return capabilities

    def processes(self, regex=None, refresh=False, method='GET'):
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities(method)

        return [cwt.Process(x) for x in self.__capabilities.process_offerings]

    def get_process(self, identifier, method='GET'):
        if self.__capabilities is None:
            self.__capabilities = self.__get_capabilities(method)

        try:
            return [cwt.Process(x) for x in self.__capabilities.process_offerings
                    if x.identifier == identifier][0]
        except IndexError:
            logger.debug('Failed to find process with identifier "%s"', identifier)

            raise Exception('Failed to find process with identifier "{}"'.format(identifier))

    def describe(self, process, method='GET'):
        if isinstance(process, cwt.Process):
            identifier = process.identifier
        else:
            identifier = process

        params = {
                'service': 'wps',
                'request': 'describeprocess',
                'version': '1.0.0',
                'identifier': identifier,
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

        desc = self.__parse_response(response, operations.DescribeProcessResponse)

        return desc

    @staticmethod
    def parse_data_inputs(data_inputs):
        match = re.search('\[(.*)\]', data_inputs)

        kwargs = dict((x.split('=')[0], json.loads(x.split('=')[1])) for x in match.group(1).split(';'))

        variables = [cwt.Variable.from_dict(x) for x in kwargs.get('variable', [])]

        domains = [cwt.Domain.from_dict(x) for x in kwargs.get('domain', [])]

        operation = [cwt.Process.from_dict(x) for x in kwargs.get('operation', [])]

        return operation, domains, variables

    def __prepare_data_inputs(self, process, inputs, domains, **kwargs):
        domains = [x.parameterize() for x in domains]

        parameters = [cwt.NamedParameter(x, *y) for x, y in kwargs.iteritems()]

        process.inputs.extend(inputs)

        process.add_parameters(*parameters)

        processes, variables = process.collect_input_processes()

        variables = [x.parameterize() for x in variables]

        operation = [process.parameterize()] + [x.parameterize() for x in processes]

        return {'variable': variables, 'domain': domains, 'operation': operation}

    def prepare_data_inputs(self, process, inputs, domains, **kwargs):
        data_inputs = self.__prepare_data_inputs(process, inputs, domains, **kwargs)

        return '[{}]'.format(';'.join('{}={}'.format(x, json.dumps(y))
            for x, y in data_inputs.iteritems()))

    def __execute_post_data(self, data_inputs, base_params):
        request = operations.ExecuteRequest()

        base_params['data_inputs'] = []

        for key, value in data_inputs.iteritems():
            inp = metadata.Input()

            inp.identifier = key

            inp_data = metadata.ComplexData()

            inp_data.value = '{0}'.format(value)

            inp.data = inp_data

            base_params['data_inputs'].append(inp) 

        return request(**base_params)

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

        if method.lower() == 'get':
            params['datainputs'] = self.prepare_data_inputs(process, inputs, domains, **kwargs)
            #params['datainputs'] = '[{0}]'.format(';'.join('{0}={1}'.format(x, json.dumps(y))
            #    for x, y in data_inputs.iteritems()))

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            data_inputs = self.__prepare_data_inputs(process, inputs, domains, **kwargs)

            data = self.__execute_post_data(data_inputs, params)

            response = self.__request(method, data=data)
        else:
            raise WPSHTTPMethodError('{0} is an unsupported method'.format(method))

        process.response = self.__parse_response(response, operations.ExecuteResponse)
