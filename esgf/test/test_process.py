"""
Process Unittest.
"""

import re

from unittest import TestCase

from mock import patch, Mock

from esgf import WPS
from esgf import Process
from esgf import Variable
from esgf import Dimension
from esgf import Domain
from esgf import WPSServerError

from . import MockPrint

class TestProcess(TestCase):
    """ Process Test Case. """

    # pylint: disable=protected-access
    def test_status(self):
        """ Status checking/updating. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'test.echo')

        # Mock _result that would be set from WebProcessingService.execute
        process._result = Mock(
            status='Status',
            statusMessage='Status Message',
            percentCompleted=50.0,
            statusLocation=None)

        # Check library passes back correct values
        self.assertEqual(process.status, 'Status')
        self.assertEqual(process.message, 'Status Message')
        self.assertEqual(process.progress, 50.0)

        # Should throw error when _result.statusLocation is None
        with self.assertRaises(WPSServerError) as ctx:
            process.check_status()

        self.assertEqual(ctx.exception.message,
                         'Process \'test.echo\' doesn\'t support status.')

        # Update statsLocation to check that WPSExecution.checkStatus is called.
        process._result.statusLocation = 'http://localhost:8000/wps/status'
        process._result.checkStatus = Mock()

        process.check_status()

        process._result.checkStatus.assert_called_once()

    def test_from_identifier(self):
        """ Test creating Procress from identifier. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'OP.test')

        self.assertEqual(process.name, 'OP.test')

    def test_from_name(self):
        """ Test creating Process from name. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_name(wps, 'OP', 'test')

        self.assertIsNotNone(process)
        self.assertEqual(process.name, 'OP.test')

    @patch('esgf.wps.WebProcessingService')
    def test_execute(self, mock_service):
        """ Test simple execute. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_name(wps, 'OP', 'test')

        self.assertIsNotNone(process)

        variable = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        lat = Dimension.from_single_value(45, name='lat')
        lon = Dimension.from_single_value(30, name='lon')
        lev = Dimension.from_single_value(7500, name='lev')

        domain0 = Domain([lat, lon, lev], name='d0')

        process.execute(variable, [domain0], [domain0])

        mock_inst = mock_service.return_value

        mock_inst.execute.assert_called_once()

        self.assertEqual(mock_inst.execute.call_args_list[0][0][0], 'OP.test')

    def test_str(self):
        """ Tests __str__. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_name(wps, 'OP', 'test')

        with MockPrint() as ctx:
            print process

        self.assertEqual(ctx.value, 'OP.test\n')

    def test_repr(self):
        """ Tests __repr__. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_name(wps, 'OP', 'test')

        with MockPrint() as ctx:
            print '%r' % (process,)

        self.assertIsNotNone(re.match(r'Process\(wps=.*, operation=.*\)',
                                      ctx.value))
