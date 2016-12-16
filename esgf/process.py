"""
Process Module.
"""

import json

from tempfile import NamedTemporaryFile

from esgf import errors
from esgf import operation
from esgf import variable
from esgf import named_parameter

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
    def from_identifier(cls, wps, identifier, name=None):
        """ Helper create process from identifer. """
        op = operation.Operation(identifier, name=name)

        return cls(wps, op)

    @property
    def name(self):  # pragma: no cover
        """ Process name. """
        return self._operation.identifier

    @property
    def status(self): # pragma: no cover
        """ Process status. """
        return self._result.status

    @property
    def message(self):  # pragma: no cover
        """ Process message. """
        return self._result.message

    @property
    def percent(self):  # pragma: no cover
        """ Process percent. """
        return self._result.percent

    @property
    def output(self):
        """ Process output. """
        if self.status != 'ProcessSucceeded':
            raise errors.WPSServerError(
                'Process has no output, possibly process execution error.')

        output_json = json.loads(self._result.output)

        return variable.Variable.from_dict(output_json)

    def check_status(self, sleep_secs=0):
        """ Retrieves latest status from server. """
        if not self._result.status_location:
            raise errors.WPSServerError('Process \'%s\' doesn\'t '
                                        'support status.' % (self.name,))

        self._result.check_status(sleepSecs=sleep_secs)

    def __nonzero__(self):
        """ Returns true while process is still executing. """
        self.check_status()

        complete = ('ProcessSucceeded', 'ProcessFailed', 'Exception')

        return self.status not in complete

    def execute(self, inputs=None, domain=None, parameters=None, store=False,
                status=False, method='POST',**kargs):
        """ Passes process parameters to WPS to execute. """
        if inputs:
            for inp in inputs:
                self._operation.add_input(inp)

        if domain:
            self._operation.domain = domain

        if parameters:
            for param in parameters:
                self._operation.add_parameter(param)

        for k in kargs:
            self._operation.add_parameter(named_parameter.NamedParameter(k,kargs[k]))

        self._variable, self._domain = self._operation.gather()

        datainputs = {
            'variable': [x.parameterize() for x in self._variable.values()],
            'domain': [x.parameterize() for x in self._domain.values()],
            'operation': self._operation.flatten(),
        }

        self._result = self._wps.execute(self._operation.identifier,
                                         datainputs,
                                         status=status,
                                         store=store,
                                         method=method)

    def __repr__(self): # pragma: no cover
        return 'Process(wps=%r, operation=%r)' % (self._wps, self._operation)

    def __str__(self): # pragma: no cover
        return self.name
