""" A WPS Client """

import json
import logging
import re
import sys

import requests
from owslib import wps

from cwt.domain import Domain
from cwt.errors import CWTError
from cwt.errors import WPSClientError
from cwt.process import Process
from cwt.variable import Variable

logger = logging.getLogger('cwt.wps_client')


class WPSClient(object):
    def __init__(self, url, **kwargs):
        """ WPS class

        An class to connect and communicate with a WPS server implementing
        the ESGF-CWT API.

        Attributes:
            url: A string url path for the WPS server.
            api_key: A string that will be passed as the value to COMPUTE-TOKEN HTTP header.
            version: A string version of the WPS server.
            log: A boolean flag to enable logging.
            log_level: A string log level (default: INFO).
            log_file: A string path for a log file.
            verify: A bool to enable/disable verifying a server's TLS certificate.
            cert: A str path to an SSL client cert or a tuple as ('cert', 'key').
            headers: A dict that will be passed as HTTP headers.
        """
        self.log = kwargs.get('log', False)

        self.log_file = None

        if self.log:
            log_level = kwargs.get('log_level', 'info').upper()

            root_logger = logging.getLogger()

            root_logger.setLevel(log_level)

            formatter = logging.Formatter(
                '[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            stream_handler = logging.StreamHandler(sys.stdout)

            stream_handler.setFormatter(formatter)

            stream_handler.setLevel(log_level)

            root_logger.addHandler(stream_handler)

            logger.info('Added stdout handler')

            self.log_file = kwargs.get('log_file', None)

            if self.log_file is not None:
                file_handler = logging.FileHandler(self.log_file)

                file_handler.setFormatter(formatter)

                file_handler.setLevel(log_level)

                root_logger.addHandler(file_handler)

                logger.info('Added file handle %s', self.log_file)

        self.headers = kwargs.get('headers', {})

        self.api_key = kwargs.get('api_key', None)

        if self.api_key is not None:
            self.headers['COMPUTE-TOKEN'] = self.api_key

        self.verify = kwargs.get('verify', True)

        client_kwargs = {
            'skip_caps': True,
            'headers': self.headers,
            'verify': self.verify,
            'verbose': True if self.log else False,
        }

        self.version = kwargs.get('version', None)

        if self.version is not None:
            client_kwargs['version'] = self.version

        self.cert = kwargs.get('cert', None)

        if self.cert is not None:
            client_kwargs['cert'] = self.cert

        logger.info('Initialize OWSLib with %r', client_kwargs)

        self.url = url

        self.client = wps.WebProcessingService(self.url, **client_kwargs)

        self._has_capabilities = False

    def __repr__(self):
        return ('WPSClient(url={!r}, log={!r}, log_file={!r}, '
                'verify={!r}, version={!r}, cert={!r}, headers={!r})').format(
                    self.url, self.log, self.log_file, self.verify,
                    self.cert, self.version, self.headers)

    def get_capabilities(self, method='get'):
        """ Executes a GetCapabilities request."""
        self.client.getcapabilities()

        self._has_capabilities = True

    def describe_process(self, process):
        """ Executes a DescribeProcess request."""
        description = self.client.describeprocess(process.identifier)

        new_process = Process.from_owslib(description)

        new_process.inputs = process.inputs

        new_process.domain = process.domain

        new_process.parameters = process.parameters

        return new_process

    def parse_wps_execute_get_params(self, kwargs):
        params = {}

        param_names = ('ResponseDocument', 'RawDataOutput', 'storeExecuteResponse',
                       'lineage', 'status')

        for name in param_names:
            if name in kwargs:
                params[name] = kwargs.pop(name)

        return params

    def execute(self, process, inputs=None, domain=None, **kwargs):
        """ Executes an Execute request.

        kwargs will be passed to cwt.Process.add_parameters, see this method for additional
        documentation.

        If method is set to GET then you may pass any of the following WPS Execute parameters:
        (ResponseDocument, RawDataOutput, storeExecuteResponse, lineage, status). See the
        WPS document at (http://portal.opengeospatial.org/files/?artifact_id=24151).

        Examples:
            client = cwt.WPSClient(...)

            client.execute(proc, inputs=v0)

            client.execute(proc, inputs=[v0, v1], domain=d0)

            client.execute(proc, inputs=[v0, v1], domain=d0, method='GET')

            client.execute(proc, inputs=v0, axes='time')

            client.execute(proc, inputs=v0, axes=['lat', 'lon])

        NOTES:
            * `inputs` will be merged with existing values of `process.inputs`
            * `domain` will override the value of `process.domain`
            * `kwargs` will be merged with existing values of `process.parameters`

        Args:
            process: An instance of cwt.Process.
            inputs: An instance of cwt.Variable or a list of cwt.Variable.
            domain: An instance of cwt.Domain.
            method: A str HTTP method (GET or POST).
            **kwargs: See above description.
        """
        if inputs is None:
            inputs = []
        elif not isinstance(inputs, (list, tuple)):
            inputs = [inputs, ]

        method = kwargs.pop('method', 'post').lower()

        if method == 'post':
            variable, domain, operation = self.prepare_data_inputs(process, inputs, domain, **kwargs)

            variable = wps.ComplexDataInput(variable, mimeType='application/json')

            domain = wps.ComplexDataInput(domain, mimeType='application/json')

            operation = wps.ComplexDataInput(operation, mimeType='application/json')

            data_inputs = [('variable', variable), ('domain', domain), ('operation', operation)]

            try:
                process.context = self.client.execute(process.identifier, data_inputs)
            except Exception as e:
                raise WPSClientError('Client error {!r}', str(e))
        elif method == 'get':
            params = self.parse_wps_execute_get_params(kwargs)

            variable, domain, operation = self.prepare_data_inputs(process, inputs, domain, **kwargs)

            variable = 'variable={!s}'.format(variable)

            domain = 'domain={!s}'.format(domain)

            operation = 'operation={!s}'.format(operation)

            data_inputs = ';'.join([variable, domain, operation])

            try:
                params.update({
                    'service': 'WPS',
                    'request': 'Execute',
                    'version': '1.0.0',
                    'Identifier': process.identifier,
                    'DataInputs': data_inputs.replace(' ', ''),
                })

                extras = {
                    'verify': self.verify,
                }

                if self.cert is not None:
                    extras['cert'] = self.cert

                logger.debug('params %r extras %r', params, extras)

                response = requests.get(self.url, params=params, headers=self.headers, **extras)

                logger.debug('Request url %r', response.url)

                response_text = response.text.encode('utf-8')

                logger.debug('Response %r', response_text)

                process.context = self.client.execute(process.identifier, None, request=response.url,
                                                      response=response_text)
            except Exception as e:
                raise WPSClientError('Client error {!r}', str(e))
        else:
            raise WPSClientError('Unsupported method {!r}', method)

    def processes(self, pattern=None):
        if not self._has_capabilities:
            self.get_capabilities()

        items = []

        logger.info('Matching against pattern %r', pattern)

        for x in self.client.processes:
            logger.info('Checking %r', x)

            if pattern is not None:
                try:
                    if re.match(pattern, x.identifier):
                        items.append(Process.from_owslib(x))
                except re.error:
                    raise CWTError(
                        'Invalid pattern, see python\'s "re" module for documentation')
            else:
                items.append(Process.from_owslib(x))

        return items

    def process_by_name(self, identifier, version=None):
        if not self._has_capabilities:
            self.get_capabilities()

        matches = []

        for x in self.client.processes:
            if x.identifier == identifier:
                matches.append(x)

        if len(matches) == 0:
            raise CWTError('No matching process {!r}', identifier)

        process = None

        if version is None:
            matches = sorted(matches, key=lambda x: x.processVersion)

            process = Process.from_owslib(matches[-1])
        else:
            for x in matches:
                if x.processVersion == version:
                    process = Process.from_owslib(x)

                    break

        if process is None:
            raise CWTError('No matching process {!r} version {!r}', identifier, version)

        return process

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
        match = re.search(r'\[(.*)\]', data_inputs)

        kwargs = dict((x.split('=')[0], json.loads(x.split('=')[1]))
                      for x in match.group(1).split(';'))

        variables = [Variable.from_dict(x) for x in kwargs.get('variable', [])]

        domains = [Domain.from_dict(x) for x in kwargs.get('domain', [])]

        operation = [Process.from_dict(x) for x in kwargs.get('operation', [])]

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
        temp_process = process.copy()

        domains = {}

        if domain is not None:
            domains[domain.name] = domain

            temp_process.domain = domain

        if not isinstance(inputs, (list, tuple)):
            inputs = [inputs, ]

        temp_process.inputs.extend(inputs)

        if 'gridder' in kwargs:
            temp_process.gridder = kwargs.pop('gridder')

        temp_process.add_parameters(**kwargs)

        processes, variables = temp_process.collect_input_processes()

        # Collect all the domains from nested processes
        for item in processes.values():
            if item.domain is not None and item.domain.name not in domains:
                domains[item.domain.name] = item.domain

        variable = json.dumps([x.to_dict() for x in variables.values()])

        domain = json.dumps([x.to_dict() for x in domains.values()])

        operation = json.dumps([x.to_dict() for x in processes.values()])

        return variable, domain, operation
