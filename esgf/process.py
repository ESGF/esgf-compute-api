"""
Process Module.
"""

import json

from esgf import Operation

class Process(object):
    """ Process class.

    """
    def __init__(self, wps, operation):
        """ Process init. """
        self._wps = wps
        self._operation = operation

    @classmethod
    def from_name(cls, wps, method, kernel):
        """ Helper function to bypass creating operation. """
        operation = Operation(method, kernel)

        return cls(wps, operation)

    @property
    def name(self):
        """ Read-only wrapper for operation name. """
        return self._operation.name

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

        self._wps.execute(self._operation.name, inputs, output)
