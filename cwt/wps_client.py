""" A WPS Client """

from builtins import str
from builtins import object
import json
import logging
import os
import re
import sys
import collections
import warnings

logger = logging.getLogger(__name__)

import requests
from owslib import util

s = requests.Session()

__request = util.requests.request

# Monkey patch owslib to handle CSRF token.
def _request(method, *args, **kwargs):
    if method == 'POST':
        response = s.get(*args, **kwargs)

        if 'headers' in kwargs:
            try:
                kwargs['headers'].update({'X-CSRFToken': response.cookies['csrftoken']})
            except KeyError:
                logger.info('Did not find "csrftoken" in response coockies')

    return s.request(method, *args, **kwargs)

util.requests.request = _request

from owslib import wps

from cwt import auth
from cwt import utilities
from cwt.domain import Domain
from cwt.errors import CWTError
from cwt.errors import WPSClientError
from cwt.process import Process
from cwt.variable import Variable

class TokenAuthentication():
    pass


class ProcessCollection(collections.OrderedDict):
    def __getattr__(self, name):
        if name in self:
            return self[name]

        raise AttributeError(name)


class WPSClient(object):
    def __init__(self, url, **kwargs):
        """ WPS class

        An class to connect and communicate with a WPS server implementing
        the ESGF-CWT API.

        Attributes:
            url: A string url path for the WPS server.
            version: A string version of the WPS server.
            log: A boolean flag to enable logging.
            log_level: A string log level (default: INFO).
            verify: A bool to enable/disable verifying a server's TLS certificate.
            cert: A str path to an SSL _client cert or a tuple as ('cert', 'key').
            headers: A dict that will be passed as HTTP headers.
        """
        self.set_logging(kwargs)

        self.headers = kwargs.get('headers', {})

        self.cert = kwargs.get('cert', None)

        self.verify = kwargs.pop('verify', True)

        self.auth = kwargs.get('auth', None)

        owslib_auth_kwargs = {
            'username': kwargs.pop('username', None),
            'password': kwargs.pop('password', None),
            'verify': self.verify,
            'cert': self.cert,
        }

        owslib_auth = util.Authentication(**owslib_auth_kwargs)

        self.version = kwargs.get('version', '1.0.0')

        _client_kwargs = {
            'skip_caps': True,
            'headers': self.headers,
            'verbose': True if self.log else False,
            'auth': owslib_auth,
            'version': self.version,
        }

        logger.info('Initialize OWSLib with %r', _client_kwargs)

        self.url = url

        self._client = wps.WebProcessingService(self.url, **_client_kwargs)

        self._build_process_collection()

    def __repr__(self):
        return ('WPSClient(url={!r}, log={!r}, log_file={!r}, '
                'verify={!r}, version={!r}, cert={!r}, headers={!r})').format(
                    self.url, self.log, self.log_file, self.verify,
                    self.cert, self.version, self.headers)

    def set_logging(self, kwargs):
        env_log = bool(os.environ.get('WPS_LOG', False))

        env_log_level = os.environ.get('WPS_LOG_LEVEL', 'info')

        self.log = bool(kwargs.get('log', env_log))

        log_level = kwargs.get('log_level', env_log_level).upper()

        if self.log:
            logging.basicConfig(level=log_level)

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

    def _build_process_collection(self):
        self._client.getcapabilities()

        groups = {}

        processes = sorted(self._client.processes, key=lambda x: x.identifier)

        for x in processes:
            process = Process.from_owslib(self, x)

            id_parts = process.identifier.split('.')

            if len(id_parts) == 1:
                name = id_parts[0]

                if 'General' not in groups:
                    groups['General'] = ProcessCollection()

                groups['General'][name] = process
            elif len(id_parts) == 2:
                module, name = id_parts

                if module not in groups:
                    groups[module] = ProcessCollection()

                groups[module][name] = process
            else:
                raise CWTError('Could not group process {!s}.', process.identifier)

        for x, y in groups.items():
            process_list = '\n'.join(sorted([x for x in y]))

            doc = ("Collection of processes for {module!r} module.\n"
                   "\n"
                   "{process_list!s}")

            doc = doc.format(module=x, process_list=process_list)

            setattr(y, '__doc__', doc)

            setattr(self, x, y)

    def processes(self, pattern=None):
        self.get_capabilities()

        items = []

        logger.info('Matching against pattern %r', pattern)

        for x in self._client.processes:
            logger.info('Checking %r', x)

            if pattern is not None:
                try:
                    if re.match(pattern, x.identifier):
                        items.append(Process.from_owslib(self, x))
                except re.error:
                    raise CWTError(
                        'Invalid pattern, see python\'s "re" module for documentation')
            else:
                items.append(Process.from_owslib(self, x))

        return items

    def process_by_name(self, identifier, version=None):
        self.get_capabilities()

        matches = []

        for x in self._client.processes:
            if x.identifier == identifier:
                matches.append(x)

        if len(matches) == 0:
            raise CWTError('No matching process {!r}', identifier)

        process = None

        if version is None:
            matches = sorted(matches, key=lambda x: x.processVersion)

            process = Process.from_owslib(self, matches[-1])
        else:
            for x in matches:
                if x.processVersion == version:
                    process = Process.from_owslib(self, x)

                    break

        if process is None:
            raise CWTError('No matching process {!r} version {!r}', identifier, version)

        return process

    def _repr_html_(self):
        self._client.getcapabilities()

        headers = ('<tr>'
                   '<th>Identifier</td>'
                   '<th>Title</td>'
                   '<th>Process Version</td>'
                   '<th>Status Supported</td>'
                   '<th>Store Supported</td>'
                   '<th style="text-align: left">Abstract</td>'
                   '</tr>')

        rows = []

        max_length = 800

        for x in self._client.processes:
            short_abstract = x.abstract[:max_length] + '...<b>see process for full abstract</b>' if len(x.abstract) > max_length else x.abstract

            r = ('<tr>'
                 '<td>{identifier}</td>'
                 '<td>{title}</td>'
                 '<td>{processVersion}</td>'
                 '<td>{statusSupported}</td>'
                 '<td>{storeSupported}</td>'
                 '<td><pre style="text-align: left">{short_abstract}</pre></td>'
                 '</tr>').format(**x.__dict__, short_abstract=short_abstract)

            rows.append(r)

        table = '<div><table>{}{}</table></div>'.format(headers, ''.join(rows))

        return table

    def get_capabilities(self):
        """ Executes a GetCapabilities request."""
        self._client.getcapabilities()

    def describe_process(self, process):
        """ Executes a DescribeProcess request."""
        process.process = self._client.describeprocess(process.identifier)

        return process

    def parse_wps_execute_get_params(self, kwargs):
        params = {}

        param_names = ('ResponseDocument', 'RawDataOutput', 'storeExecuteResponse',
                       'lineage', 'status')

        for name in param_names:
            if name in kwargs:
                params[name] = kwargs.pop(name)

        return params

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
        data_inputs = utilities.prepare_data_inputs(process, inputs, domain, **kwargs)

        return dict((x, json.dumps(y)) for x, y in data_inputs.items())

    def _patch_authentication(self, headers, params):
        # Prepare headers and GET params
        if self.auth is not None and isinstance(self.auth, auth.Authenticator):
            logger.info("Getting authentication")

            self.auth.prepare(headers, params)

    def _execute_post(self, process, data_inputs, headers):
        variable = wps.ComplexDataInput(data_inputs['variable'], mimeType='application/json')

        domain = wps.ComplexDataInput(data_inputs['domain'], mimeType='application/json')

        operation = wps.ComplexDataInput(data_inputs['operation'], mimeType='application/json')

        data_inputs = [('variable', variable), ('domain', domain), ('operation', operation)]

        self._client.headers.update(headers)

        logger.info("Sending execute request")

        process.context = self._client.execute(process.identifier, data_inputs)

        return process

    def _execute_get(self, process, data_inputs, headers, params):
        data_inputs = ';'.join(['{0!s}={1!s}'.format(x, y) for x, y in data_inputs.items()])

        params.update({
            'service': 'WPS',
            'request': 'Execute',
            'version': self.version,
            'Identifier': process.identifier,
            'DataInputs': data_inputs.replace(' ', ''),
        })

        # Update using same arguments as owslib
        extras = self._client.urlopen_kwargs

        response = requests.get(self.url, params=params, headers=headers, **extras)

        response_text = response.text.encode('utf-8')

        # Let owslib handle the parse of the result
        process.context = self._client.execute(process.identifier, None, request=response.url, response=response_text)

        return process

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
        params = {}
        headers = self.headers.copy()
        method = kwargs.pop('method', 'post').lower()

        logger.info(f"Executing {process.identifier} with {len(process.inputs)}")

        if inputs is not None or domain is not None or len(kwargs) > 0:
            warnings.warn('Use of "inputs", "domain" and setting parameters is deprecated.'
                    'Set theses values on their respective process objects.', DeprecationWarning)

        if inputs is None:
            inputs = []
        elif not isinstance(inputs, (list, tuple)):
            inputs = [inputs, ]

        self._patch_authentication(headers, params)

        try:
            if isinstance(process, Process):
                if method == 'post':
                    data_inputs = self.prepare_data_inputs(process, inputs, domain, **kwargs)

                    process = self._execute_post(process, data_inputs, headers)
                elif method == 'get':
                    extra_params = self.parse_wps_execute_get_params(kwargs)

                    params.update(extra_params)

                    data_inputs = self.prepare_data_inputs(process, inputs, domain, **kwargs)

                    process = self._execute_get(process, data_inputs, headers, params)
                else:
                    raise WPSClientError('Unsupported method {!r}', method)
            elif isinstance(process, str):
                context = self._client.execute(None, None, request=process)

                process = Process()

                process.context = context
        except Exception as e:
            raise WPSClientError(str(e))

        return process
