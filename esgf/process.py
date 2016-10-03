"""
Process Module.
"""

import json

from tempfile import NamedTemporaryFile

from .errors import WPSServerError
from .operation import Operation
from .variable import Variable

class Process(object):
    """ Process.

    Represents the operation that will be peformed.

    Can be created from the Process class but there is no checking if the 
    process actually exists on the server.

    >>> wps = WPS('http://localhost/wps/')
    >>> averager = Process.from_identifier(wps, 'averager.mv')

    To retrieve a process that is known to be on the server use WPS.

    >>> averager = wps.get_process('averager.mv')
   
    Attributes:
        wps: A WPS instance pointing the a WPS server.
        operation: An Operation that will be executed by the process.
    """
    def __init__(self, wps, operation):
        """ Process init. """
        self._wps = wps
        self._result = None
    
        self._variable = {}
        self._domain = {}
        self._operation = operation

    @classmethod
    def from_identifier(cls, wps, identifier):
        """ Helper create process from identifer. """
        operation = Operation(identifier)

        return cls(wps, operation)

    @property
    def name(self):
        """ Process name. """
        return self._operation.identifier

    @property
    def status(self):
        """ Process status. """
        return self._result.status

    @property
    def message(self):
        """ Process message. """
        return self._result.statusMessage

    @property
    def progress(self):
        """ Process progress. """
        return self._result.percentCompleted

    @property
    def output(self):
        """ Process output. """
        if not self._result.isSucceded():
            raise WPSServerError(
                'Process has no output, possibly process execution error.')

        output = None

        with NamedTemporaryFile() as temp_file:
            self._result.getOutput(temp_file.name)

            json_obj = json.load(temp_file)

            output = Variable.from_dict(json_obj, self._domain)

        return output

    def check_status(self, sleep_secs=0):
        """ Retrieves latest status from server. """
        if not self._result.statusLocation:
            raise WPSServerError('Process \'%s\' doesn\'t support status.' %
                                 (self.name,))

        self._result.checkStatus(sleepSecs=sleep_secs)

    def __nonzero__(self):
        """ Returns true while process is still executing. """
        self.check_status()

        return True if self.status.lower() != 'processsucceeded' else False

    def execute(self, inputs=None, domain=None, parameters=None, store=False, status=False):
        """ Passes process parameters to WPS to execute. """
        if inputs:
            for inp in inputs:
                self._operation.add_input(inp)

        if domain:
            self._operation.domain = domain

        if parameters:
            for param in parameters:
                self._operation.add_parameter(param)

        self._variable, self._domain = self._operation.gather()

        datainputs = {
            'variable': [x.parameterize() for x in self._variable.values()],
            'domain': [x.parameterize() for x in self._domain.values()],
            'operation': self._operation.flatten(),
        }

        self._result = self._wps.execute(self._operation.identifier,
                                         datainputs,
                                         status=status,
                                         store=store)

    def __repr__(self):
        return 'Process(wps=%r, operation=%r)' % (self._wps, self._operation)

    def __str__(self):
        return self.name
