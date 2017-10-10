""" A WPS Client """

import json
import logging
import re
import sys, urllib
import xml.etree.ElementTree
import time
import requests
from lxml import etree

import cwt
from cwt.wps_lib import metadata
from cwt.wps_lib import operations

logger = logging.getLogger('cwt.wps')

class WPSError(Exception):
    pass

class WPSHTTPError(Exception):
    pass

class WPSHTTPMethodError(Exception):
    pass

class WPS(object):
    def __init__(self, url, username=None, password=None, **kwargs):
        """ WPS class

        An class to connect and communicate with a WPS server implementing
        the ESGF-CWT API.

        Supports two authentication methods, username/password or api_key.
        
        Attributes:
            url: A string url path for the WPS server.
            username: A string username.
            password: A string password.
            api_key: A string API_KEY for the WPS server.
            version: A string version of the WPS server.
            language: A string language code for the WPS server to communicate in.
            log: A boolean flag to enable logging
            verify: A boolean flag to enable checking of certificates (default = True)
            log_file: A string path for a log file.
        """
        self.__url = url
        self.__username = username
        self.__password = password
        self.__version = kwargs.get('version')
        self.__language = kwargs.get('language')
        self.__api_key = kwargs.get('api_key')
        self.__verify = kwargs.get('verify',True)
        self.__capabilities = None 
        self.__csrf_token = None
        self.__client = requests.Session()

        if kwargs.get('log') is not None:
            formatter = logging.Formatter('[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

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

    def capabilities(self, parse=True ):
        """ Attempts to retrieve and return the WPS servers capabilities document. """
        if self.__capabilities == None:
            self.__capabilites = self.__get_capabilities(parse=parse)

        return self.__capabilities

    def getCapabilities( self, cap_type="", parse=True ):
        return self.__get_capabilities( identifier=cap_type, parse=parse ) if( cap_type ) else self.capabilities(parse=parse)

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

        try:
            logger.debug( "Sending request to url: {0}, params = {1}, data = {2}, headers={3}".format(url,str(params),str(data),str(headers)))
            response = self.__client.request(method, url, params=params, data=data, headers=headers, verify=self.__verify )
        except requests.RequestException, err:
            raise WPSHTTPError('{0} request failed: {1}'.format(method,str(err)))

        logger.debug('%s request succeeded', method)

        logger.debug('Response headers %s', response.headers)

        logger.debug('Response cookies %s', response.cookies)

        if 'csrftoken' in response.cookies:
            self.__csrf_token = response.cookies['csrftoken']

        if response.status_code != 200:
            raise WPSHTTPError('{0} response failed with status code '
                    '{1} {2}'.format(method, response.status_code, response.content))

        return response.text

    def status( self, process ):
        href = process.hrefs.get("status")
        toks = href.split('?')
        url = toks[0]
        parm_toks = toks[1].split('=')
        params = { parm_toks[0]: parm_toks[1] }
        headers = {}
        response = self.__http_request("get", url, params, None, headers)
        process.response = xml.etree.ElementTree.fromstring( response )
        status = "UNKNOWN"
        for ref in process.response.iter( '{http://www.opengis.net/wps/1.0.0}Status' ):
            if   ref.find("{http://www.opengis.net/wps/1.0.0}ProcessAccepted"): status = "QUEUED"
            elif ref.find("{http://www.opengis.net/wps/1.0.0}ProcessStarted"): status = "EXECUTING"
            elif ref.find("{http://www.opengis.net/wps/1.0.0}ProcessFinished"): status = "COMPLETED"
            elif ref.find("{http://www.opengis.net/wps/1.0.0}ProcessFailed"): status = "ERROR"
        return status


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

        logger.info('{}'.format(response))

        return response

    def __parse_response(self, response, response_type):
        """ Attempts to parse the WPS response.

        Args:
            response: A string WPS response.
            response_type: A class we want to attempt to parse.

        Returns:
            A class containing the parsed WPS response.

        Raises:
            WPSError: An ExceptionReport was returned from the WPS server.
        """
        data = None

        try:
            data = response_type.from_xml(response)
        except Exception:
            raise
        else:
            return data

        if data is None:
            try:
                data = metadata.ExceptionReport.from_xml(response)
            except Exception:
                raise WPSError('Failed to parse server response')
            else:
                raise WPSError(data)

    def __get_capabilities(self, method='GET', identifier='', parse=True ):
        """ Builds and attempts a GetCapabilities request. """
        params = {
                'service': 'WPS',
                'request': 'GetCapabilities',
                }
        if( identifier ):
            params['identifier'] = identifier

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

        capabilities = self.__parse_response(response, operations.GetCapabilitiesResponse) if(parse) else operations.GetCapabilitiesResponse

        return capabilities

    def processes(self, regex=None, refresh=False, method='GET'):
        """ Returns a list of WPS processes.

        Args:
            regex: A string regex used to filter the processes by identifier.
            refresh: A boolean to force a GetCapabilites refresh.
            method: A string HTTP method.

        Returns:
            A GetCapabilities object.
        """
        if self.__capabilities is None or refresh:
            self.__capabilities = self.__get_capabilities(method)

        return [cwt.Process(x) for x in self.__capabilities.process_offerings]

    def get_process(self, identifier, method='GET'):
        """ Return a specified process.
        
        Args:
            identifier: A string process identifier.

        Returns:
            The specified process instance.

        Raises:
            Exception: A process with identifier was not found.
        """
        if self.__capabilities is None:
            self.__capabilities = self.__get_capabilities(method)

        try:
            return [cwt.Process(x) for x in self.__capabilities.process_offerings
                    if x.identifier == identifier][0]
        except IndexError:
            raise Exception('Failed to find process with identifier "{}"'.format(identifier))

    def describe(self, process, method='GET'):
        """ Return a DescribeProcess response.
        
        Args:
            process: An object of type Process to describe.
            method: A string HTTP method to use.

        Returns:
            A DescribeProcessResponse object.
        """
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

    def __execute_post_data(self, data_inputs, base_params):
        """ Attempts to execute an HTTP Post request. """
        request = operations.ExecuteRequest()

        base_params['data_inputs'] = []

        for key, value in data_inputs.iteritems():
            logger.info('Setting input {} to {}'.format(key, value))

            inp = metadata.Input()

            inp.identifier = key

            inp_data = metadata.ComplexData()

            inp_data.value = '{0}'.format(value)

            inp.data = inp_data

            base_params['data_inputs'].append(inp) 

        return request(**base_params)

    def download_result( self, op ):
        status = self.status( op )
        logger.info( "STATUS: " +  status )
        while status == "QUEUED" or status == "EXECUTING":
            time.sleep(1)
            status = self.status( op )
            logger.info( "STATUS: " +  status )
        if status == "COMPLETED":
            file_href = op.hrefs.get("file")
            file_path = "/tmp/" + file_href.split('/')[ -1 ]
            urllib.urlretrieve (file_href, file_path )
            return file_path
        else:
            print xml.etree.ElementTree.tostring( op.response )
            return ""



    def execute(self, process, inputs=None, domain=None, async=True, method='GET', **kwargs):
        """ Execute the process on the WPS server. 
        
        Args:
            process: A Process object to be executed on the WPS server.
            inputs: A list in Variables/Processes.
            domain: A Domain object to be used.
            async:  A bool determining async (True) or sync (False) execution.
            kwargs: A dict containing additional arguments.
        """
        if inputs is None:
            inputs = []

        params = {
                'service': 'WPS',
                'request': 'Execute',
                'version': '1.0.0',
                'identifier': process.identifier,
                'status': str(async).lower()
                }

        if method.lower() == 'get':
            params['datainputs'] = self.prepare_data_inputs(process, inputs, domain, **kwargs)

            response = self.__request(method, params=params)
        elif method.lower() == 'post':
            data_inputs = self.__prepare_data_inputs(process, inputs, domain, **kwargs)

            data = self.__execute_post_data(data_inputs, params)

            response = self.__request(method, data=data)
        else:
            raise WPSHTTPMethodError('{0} is an unsupported method'.format(method))

#        process.response = self.__parse_response(response, operations.ExecuteResponse)
        process.response = xml.etree.ElementTree.fromstring( response )

        for ref in process.response.iter( '{http://www.opengis.net/wps/1.0.0}Reference' ):
            process.hrefs[ ref.attrib.get('id') ] = ref.attrib.get('href')

        logger.info( "HREFS: " + str(process.hrefs) )

#        if isinstance(process.response.status, metadata.ProcessFailed):
#            raise Exception(process.response.status.exception_report)
