""" A WPS Client """

from .errors import WPSClientError
from .errors import WPSServerError
from .process import Process

import json
import urllib

from owslib.wps import WPSExecution
from owslib.wps import WebProcessingService
from owslib.util import ResponseWrapper

import requests
from requests.exceptions import ConnectionError

from lxml import etree

import sys
import logging

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

class _WPSRequest(object):
    """ _WPSRequest

    Replaces owslibs http querying for get_capabilities, describe_process and
    execute.
    """
    def __init__(self, base_url, **kwargs):
        self._base_url = base_url
        self._username = kwargs.get('username', None)
        self._password = kwargs.get('password', None)
        self._accept_versions = kwargs.get('accept_versions', None)
        self._language = kwargs.get('language', None)
        self._session = requests.Session()

    def _base_params(self, request):
        """ Generates base parameters for all requests. """
        params = {
            'service': 'WPS',
            'request': request,
        }

        if self._accept_versions:
            params['AcceptVersions'] = self._accept_versions

        if self._language:
            params['language'] = self._language

        return params

    def _auth(self):
        """ Formats authentication for requests library. """
        if self._username and self._password:
            return (self._username, self._password)

        return None

    def get_capabilities(self, method='GET'):
        """ Calls GetCapabilities endpoint. """
        if method.lower() == 'post':
            raise NotImplementedError('GetCapabilities POST request is not supported.')

        params = self._base_params('GetCapabilities')

        try:
            response = self._session.get(self._base_url,
                                         params=params,
                                         cookies=self._session.cookies,
                                         auth=self._auth())

            logger.debug('GetCapabilites\n%s', urllib.unquote(response.url))
        except ConnectionError as e:
            raise WPSServerError('GetCapabilities Request failed, check logs.')

        return etree.fromstring(response.text.encode('utf-8'))

    def describe_process(self, identifier, version='1.0.0', method='GET'):
        """ Calls DescribProcess endpoint. """
        if method.lower() == 'post':
            raise NotImplementedError('DescribeProcess POST request is not supported.')

        params = self._base_params('DescribeProcess')

        params['version'] = version

        if isinstance(identifier, (list, tuple)):
            params['Identifier'] = ','.join(identifier)
        else:
            params['Identifier'] = identifier

        try:
            response = self._session.get(self._base_url,
                                         params=params,
                                         cookies=self._session.cookies,
                                         auth=self._auth())

            logger.debug('DescribeProcess\n%s', urllib.unquote(response.url))
        except ConnectionError as e:
            raise WPSServerError('DescribeProcess Request failed, check logs.')

        return etree.fromstring(response.text.encode('utf-8'))

    def execute(self, identifier, version='1.0.0', method='POST', **kwargs):
        """ Calls Execute endpoint. """
        params = self._base_params('Execute')

        params['version'] = version
        params['Identifier'] = identifier

        data = kwargs.get('data', '')

        try:
            if method.lower() == 'get':
                params['datainputs'] = '[%s]' % (data.replace(' ', ''),)

                response = self._session.get(self._base_url,
                                             params=params,
                                             auth=self._auth())

                logger.debug('Query\n%s', urllib.unquote(response.url))
                logger.debug('Execute response\n%s', response.text)
            elif method.lower() == 'post':
                # Check for CSRF token
                csrf_token = None

                for cookie in self._session.cookies:
                    if 'csrf' in cookie.name.lower():
                        csrf_token = cookie.value

                # Build headers and payload for CSRF token
                if csrf_token:
                    logger.debug('CSRF token present')

                    payload = {
                        'document': data,
                        'csrfmiddlewaretoken': csrf_token,
                    }

                    headers = {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0',
                    }
                else:
                    payload = data

                    headers = { }

                response = self._session.post(self._base_url,
                                              data=payload,
                                              headers=headers,
                                              cookies=self._session.cookies,
                                              auth=self._auth())

                # Grabbed from owslib to handle the execute response
                if response.status_code in [400, 401]:
                    raise ServiceException(response.text)

                if response.status_code in [404, 500, 502, 503, 504]:
                    response.raise_for_status()

                valid_content = [
                    'text/xml',
                    'application/xml',
                    'application/vnd.ogc.se_xml',
                ]

                if 'Content-Type' in response.headers and response.headers['Content-Type'] in valid_content:
                    se_tree = etree.fromstring(response.content)

                    possible_errors = [
                        '{http://www.opengis.net/ows}Exception',
                        '{http://www.opengis.net/ows/1.1}Exception',
                        '{http://www.opengis.net/ogc}ServiceException',
                        'ServiceException'
                    ]

                    for possible_error in possible_errors:
                        serviceException = se_tree.find(possible_error)

                        if serviceException is not None:
                            raise ServiceException('\n'.join([str(t).strip() for t in serviceException.itertext() if str(t).strip()]))
    
                xml_response = ResponseWrapper(response).read()

                logger.debug('Execute server response\n%s', xml_response)

                response = etree.fromstring(xml_response)
            else:
                raise WPSClientError('HTTP %s method is not supported' % (method,))
        except ConnectionError as e:
            raise WPSServerError('Execute Request failed, check logs.')

        return response

