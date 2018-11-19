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

class CapabilitiesWrapper(object):
    def __init__(self, binding, client):
        self.binding = binding

        self.client = client

    @property
    def processes(self):
        data = []

        for process in self.binding.ProcessOfferings.Process:
            proc = cwt.Process.from_binding(process)

            proc.set_client(self.client)

            data.append(proc)

        return data

    @property
    def version(self):
        return self.binding.version

    @property
    def lang(self):
        return self.binding.lang.Default

    @property
    def service(self):
        return self.binding.service

class ProcessDescriptionWrapper(object):
    def __init__(self, binding):
        self.binding = binding

    @property
    def identifier(self):
        return self.binding.Identifier.value()

    @property
    def title(self):
        return self.binding.Title.value()

    @property
    def abstract(self):
        return self.binding.Abstract.value()

    @property
    def metadata(self):
        return dict(x.title.split(':') for x in self.binding.Metadata)

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
            cert: A str path to an SSL client cert or a tuple as ('cert', 'key').
            timeout: A float or tuple. If tuple the timeout format is as follows
                (connect timeout, read timeout).
        """
        self.url = url

        self.version = kwargs.get('version')
        self.language = kwargs.get('language')
        self.api_key = kwargs.get('api_key')
        self.ssl_verify = kwargs.get('verify', True)
        self.ssl_verify_ca = kwargs.get('ca', None)
        self.ssl_cert = kwargs.get('cert', None)
        self.timeout = kwargs.get('timeout', None)

        self.csrf_token = None
        self.file_handler = None
        self.capabilities = None

        self.client = requests.Session()

        if kwargs.get('log', False):
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            logger.setLevel(logging.INFO)

            stream_handler = logging.StreamHandler(sys.stdout)

            stream_handler.setFormatter(formatter)

            logger.addHandler(stream_handler)

            log_file = kwargs.get('log_file')

            if log_file is not None:
                self.file_handler = logging.FileHandler(log_file)

                self.file_handler.setFormatter(formatter)

                logger.addHandler(self.file_handler)
        else:
            logger.addHandler(logging.NullHandler())

    def __repr__(self):
        return ('Process(url=%r, version=%r, language=%r, capabilities=%r, ssl_verify=%r)') % (
            self.url,
            self.version,
            self.language,
            self.capabilities is not None,
            self.ssl_verify,
        )
    
    def get_capabilities(self, method='GET'):
        """ Builds and attempts a GetCapabilities request. """
        if method.lower() == 'get':
            params = {
                'service': 'WPS',
                'request': 'GetCapabilities',
            }

            if self.version is not None:
                params['acceptversions'] = self.version

            if self.language is not None:
                params['language'] = self.language

            response = self.request(method, params=params)
        elif method.lower() == 'post':
            bds.reset()

            data = wps.get_capabilities().toxml(bds=bds)

            response = self.request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        if response is None:
            raise cwt.WPSError('Recieved invalid response')

        self.capabilities = CapabilitiesWrapper(response, self)

        return self.capabilities

    def describe_process(self, process, method='GET'):
        """ Return a DescribeProcess response.
        
        Args:
            process: An object of type Process to describe.
            method: A string HTTP method to use.

        Returns:
            A DescribeProcessResponse object.
        """
        if not isinstance(process, list):
            process = [process]

        identifier = ','.join([x.identifier for x in process])

        if method.lower() == 'get':
            params = {
                'service': 'WPS',
                'request': 'DescribeProcess',
                'version': '1.0.0',
                'identifier': identifier,
            }

            if self.language is not None:
                params['language'] = self.language


            response = self.request(method, params=params)
        elif method.lower() == 'post':
            bds.reset()

            data = wps.describe_process(identifier, '1.0.0').toxml(bds=bds)

            response = self.request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        for x in response.ProcessDescription:
            try:
                p = [y for y in process if y.identifier == x.Identifier.value()][0]
            except IndexError:
                raise cwt.CWTError('Error matching description "{name}"', name=x.identifier)

            p.description = ProcessDescriptionWrapper(x)

        return [x.description for x in process]

    def execute(self, process, inputs=None, domain=None, method='POST',
                block=False, **kwargs):
        """ Execute the process on the WPS server. 
        
        Args:
            process: A Process object to be executed on the WPS server.
            inputs: A list in Variables/Processes.
            domain: A Domain object to be used.
            kwargs: A dict containing additional arguments.
        """
        process.set_client(self)

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

            response = self.request(method, params=params)
        elif method.lower() == 'post':
            data_inputs = self.prepare_data_inputs(process, inputs, domain, **kwargs)

            variables = wps.data_input('variable', 'Variable', json.dumps(data_inputs['variable']))

            domains = wps.data_input('domain', 'Domain', json.dumps(data_inputs['domain']))

            operation = wps.data_input('operation', 'Operation', json.dumps(data_inputs['operation']))

            bds.reset()

            data = wps.execute(process.identifier, '1.0.0', [variables, domains, operation]).toxml(bds=bds)

            response = self.request(method, data=data)
        else:
            raise cwt.WPSError('{} method is unsupported'.format(method))

        process.response = response

        if block:
            process.wait()

        if process.failed:
            raise Exception(process.exception_message)

        if block:
            return process.output

    def processes(self, pattern=None, method='GET'):
        if self.capabilities is None:
            self.get_capabilities(method)

        if pattern is None:
            return self.capabilities.processes

        try:
            return [x for x in self.capabilities.processes 
                    if re.match(pattern, x.identifier)]
        except re.error:
            raise cwt.CWTError('Invalid pattern, see python\'s "re" module for documentation')

    def request(self, method, params=None, data=None):
        """ WPS Request

        Prepares the HTTP request by fixing urls and adding extra headers.
        
        Args:
            method: A string HTTP method.
            params: A dict of HTTP parameters.
            data: A string for data for the HTTP body.

        Returns:
            A string response from the server.
        """
        url = self.url

        if method.lower() == 'post' and self.url[-1] != '/':
            url = '{0}/'.format(self.url)

        headers = {}

        if self.csrf_token is not None:
            headers['X-CSRFToken'] = self.csrf_token

        response = self.http_request(method, url, params, data, headers)

        data = wps.CreateFromDocument(response)

        if isinstance(data, cwt.wps.ows.CTD_ANON_9):
            raise cwt.WPSExceptionError.from_binding(data)

        return data

    def http_request(self, method, url, params, data, headers):
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
        if self.api_key is not None:
            if params is None:
                params = {}

            # sign all requests with the api key
            params['api_key'] = self.api_key

        kwargs = {
            'params': params,
            'data': data,
            'headers': headers,
            'verify': self.ssl_verify,
            'timeout': self.timeout,
        }

        if self.ssl_verify_ca is not None and self.ssl_verify:
            kwargs['verify'] = self.ssl_verify_ca

        if self.ssl_cert is not None:
            kwargs['cert'] = self.ssl_cert

        logger.info('Request %r, %r, %r', method, url, kwargs)

        try:
            response = self.client.request(method, url, **kwargs)
        except requests.ConnectionError as e:
            logger.exception('Connection error')

            raise cwt.WPSHttpError('Connection failed {error}', error=e)
        except requests.HTTPError as e:
            logger.exception('HTTP error')

            raise cwt.WPSHttpError('HTTP request failed {error}', error=e)
        except requests.Timeout as e:
            logger.exception('Timeout error')

            raise cwt.WPSHttpError('Timeout error {error}', error=e)

        logger.debug('%s request succeeded', method)

        if 'csrftoken' in response.cookies:
            self.csrf_token = response.cookies['csrftoken']

        if response.status_code > 200:
            raise cwt.WPSHttpError.from_request_response(response)

        return response.text

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

    def prepare_data_inputs(self, process, inputs, domain, **kwargs):
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
        if process.description is None:
            self.describe_process(process)

        new_process = cwt.Process.from_identifier(process.identifier)

        new_process.description = process.description

        new_process.name = process.name

        domains = []

        if domain is not None:
            new_process.domain = domain

            domains.append(domain.parameterize())

        new_process.inputs = [x for x in process.inputs]

        new_process.inputs.extend(inputs)

        new_process.validate()

        parameters = [cwt.NamedParameter(x, y) for x, y in kwargs.iteritems()]

        new_process.add_parameters(*parameters)

        processes, variables = new_process.collect_input_processes()

        variables = [x.parameterize() for x in variables]

        operation = [new_process.parameterize()] + [x.parameterize() for x in processes]

        return {'variable': variables, 'domain': domains, 'operation': operation}

    def prepare_data_inputs_str(self, process, inputs, domains, **kwargs):
        data_inputs = self.prepare_data_inputs(process, inputs, domains, **kwargs)

        variable = 'variable={}'.format(json.dumps(data_inputs['variable']))

        domain = 'domain={}'.format(json.dumps(data_inputs['domain']))

        operation = 'operation={}'.format(json.dumps(data_inputs['operation']))

        return '[{};{};{}]'.format(variable, domain, operation)
