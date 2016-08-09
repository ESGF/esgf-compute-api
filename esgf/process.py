"""
Process Module.
"""

import json

from .errors import WPSServerError
from .operation import Operation

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
        """ Read-only wrapper for operation name. """
        return self._operation.name

    @property
    def status(self):
        """ Remote status property. """
        return self._result.status

    @property
    def message(self):
        """ Remote message property. """
        return self._result.statusMessage

    @property
    def progress(self):
        """ Remote progresss property. """
        return self._result.percentCompleted

    def check_status(self, sleep_secs=0):
        """ Retrieves latest status from server. """
        if not self._result.statusLocation:
            raise WPSServerError('Process \'%s\' doesn\'t support status.' %
                                 (self.name,))

        self._result.checkStatus(sleepSecs=sleep_secs)

    def execute(self, variable, domains, parameters=None, output=None):
        """ Passes process parameters to WPS to execute. """
        if parameters:
            for param in parameters:
                self._operation.add_parameter(param)

        inputs = {
            'domains': json.dumps([x.parameterize() for x in domains]),
            'variable': json.dumps(variable.parameterize()),
            'operation': self._operation.parameterize(),
        }

        self._result = self._wps.execute(self._operation.name, inputs, output)

    def __repr__(self):
        return 'Process(wps=%r, operation=%r)' % (self._wps, self._operation)

    def __str__(self):
        return self.name
