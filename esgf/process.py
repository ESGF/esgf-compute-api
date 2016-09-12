"""
Process Module.
"""

import json

from tempfile import NamedTemporaryFile

from .errors import WPSServerError
from .operation import Operation
from .variable import Variable

class Process(object):
    """ Process class.

    """
    def __init__(self, wps, operation):
        """ Process init. """
        self._wps = wps
        self._operation = operation
        self._result = None

    @classmethod
    def from_name(cls, wps, method, kernel):
        """ Helper crate process from method and kernel. """
        operation = Operation(method, kernel)

        return cls(wps, operation)

    @classmethod
    def from_identifier(cls, wps, identifier):
        """ Helper create process from identifer. """
        method, kernel = identifier.split('.')

        operation = Operation(method, kernel)

        return cls(wps, operation)

    @property
    def name(self):
        """ Process name. """
        return self._operation.name

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

            output = Variable.from_dict(json_obj, self._domains)

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

    def execute(self, variable, domains, parameters=None, store=False, status=False):
        """ Passes process parameters to WPS to execute. """
        if parameters:
            for param in parameters:
                self._operation.add_parameter(param)

        self._domains = dict((x.name, x) for x in domains)

        inputs = {
            'domain': json.dumps([x.parameterize() for x in domains]),
            'variable': json.dumps(variable.parameterize()),
            'operation': self._operation.parameterize(),
        }

        self._result = self._wps.execute(self._operation.name,
                                         inputs,
                                         store=store,
                                         status=status)

    def __repr__(self):
        return 'Process(wps=%r, operation=%r)' % (self._wps, self._operation)

    def __str__(self):
        return self.name