class WPS(object):
    """ Web Processing Service client.

    Describes a WPS server. Processes can be retrieved from WPS and executed.

    >>> wps = WPS('http://localhost/wps/')

    Print debugrmation about WPS server.

    >>> wps.identification
    >>> wps.provider

    Retrieve a process.

    >>> averager = wps.get_process('averager.mv')

    Attributes:
    url: A String of a path to a WPS server.
    username: A String username.
    password: A String password.
    """
    def __init__(self, url, username=None, password=None, **kwargs):
        """ Inits WebProcessingService """
        self._url = url

        if kwargs.get('log'):
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            logger.setLevel(logging.DEBUG)

            std_handler = logging.StreamHandler(sys.stdout)
            std_handler.setFormatter(formatter)
            logger.addHandler(std_handler)

            log_file = kwargs.get('log_file')

            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

        self._service = _WPSRequest(url, username=username, password=password)

        self._identification = None
        self._provider = None
        self._processes = []

        self._init = False

    def init(self, force=False):
        """ Executes WPS GetCapabilites request.

        Retrieves a servers description data (identification and provider)
        and its processes.

        """
        if not self._init or force:
            if not self._init:
                self._init = True

            logger.debug('Retrieving capabilities')

            capabilities = self._service.get_capabilities()

            wps = WebProcessingService(self._url, skip_caps=True)

            wps._parseCapabilitiesMetadata(capabilities)

            logger.debug('Populating identifer, provider and contact debug')

            ident = wps.identification

            self._identification = dict((x, getattr(ident, x))
                                        for x in _IDENTIFICATION)

            prov = wps.provider

            self._provider = dict((x, getattr(prov, x))
                                  for x in _PROVIDER)

            cont = self._provider['contact']

            self._provider['contact'] = dict((x, getattr(cont, x))
                                             for x in _CONTACT)

            del self._processes[:]

            logger.debug('Populating processes')

            for process in wps.processes:
                self._processes.append(process.identifier)

    @property
    def identification(self):
        """ Returns identification data as JSON. """
        self.init()

        return self._identification

    @property
    def provider(self):
        """ Returns provider data as JSON. """
        self.init()

        return self._provider

    def get_process(self, name):
        """ Returns process from name. """
        self.init()

        if name not in self._processes:
            raise WPSClientError('No process named \'%s\' was found.' % (name,))

        return Process.from_identifier(self, name)

    def execute(self, identifier, inputs, store=False, status=False, method='GET'):
        """ Formats data and executs WPS process. """
        logger.debug('Executing "%s" at "%s" using HTTP %s method', identifier, self._url, method)

        if method.lower() == 'get':
            params = {}

            for k, v in inputs.iteritems():
                params[k] = json.dumps(v)

            params_kv = ['%s=%s' % (k, v) for k, v in params.iteritems()]

            params_kv = ';'.join(params_kv)

            logger.debug('DataInputs:\n%s', params_kv)

            response = self._service.execute(identifier, data=params_kv, method=method)

            execution = WPSExecution()

            execution.parseResponse(etree.fromstring(response.text.encode('utf-8')))
        elif method.lower() == 'post':
            execution = WPSExecution()

            params_kv = [(k, json.dumps(v)) for k, v in inputs.iteritems()]

            output = None
            
            if store and status:
                output = 'output'

            xml_data = execution.buildRequest(identifier, params_kv, output)

            if store and stastu:
                request_document = xml_data.xpath(
                    '/wps100:Execute/wps100:ResponseForm/wps100:ResponseDocument',
                    namespaces=xml_data.nsmap)[0]
        
                request_document.set('status', str(status))
                request_document.set('storeExecuteResponse', str(store))

            xml_data = etree.tostring(xml_data)

            logger.debug('HTTP body:\n%s', xml_data)
            
            response = self._service.execute(identifier, data=xml_data, method=method)

            execution.parseResponse(response)
        else:
            raise WPSClientError('HTTP method %s is not supported' % (method,))

        return execution

    def __iter__(self):
        for proc in self._processes:
            yield Process.from_identifier(self, proc)

    def __repr__(self):
        return 'WPS(url=%r, service=%r)' % (self._url, self._service)

    def __str__(self):
        return json.dumps({
            'identification': self.identification,
            'provider': self.provider},
                          indent=4)
