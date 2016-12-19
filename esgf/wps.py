""" A WPS Client """

import json
import logging
import tempfile
import urllib
import sys

import lxml
from lxml import etree
from owslib.wps import WebProcessingService
from owslib.wps import WPSExecution
import requests

from esgf import errors
from esgf import process

logger = logging.getLogger()

_IDENTIFICATION = (
    'title',
    'abstract',
    'keywords',
    'accessconstraints',
    'fees',
    'type',
    'service',
    'version',
    'profiles'
)

_PROVIDER = (
    'name',
    'contact',
    'url'
)

_CONTACT = (
    'name',
    'organization',
    'site',
    'position',
    'phone',
    'fax',
    'address',
    'city',
    'region',
    'postcode',
    'country',
    'email',
    'url',
    'hours',
    'instructions'
)

class UnsupportedMethodError(Exception):
    pass

class WPSRequestError(Exception):
    pass

class WPSResponseError(Exception):
    pass

class _WPSRequest(object):
    """ _WPSRequest

    Execute WPS operations through HTTP requests. Operations are
    GetCapabilities, DescribeProcess and Execute.

    Attributes:
        username: Username to access WPS server.
        password: Password for Username.
        accept_versions: Version of servers allowed to connect to.
        language: Language required.
    """
    def __init__(self, base_url, **kwargs):
        """ init """
        self._base_url = base_url
        self._username = kwargs.get('username', None)
        self._password = kwargs.get('password', None)
        self._accept_versions = kwargs.get('accept_versions', None)
        self._language = kwargs.get('language', None)

        self._session = requests.Session()

    def _get_params(self, request):
        """ Returns the common required parameters for a GET request. """
        params = {
            'service': 'WPS',
            'request': request,
        }

        if self._language:
            params['language'] = self._language

        return params

    def _get_auth(self):
        """ Returns the authentication header. """
        auth = None

        if self._username and self._password:
            auth = requests.auth.HTTPBasicAuth(self._username,
                                               self._password)

        return auth

    def _get_request(self, params):
        try:
            response = self._session.get(self._base_url,
                                         params=params,
                                         auth=self._get_auth())
        except requests.RequestException as e:
            logger.exception('Get request failed with parameters:\n%s',
                             params)

            raise WPSRequestError('Get request failed: %s' % (e.message,))

        logger.debug('Get request success\n%s', response.url)

        if response.status_code != 200:
            raise WPSResponseError('Get status code %s: %s' %
                                   (response.status_code,
                                    response.reason))

        logger.debug('Get response\n%s', response.text)

        return response

    def _post_request(self, data):
        try:
            response = self._session.post(self._base_url,
                                          data=data,
                                          auth=self._get_auth())
        except requests.RequestException as e:
            logger.exception('Post request failed with data:\n%s',
                             data)

            raise WPSRequestError('Post request failed: %s' % (e.message,))

        logger.debug('Post request success\n%s', data)

        if response.status_code != 200:
            raise WPSResponseError('Post status code %s: %s' %
                                   (response.status_code,
                                    response.reason))

        logger.debug('Post response\n%s', response.text)

        return response

    def get_capabilities(self, method='GET'):
        """ GetCapabilities request.

        Sends a GetCapabilites request to a WPS server. The response is parsed
        and returned.

        Args:
            method: HTTP method used to make the request.

        Returns:
            A _WPSGetCapabilitiesResponse object wrapping the return XML response.

        Raises:
            UnsupportedMethodError: An unsupported HTTP method was used.
            WPSRequestError: An error occurred during the request.
            WPSResponseError: An error occurred during the response handling.
        """
        method_sel = method.lower()

        if method_sel == 'get':
            params = self._get_params('GetCapabilities')

            # Optional parameter
            if self._accept_versions:
                params['AcceptedVersions'] = self._accept_versions

            response = self._get_request(params)
        else:
            # Handle unsupported methods
            raise UnsupportedMethodError('GetCapabilities does not support "%s"' % (method,))

        return _WPSGetCapabilitiesResponse.from_response(response.text)

    def describe_process(self, identifier, version='1.0.0', method='GET'):
        """ DescribeProcess request.

        Sends a DescribeProcess request to a WPS server. The response is 
        parsed and returned.

        Args:
            identifier: The identifier of the process to describe.
            version: Version of the process of interest.
            method: HTTP method used to perform the request.

        Returns:
            A _WPSDescribeProcessResponse object wrapping the server XML
            response.

        Raises:
            UnsupportedMethodError: An unsupported HTTP method was used.
            WPSRequestError: An error occurred during the request.
            WPSResponseError: An error occurred during the response handling.
        """
        method_sel = method.lower()

        if method_sel == 'get':
            params = self._get_params('DescribeProcess')

            # Add the required parameters
            params['Identifier'] = identifier

            params['version'] = version

            response = self._get_request(params)
        else:
            raise UnsupportedMethodError('DescribeProcess does not support "%s"' % (method,))

        return _WPSDescribeProcessResponse.from_response(response.text)

    def execute(self, identifier, inputs, version='1.0.0', method='POST', **kwargs):
        """ Execute request.

        Sends an Execute request to a WPS server. The response is parsed and
        returned.

        Args:
            identifier: Process identifier to be executed.
            inputs: Dictionary of Process inputs.
            version: Version of the Process that will be executed.
            method: HTTP method used to perform request.

        Returns:
            A _WPSExecuteResponse object containing the server response.

        Raises:
            UnsupportedMethodError: An unsupported HTTP method was used.
            WPSRequestError: An error occurred during the request.
            WPSResponseError: An error occurred during the response handling.
        """
        method_sel = method.lower()

        status = kwargs.get('status', False)
        store = kwargs.get('store', False)

        if method_sel == 'get':
            params = self._get_params('Execute')

            # Add our required parameters
            params['version'] = version
            params['Identifier'] = identifier
            params['status'] = status
            params['storeExecuteResponse'] = store

            # Format the dictionary to list of k=v strings
            data_inputs = ['%s=%s' % (k, json.dumps(v))
                           for k, v in inputs.iteritems()]

            data_inputs = ';'.join(data_inputs)

            # Set datainputs parameter, remove spaces for server side.
            params['datainputs'] = '[%s]' % (data_inputs.replace(' ', ''),)

            response = self._get_request(params)
        elif method_sel == 'post':
            data = [(k, json.dumps(v)) for k, v in inputs.iteritems()]

            # Build the XML execute document
            xml_payload = self._build_request(identifier,
                                              data,
                                              status,
                                              store)

            response = self._post_request(xml_payload)
        else:
            raise UnsupportedMethodError('Execute does not support "%s"' % (method,))

        ex_res =  _WPSExecuteResponse.from_response(response.text)

        # Check if the process failed, raise an Exception to warn user
        if ex_res.status == 'ProcessFailed':
            errors = [self._error_to_json(x) for x in ex_res.errors]

            raise WPSResponseError(errors)

        return ex_res

    def _error_to_json(self, error):
        """ Helper method to format errors. """
        return {
            'code': error.code,
            'locator': error.locator,
            'text': error.text,
        }

    def _build_request(self, identifier, data, status, store):
        """ Build Execute XML document. """
        execution = WPSExecution()

        xml = execution.buildRequest(identifier, data, 'output')

        # Set the status and store flags independently of eachother
        request_document = xml.xpath(
            '/wps100:Execute/wps100:ResponseForm/wps100:ResponseDocument',
            namespaces=xml.nsmap)[0]

        request_document.set('status', str(status))
        request_document.set('storeExecuteResponse', str(store))

        # Serialize the XML tree
        try:
            xml_payload = etree.tostring(xml)
        except lxml.etree.XMLSyntaxError as e: # pragma: no cover
            logger.exception(e.message) 

            raise WPSRequestError('Failed to create WPS XML document.')

        return xml_payload

