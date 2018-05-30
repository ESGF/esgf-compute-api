""" A WPS Client """

import json
import logging
import re
import sys

import requests
from pyxb.utils import domutils

import cwt
from cwt.wps import ows
from cwt.wps import wps
from cwt.wps import xlink

domutils.BindingDOMSupport.DeclareNamespace(ows.Namespace, 'ows')

domutils.BindingDOMSupport.DeclareNamespace(wps.Namespace, 'wps')

domutils.BindingDOMSupport.DeclareNamespace(xlink.Namespace, 'xlink')

bds = domutils.BindingDOMSupport()

logger = logging.getLogger('cwt.wps_client')

__ALL__ = [
    'WPSClient',
]

class WPSClient(object):
    def __init__(self, url, **kwargs):
        """ WPS class

        An class to connect and communicate with a WPS server implementing
        the ESGF-CWT API.
        
        Attributes:
            url: A string url path for the WPS server.
            api_key: A string API_KEY for the WPS server.
            version: A string version of the WPS server.
            language: A string language code for the WPS server to communicate in.
            log: A boolean flag to enable logging
            log_file: A string path for a log file.
            verify: A bool to enable/disable verifying a server's TLS certificate.
            ca: A str path to a CA bundle to use when verifiying a server's TLS certificate.
        """
        self.__url = url
        self.__version = kwargs.get('version')
        self.__language = kwargs.get('language')
        self.__api_key = kwargs.get('api_key')
        self.__capabilities = None 
        self.__csrf_token = None
        self.__client = requests.Session()
        self.__file_handler = None
        self.__ssl_verify = kwargs.get('verify', True)
        self.__ssl_verify_ca = kwargs.get('ca', None)

        if kwargs.get('log') is not None:
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            logger.setLevel(logging.INFO)

            stream_handler = logging.StreamHandler(sys.stdout)

            stream_handler.setFormatter(formatter)

            logger.addHandler(stream_handler)

            log_file = kwargs.get('log_file')

            if log_file is not None:
                self.__file_handler = logging.FileHandler(log_file)

                self.__file_handler.setFormatter(formatter)

                logger.addHandler(self.__file_handler)

    def __repr__(self):
        return ('Process(url=%r, version=%r, language=%r, capabilities=%r, ssl_verify=%r)') % (
            self.__url,
            self.__version,
            self.__language,
            self.__capabilities is not None,
            self.__ssl_verify,
        )

    def __del__(self):
        logging.shutdown()

        if self.__file_handler is not None:
            logger.removeHandler(self.__file_handler)

            self.__file_handler.close()
    
    def get_capabilities(self, refresh=False, method='GET'):
        """ Attempts to retrieve and return the WPS servers capabilities document. """
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities(method)

        return self.__capabilities

    def __http_request(self, method, url, params, data, headers):
        """ HTTP request

        Args:
            method: A string HTTP method.
            url: A string url path to query.
            params: A dict containing parameters.
            data: A string to send in the HTTP body.
            headers: A dict of additional headers.

        Returns:
            A string response from the WPS server.
        """
        if self.__api_key is not None:
            if params is None:
                params = {}

            # sign all requests with the api key
            params['api_key'] = self.__api_key

        kwargs = {
            'params': params,
            'data': data,
            'headers': headers,
            'verify': self.__ssl_verify,
        }

        if self.__ssl_verify_ca is not None and self.__ssl_verify:
            kwargs['verify'] = self.__ssl_verify_ca

        try:
            response = self.__client.request(method, url, **kwargs)
        except requests.RequestException as e:
            raise cwt.WPSHttpError.from_request_response(e.response)

        logger.debug('%s request succeeded', method)

        logger.debug('Response headers %s', response.headers)

        logger.debug('Response cookies %s', response.cookies)

        if 'csrftoken' in response.cookies:
            self.__csrf_token = response.cookies['csrftoken']

        if response.status_code > 200:
            raise cwt.WPSHttpError.from_request_response(response)

        return response.text

    def __request(self, method, params=None, data=None):
        """ WPS Request

        Prepares the HTTP request by fixing urls and adding extra headers.
        
        Args:
            method: A string HTTP method.
            params: A dict of HTTP parameters.
            data: A string for data for the HTTP body.

        Returns:
            A string response from the server.
        """
        url = self.__url

        if method.lower() == 'post' and self.__url[-1] != '/':
            url = '{0}/'.format(self.__url)

        headers = {}

        if self.__csrf_token is not None:
            headers['X-CSRFToken'] = self.__csrf_token
       
        response = self.__http_request(method, url, params, data, headers)

        return response

    def __get_capabilities(self, method):
        """ Builds and attempts a GetCapabilities request. """
        if method.lower() == 'get':
            params = {
                'service': 'WPS',
                'request': 'GetCapabilities',
            }

            if self.__version is not None:
                params['acceptversions'] = self.__version

            if self.__language is not None:
                params['language'] = self.__language

            logger.debug(params)

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            data = wps.get_capabilities().toxml(bds=bds)

            logger.debug(data)

            response = self.__request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        capabilities = wps.CreateFromDocument(response)

        return capabilities

    def processes(self, pattern=None, refresh=False, method='GET'):
        """ Returns a list of WPS processes.

        Args:
            pattern: A string regex used to filter the processes by identifier.
            refresh: A boolean to force a GetCapabilites refresh.
            method: A string HTTP method.

        Returns:
            A GetCapabilities object.
        """
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities(method)

        processes = [cwt.Process.from_binding(x) for x in self.__capabilities.ProcessOfferings.Process]

        if pattern is not None:
            processes = [x for x in processes if re.match(pattern, x.identifier) is not None]

        return processes

    def get_process(self, identifier, method='GET'):
        """ Return a specified process.
        
        Args:
            identifier: A string process identifier.

        Returns:
            The specified process instance.

        Raises:
            Exception: A process with identifier was not found.
        """
        processes = self.processes(identifier, method=method)

        try:
            process = processes[0]
        except IndexError:
            raise cwt.WPSError('No process with identifer matching "{}" exists'.format(identifier))
        else:
            return process

    def describe_process(self, process, method='GET'):
        """ Return a DescribeProcess response.
        
        Args:
            process: An object of type Process to describe.
            method: A string HTTP method to use.

        Returns:
            A DescribeProcessResponse object.
        """
        identifier = process.identifier

        if method.lower() == 'get':
            params = {
                'service': 'wps',
                'request': 'describeprocess',
                'version': '1.0.0',
                'identifier': identifier,
            }

            if self.__language is not None:
                params['language'] = self.__language

            logger.debug(params)

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            data = wps.describe_process([identifier], '1.0.0').toxml(bds=bds)

            logger.debug(data)

            response = self.__request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        desc = wps.CreateFromDocument(response)

        return desc

    @staticmethod
    def parse_data_inputs(data_inputs):
        """ Parses a data_inputs string

        The data_inputs string follows this format:

        [variable=[];domain=[];operation=[]]

        Args:
            data_inputs: A string containing the processes data_inputs

        Returns:
            A tuple containing the a list of operations, domains and variables
            object contained in the data_inputs string.
        """
        match = re.search('\[(.*)\]', data_inputs)

        kwargs = dict((x.split('=')[0], json.loads(x.split('=')[1])) for x in match.group(1).split(';'))

        variables = [cwt.Variable.from_dict(x) for x in kwargs.get('variable', [])]

        domains = [cwt.Domain.from_dict(x) for x in kwargs.get('domain', [])]

        operation = [cwt.Process.from_dict(x) for x in kwargs.get('operation', [])]

        return operation, domains, variables

    def __prepare_data_inputs(self, process, inputs, domain, **kwargs):
        """ Preparse a process inputs for the data_inputs string.

        Args:
            process: A object of type Process to be executed.
            inputs: A list of Variables/Operations.
            domain: A Domain object.
            kwargs: A dict of addiontal named_parameters or k=v pairs.

        Returns:
            A dictionary containing the operations, domains and variables
            associated with the process.
        """
        domains = []

        if domain is not None:
            process.domain = domain

            domains.append(domain.parameterize())

        parameters = [cwt.NamedParameter(x, y) for x, y in kwargs.iteritems()]

        process.inputs.extend(inputs)

        process.add_parameters(*parameters)

        processes, variables = process.collect_input_processes()

        variables = [x.parameterize() for x in variables]

        operation = [process.parameterize()] + [x.parameterize() for x in processes]

        return {'variable': variables, 'domain': domains, 'operation': operation}

    def prepare_data_inputs(self, process, inputs, domain, **kwargs):
        """ Creates the data_inputs string. """
        data_inputs = self.__prepare_data_inputs(process, inputs, domain, **kwargs)

        return '[{}]'.format(';'.join('{}={}'.format(x, json.dumps(y))
            for x, y in data_inputs.iteritems()))

    def execute(self, process, inputs=None, domain=None, method='POST', **kwargs):
        """ Execute the process on the WPS server. 
        
        Args:
            process: A Process object to be executed on the WPS server.
            inputs: A list in Variables/Processes.
            domain: A Domain object to be used.
            kwargs: A dict containing additional arguments.
        """
        if inputs is None:
            inputs = []

        if method.lower() == 'get':
            params = {
                'service': 'WPS',
                'request': 'Execute',
                'version': '1.0.0',
                'identifier': process.identifier,
            }

            params['datainputs'] = self.prepare_data_inputs(process, inputs, domain, **kwargs)

            logger.debug(params)

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            data_inputs = self.__prepare_data_inputs(process, inputs, domain, **kwargs)

            variables = wps.data_input('variable', 'Variable', json.dumps(data_inputs['variable']))

            domains = wps.data_input('domain', 'Domain', json.dumps(data_inputs['domain']))

            operation = wps.data_input('operation', 'Operation', json.dumps(data_inputs['operation']))

            data = wps.execute(process.identifier, '1.0.0', [variables, domains, operation]).toxml(bds=bds)

            logger.debug(data)

            response = self.__request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        process.response = wps.CreateFromDocument(response)

        if process.is_failed:
            raise Exception(process.exception_message)
