"""
Process Unittest.
"""

import re
import json

from unittest import TestCase

from mock import patch, Mock, call

from esgf import Gridder
from esgf import WPS
from esgf import Process
from esgf import Variable
from esgf import Dimension
from esgf import Domain
from esgf import WPSClientError
from esgf import WPSServerError
from esgf import NamedParameter
from esgf import Operation

from . import MockPrint

# pylint: disable=protected-access
class TestProcess(TestCase):
    """ Process Test Case. """

    def test_bool(self):
        """ Test status reporting. """

        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'test.echo')
        process.check_status = Mock(return_value=True)
        process._result = Mock(status='test')

        self.assertEqual(bool(process), True)

        process._result.status = 'processsucceeded'

        self.assertEqual(bool(process), False)

    def write_test_output(self, temp_file_path):
        output = {
            'uri': 'file:///test.nc',
            'id': 'ta|v0',
            'domain': [],
            'mime_type': 'application/netcdf',
        }

        with open(temp_file_path, 'w') as temp_file:
            json.dump(output, temp_file)

    def write_bad_test_output(self, temp_file_path):
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write('bad output')

    def test_output(self):
        """ Process output. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'test.echo')

        process._result = Mock()
        process._result.isSucceded.return_value = False

        with self.assertRaises(WPSServerError):
            output = process.output

        process._result.isSucceded.return_value = True
        process._result.getOutput = self.write_test_output

        output = process.output

        self.assertEqual(output.uri, 'file:///test.nc')
        self.assertEqual(output.var_name, 'ta')
        self.assertIsNotNone(output.domains)
        self.assertEqual(output.mime_type, 'application/netcdf')

        process._result.getOutput = self.write_bad_test_output

        with self.assertRaises(WPSClientError) as ctx:
            output = process.output

        self.assertEqual(ctx.exception.message, 'Server did not return any '
                         'valid output')

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

        process = Process.from_identifier(wps, 'OP.test')

        self.assertIsNotNone(process)
        self.assertEqual(process.name, 'OP.test')

    @patch('esgf.wps.WPS')
    def test_multiple_domains(self, mock_wps):
        """ Test passing multiple domains in different components. """
        wps = mock_wps.return_value

        d0 = Domain([Dimension.from_single_value('lat', 45)], name='d0')
        d1 = Domain([Dimension.from_single_value('lev', 7500)], name='d1')

        v0 = Variable('file:///test.nc', 'tas', name='v0', domains=[d0])

        process = Process.from_identifier(wps, 'OP.workflow')

        process.execute([v0], d1, None, False, False)

        expected = [
            call.execute('OP.workflow',
                         {
                             'variable': [
                                 {
                                     'domain': 'd0',
                                     'uri': 'file:///test.nc',
                                     'id': 'tas|v0',
                                 }
                             ],
                             'domain': [
                                 {
                                     'lat': {
                                         'start': 45,
                                         'step': 1,
                                         'end': 45,
                                         'crs': 'values'
                                     },
                                     'id': 'd0',
                                 },
                                 {
                                     'id': 'd1',
                                     'lev': {
                                         'start': 7500,
                                         'step': 1,
                                         'end': 7500,
                                         'crs': 'values',
                                     },
                                 }
                             ],
                             'operation': [
                                 {
                                     'input': ['v0'],
                                     'domain': 'd1',
                                     'name': 'OP.workflow',
                                     'result': process._operation.name,
                                 }
                             ],
                         },
                         method='POST',
                         status=False,
                         store=False),
        ]

        self.assertEqual(expected, wps.mock_calls)

    @patch('esgf.wps.WPS')
    def test_single_process(self, mock_wps):
        """ Tests executing single process. """
        wps = mock_wps.return_value

        process = Process.from_identifier(wps, 'OP.test')

        variable = Variable('file:///test.nc', 'tas', name='v0')

        domain = Domain([
            Dimension.from_single_value("time", 1998),
        ], name='d0')

        axes = NamedParameter('axes', 't')

        process.execute(inputs=[variable], parameters=[axes], domain=domain)

        expected = [
            call.execute('OP.test',
                         {
                             'variable': [
                                 {
                                     'uri': 'file:///test.nc',
                                     'id': 'tas|v0',
                                 }
                             ],
                             'domain': [
                                 {
                                     'id': 'd0',
                                     'time': {
                                         'start': 1998,
                                         'step': 1,
                                         'end': 1998,
                                         'crs': 'values',
                                     },
                                 }
                             ],
                             'operation': [
                                 {
                                     'input': ['v0'],
                                     'domain': 'd0',
                                     'axes': 't',
                                     'name': 'OP.test',
                                     'result': process._operation.name,
                                 }
                             ]
                         },
                         method='POST',
                         status=False,
                         store=False)
        ]

        self.assertEqual(expected, wps.mock_calls)

    @patch('esgf.wps.WPS')
    def test_gridder_variable(self, mock_wps):
        """ Test simple execute. """
        wps = mock_wps.return_value

        process = Process.from_identifier(wps, 'OP.test')

        variable = Variable('file:///test.nc', 'tas', name='v0')

        gridder = Gridder(grid=variable)

        process.execute(parameters=[gridder])

        expected = [
            call.execute('OP.test',
                         {
                             'variable': [
                                 {
                                     'uri': 'file:///test.nc',
                                     'id': 'tas|v0',
                                 },
                             ],
                             'domain': [],
                             'operation': process._operation.flatten(),
                         },
                         method='POST',
                         status=False,
                         store=False)
        ]

        self.assertEqual(expected, wps.mock_calls)

    @patch('esgf.wps.WPS')
    def test_gridder_domain(self, mock_wps):
        """ Test simple execute. """
        wps = mock_wps.return_value

        process = Process.from_identifier(wps, 'OP.test')

        domain = Domain(name='d0')

        gridder = Gridder(grid=domain)

        process.execute(parameters=[gridder])

        expected = [
            call.execute('OP.test',
                         {
                             'variable': [],
                             'domain': [
                                 {
                                     'id': 'd0',
                                 },
                             ],
                             'operation': process._operation.flatten(),
                         },
                         method='POST',
                         status=False,
                         store=False)
        ]

        self.assertEqual(expected, wps.mock_calls)

    @patch('esgf.wps.WPS')
    def test_named_parameter_as_dict(self, mock_wps):
        """ Test passing NamedParameter as kwarg """
        wps = mock_wps.return_value

        process = Process.from_identifier(wps, 'OP.test')

        process.execute(axes='longitude')

        expected = call.execute('OP.test',
                                {
                                    'variable': [],
                                    'domain': [],
                                    'operation': [
                                        {
                                            'input': [],
                                            'axes': 'longitude',
                                            'name': 'OP.test',
                                            'result': process._operation.name,
                                        }
                                    ],
                                },
                                method='POST',
                                status=False,
                                store=False)

        self.assertEqual(expected, wps.mock_calls[0])

        process.execute(axes='longitude|latitude')

        expected = call.execute('OP.test',
                                {
                                    'variable': [],
                                    'domain': [],
                                    'operation': [
                                        {
                                            'input': [],
                                            'axes': 'longitude|latitude',
                                            'name': 'OP.test',
                                            'result': process._operation.name,
                                        }
                                    ],
                                },
                                method='POST',
                                status=False,
                                store=False)

        self.assertEqual(expected, wps.mock_calls[1])

    @patch('esgf.wps.WPS')
    def test_simple_execute(self, mock_wps):
        """ Test simple execute. """
        wps = mock_wps.return_value

        process = Process.from_identifier(wps, 'OP.test')

        process.execute()

        expected = [
            call.execute('OP.test',
                         {
                             'variable': [],
                             'domain': [],
                             'operation': process._operation.flatten(),
                         },
                         method='POST',
                         status=False,
                         store=False)
        ]

        self.assertEqual(expected, wps.mock_calls)

    def test_str(self):
        """ Tests __str__. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'OP.test')

        with MockPrint() as ctx:
            print process

        self.assertEqual(ctx.value, 'OP.test\n')

    def test_repr(self):
        """ Tests __repr__. """
        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'OP.test')

        with MockPrint() as ctx:
            print '%r' % (process,)

        self.assertIsNotNone(re.match(r'Process\(wps=.*, operation=.*\)',
                                      ctx.value))
