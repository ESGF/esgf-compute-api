"""
Process Unittest.
"""

import re
import json

from unittest import TestCase

from mock import patch, Mock, call

from esgf import WPS
from esgf import Process
from esgf import Variable
from esgf import Dimension
from esgf import Domain
from esgf import WPSServerError

from . import MockPrint

# pylint: disable=protected-access
class TestProcess(TestCase):
    """ Process Test Case. """

    def test_output(self):
        """ Process output. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'test.echo')

        process._result = Mock(processOutputs=[])

        with self.assertRaises(WPSServerError):
            print process.output

        mock_output = Mock()
        mock_output.data = [
            "{\"uri\": \"file://test.nc\", \"id\": \"ta\", " +
            "\"domain\": \"d0\", \"mime_type\": " +
            "\"application/netcdf\"}"]

        process._result.processOutputs.append(mock_output)

        output = process.output

        self.assertEqual(output.uri, 'file://test.nc')
        self.assertEqual(output.var_name, 'ta')
        self.assertIsNotNone(output.domains)
        self.assertEqual(output.mime_type, 'application/netcdf')

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

    @patch('esgf.wps.WPS')
    def test_execute(self, mock_wps):
        """ Test simple execute. """
        wps = mock_wps.return_value

        process = Process.from_name(wps, 'OP', 'test')

        self.assertIsNotNone(process)

        variable = Variable('collection://MERRA/mon/atmos', 'ta', name='v0')

        lat = Dimension.from_single_value(45, name='lat')
        lon = Dimension.from_single_value(30, name='lon')
        lev = Dimension.from_single_value(7500, name='lev')

        domain0 = Domain([lat, lon, lev], name='d0')

        process.execute(variable, [domain0], [domain0])

        parameters = {
            'variable': json.dumps(variable.parameterize()),
            'domain': json.dumps([domain0.parameterize()]),
            'operation': 'd0',
        }

        expected = [
            call.execute('OP.test', parameters, status=False, store=False)
        ]

        self.assertEqual(wps.mock_calls, expected)

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