class _WPSResponse(object):
    def load_xml(self, response):
        try:
            xml = etree.fromstring(response.encode('utf-8'))
        except (AttributeError, lxml.etree.XMLSyntaxError):
            logger.exception('Could not parse server response')
            logger.debug(response)

            raise WPSResponseError('Failed to parse server response')
        else:
            return xml

class _WPSExecuteResponse(_WPSResponse):
    """ Execute Response wrapper. """
    def __init__(self):
        self._data = None

    @classmethod
    def from_response(cls, response):
        """ Create WPSExecuteResponse from XML. """
        x = cls()

        x.parse(response)

        return x

    @property
    def status(self):
        """ Process status. """
        return self._data.status

    @property
    def status_location(self):
        """ Status location if status flag is set. """
        return self._data.statusLocation

    @property
    def percent(self):
        """ Process percentage. """
        return self._data.percentCompleted

    @property
    def message(self):
        """ Process message. """
        return self._data.statusMessage

    @property
    def output(self):
        """ Process output. """
        with tempfile.NamedTemporaryFile() as temp:
            try:
                self._data.getOutput(temp.name)
            except requests.RequestException:
                logger.exception('Failed to retrieve process outputs')

                for o in self._data.processOutputs:
                    logger.debug(o.reference)
                
                raise errors.WPSClientError('Failed to retrieve process output')

            output = temp.read() # pragma: no cover

        return output # pragma: no cover

    @property
    def errors(self):
        """ List of process errors. """
        return self._data.errors

    def parse(self, response):
        """ Parses XML response document. """
        xml = self.load_xml(response)

        self._data = WPSExecution()

        self._data.parseResponse(xml)

    def check_status(self, timeout): # pragma: no cover
        """ Wait timeout then check Process status. """
        self._data.checkStatus(timeout)

