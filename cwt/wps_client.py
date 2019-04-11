""" A WPS Client """

import json
import logging
import re
import sys

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
            log: A boolean flag to enable logging
            log_file: A string path for a log file.
            verify: A bool to enable/disable verifying a server's TLS certificate.
            cert: A str path to an SSL client cert or a tuple as ('cert', 'key').
            headers: A dict that will be passed as HTTP headers.
        """
        self.log = kwargs.get('log', False)

        self.log_file = None

        if self.log:
            root_logger = logging.getLogger()

            root_logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '[%(asctime)s][%(filename)s[%(funcName)s:%(lineno)d]] %(message)s')

            stream_handler = logging.StreamHandler(sys.stdout)

            stream_handler.setFormatter(formatter)

            stream_handler.setLevel(logging.DEBUG)

            root_logger.addHandler(stream_handler)

            logger.info('Added stdout handler')

            self.log_file = kwargs.get('log_file', None)

            if self.log_file is not None:
                file_handler = logging.FileHandler(self.log_file)

                file_handler.setFormatter(formatter)

                file_handler.setLevel(logging.DEBUG)

                root_logger.addHandler(file_handler)

                logger.info('Added file handle %s', self.log_file)

        headers = kwargs.get('headers', {})

        self.api_key = kwargs.get('api_key', None)

        if self.api_key is not None:
            headers['COMPUTE-TOKEN'] = self.api_key

        self.verify = kwargs.get('verify', True)

        client_kwargs = {
            'skip_caps': True,
            'headers': headers,
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
                'verify={!r}, version={!r}, cert={!r})').format(
                    self.url, self.log, self.log_file, self.verify,
                    self.cert, self.version)

    def get_capabilities(self):
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

    def execute(self, process, inputs=None, domain=None, **kwargs):
        """ Executes an Execute request."""
        if inputs is None:
            inputs = []

        data_inputs = self.prepare_data_inputs(
            process, inputs, domain, **kwargs)

        try:
            process.context = self.client.execute(
                process.identifier, data_inputs)
        except Exception as e:
            raise WPSClientError('Client error {!r}', str(e))

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

    def process_by_name(self, identifier):
        if not self._has_capabilities:
            self.get_capabilities()

        for x in self.client.processes:
            if x.identifier == identifier:
                return Process.from_owslib(x)

        return None

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
        domains = {}

        if domain is not None:
            domains[domain.name] = domain.to_dict()

        process.inputs.extend(inputs)

        process.add_parameters(**kwargs)

        processes, variables = process.collect_input_processes()

        processes.append(process)

        variables.extend(inputs)

        variables = wps.ComplexDataInput(json.dumps([x.to_dict() for x in variables]),
                                         mimeType='application/json')

        # Collect all the domains from nested processes
        for item in processes:
            if item.domain is not None and item.domain.name not in domains:
                domains[item.domain.name] = item.domain.to_dict()

        domains = wps.ComplexDataInput(json.dumps(list(domains.values())),
                                       mimeType='application/json')

        operation = wps.ComplexDataInput(json.dumps([item.to_dict() for item in processes]),
                                         mimeType='application/json')

        return [('variable', variables), ('domain', domains),
                ('operation', operation)]

    def prepare_data_inputs_str(self, process, inputs, domains, **kwargs):
        data_inputs = self.prepare_data_inputs(
            process, inputs, domains, **kwargs)

        items = []

        for name, value in data_inputs:
            items.append('{!s}={!s}'.format(name, value))

        items_joined = ';'.join(items)

        return '[{!s}]'.format(items_joined)