class _WPSDescribeProcessResponse(_WPSResponse):
    """ Describe Process response wrapper. """
    def __init__(self):
        self._data = None
        self._process = None

    @classmethod
    def from_response(cls, response):
        """ Create DescribeProcess from XML. """
        x = cls()

        x.parse(response)

        return x

    @property
    def version(self):
        """ Version of the process. """
        return self._process.processVersion

    @property
    def status(self):
        """ Status supported. """
        return self._process.statusSupported

    @property
    def store(self):
        """ Store supported. """
        return self._process.storeSupported

    @property
    def abstract(self):
        """ Process abstract. """
        return self._process.abstract

    @property
    def identifier(self):
        """ Process identifier. """
        return self._process.identifier

    @property
    def title(self):
        """ Process title. """
        return self._process.title

    def parse(self, response):
        """ Parse response XML. """
        xml = self.load_xml(response)

        self._data = WebProcessingService('', skip_caps=True)

        self._process = self._data._parseProcessMetadata(xml)

class _WPSGetCapabilitiesResponse(_WPSResponse):
    """ Get Capabilities response wrapper. """
    def __init__(self):
        self._data = None

    @classmethod
    def from_response(cls, response):
        """ Create GetCapabilities from XML. """
        x = cls()

        x.parse(response)

        return x

    @property
    def identification(self):
        """ Server identification. """
        return dict((x, getattr(self._data.identification, x))
                    for x in _IDENTIFICATION)

    @property
    def provider(self):
        """ Provider information. """
        prov = dict((x, getattr(self._data.provider, x))
                    for x in _PROVIDER)

        if 'contact' in prov:
            prov['contact'] = dict((x, getattr(prov['contact'], x))
                                   for x in _CONTACT)

        return prov

    @property
    def processes(self):
        """ List of process identifiers. """
        return [x.identifier for x in self._data.processes]

    def parse(self, response):
        """ Parse response XML. """
        xml = self.load_xml(response)

        self._data = WebProcessingService('', skip_caps=True)

        self._data._parseCapabilitiesMetadata(xml)

class WPS(object):
    """ Web Processing Service client.

    Client is used to query WPS operations; GetCapabilities, DescribeProcess,
    and Execute.

    >>> import esgf
    >>> wps = esgf.WPS('http://wps_instance/wps')

    Print available operations on the WPS server.

    >>> for proc in wps:
    >>>     print proc

    Execute an operation.

    >>> avg = esgf.Operation(inputs=[tas], axes='latitude')
    >>> wps.execute_op(avg)

    Attributes:
    url: String WPS uri.
    username: String username for WPS server.
    password: String password for username.
    log: Boolean flag to enable logging.
    log_file: String path to log file.

    """
    def __init__(self, url, username=None, password=None, **kwargs):
        """ Inits WebProcessingService """
        self._url = url

        if kwargs.get('log') is not None:
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            logger.setLevel(logging.DEBUG)

            std_handler = logging.StreamHandler(sys.stdout)
            std_handler.setFormatter(formatter)
            logger.addHandler(std_handler)

            log_file = kwargs.get('log_file')

            if log_file is not None:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

        self._service = _WPSRequest(url, username=username, password=password, **kwargs)

        self._capabilities = None

    def init(self, force=False):
        """ Executes WPS GetCapabilites request.

        Retrieves a servers description data (identification and provider)
        and its processes.

        """
        if not self._capabilities or force:
            logger.debug('Retrieving capabilities')

            self._capabilities = self._service.get_capabilities()

    @property
    def identification(self):
        """ Returns identification data as JSON. """
        self.init()

        return self._capabilities.identification

    @property
    def provider(self):
        """ Returns provider data as JSON. """
        self.init()

        return self._capabilities.provider

    def get_process(self, name):
        """ Returns process from name. """
        self.init()

        if name not in self._capabilities.processes:
            raise errors.WPSClientError('No process named \'%s\' was found.' % (name,))

        return process.Process.from_identifier(self, name)

    def execute_op(self, operation, store=False, status=False, method='POST'):
        """ Directly executes an operation. """

        variable, domain = operation.gather()

        data_inputs = {
            'domain': [x.parameterize() for x in domain.values()],
            'variable': [x.parameterize() for x in variable.values()],
            'operation': operation.flatten(),
        }

        operation.result = self.execute(operation.identifier,
                                        data_inputs,
                                        store=store,
                                        status=status,
                                        method=method)

    def execute(self, identifier, inputs, store=False, status=False, method='POST'):
        """ Executes a WPS process. """
        return self._service.execute(identifier,
                                     inputs,
                                     method=method,
                                     store=store,
                                     status=status)

    def __iter__(self):
        self.init()

        processes = self._capabilities.processes

        for proc in processes:
            yield proc

    def __repr__(self):
        return 'WPS(url=%r, service=%r)' % (self._url, self._service)

    def __str__(self):
        return 'url=%s service=%s' % (self._url, self._service) # pragma: no cover
