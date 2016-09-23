"""
WPS unittest.
"""

import re
import json

from unittest import TestCase

from mock import patch
from mock import Mock
from mock import call

from esgf import WPS
from esgf import WPSClientError
from esgf import Process
from esgf import Variable

from . import MockPrint
from . import test_data

class TestWPS(TestCase):
    """ Test Case for WPS class. """

    @patch('esgf.wps.etree')
    @patch('esgf.wps.WPSExecution')
    def test_execute(self, mock_execution, mock_etree):
        """ Test execute method. """
        execution_inst = mock_execution.return_value

        wps = WPS('http://localhost:8000/wps')

        process = Process.from_identifier(wps, 'test.echo')

        v0 = Variable('file:///test.nc', 'tas', name='v0') 

        process.execute(v0)

        execution_inst.buildRequest.assert_called_once()

        self.assertEquals(execution_inst.buildRequest.call_args,
                          call('test.echo',
                               [
                                   ('variable', json.dumps(v0.parameterize())),
                                   ('domain', '[]'),
                                   ('operation', json.dumps(process._operation.parameterize())),
                               ],
                               output='output'))

    @patch('esgf.wps.WebProcessingService')
    def test_get_process(self, mock_service):
        """ Test retrieving process by name. """
        mock_inst = mock_service.return_value

        wps = WPS('http://localhost:8000/wps')

        with self.assertRaises(WPSClientError) as ctx:
            process = wps.get_process('CDS.test')

        self.assertEqual(ctx.exception.message,
                         'No process named \'CDS.test\' was found.')

        mock_inst.processes = [
            Mock(identifier='CDS.test'),
            Mock(identifier='CDS.subset'),
            Mock(identiifer='CDS.mean'),
        ]

        process = wps.get_process('CDS.test')

        self.assertIsNotNone(process)
        self.assertIsInstance(process, Process)

    @patch('esgf.wps.WebProcessingService')
    def test_iter(self, mock_service):
        """ Tests WPS iterator. """
        operations = [
            'CDS.test',
            'CDS.subset',
            'CDS.mean',
        ]

        mock_inst = mock_service.return_value
        mock_inst.processes = []

        for oper in operations:
            mock_inst.processes.append(Mock(identifier=oper))

        wps = WPS('http://localhost:8000/wps')

        output = zip(wps, operations)

        for process in output:
            with MockPrint() as ctx:
                print process[0]

            self.assertEqual(ctx.value.replace('\n', ''), process[1])

    def test_no_service(self):
        """ Tests bad service endpoint. """
        wps = WPS('http://localhost:9999/wps')

        with self.assertRaises(WPSClientError) as ctx:
            print wps.identification

        wps = WPS('http://localhost:9999/wps')
        
        with self.assertRaises(WPSClientError) as ctx:
            print wps.provider

    @patch('esgf.wps.WebProcessingService')
    # pylint: disable=no-self-use
    def test_wps(self, mock_service):
        """ Testing constructor. """

        # pylint: disable=unused-variable
        wps = WPS('http://localhost:8000/wps', 'username', 'password')

        mock_service.assert_called_once_with(
            'http://localhost:8000/wps',
            username='username',
            password='password',
            skip_caps=True,
            verbose=False)

    @patch('esgf.wps.WebProcessingService.getcapabilities')
    # pylint: disable=no-self-use
    def test_init(self, mock_getcapabilities):
        """ Testing init. """

        wps = WPS('http://localhost:8000/wps')

        wps.init()

        mock_getcapabilities.assert_called_once()

    @patch('esgf.wps.WebProcessingService')
    def test_identification(self, mock_service):
        """ Testing identification property. """

        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        ident = wps.identification

        self.assertTrue(ident == test_data.IDENTIFICATION)

    @patch('esgf.wps.WebProcessingService')
    def test_provider(self, mock_service):
        """ Testing provider property. """

        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        prov = wps.provider

        # Reset the contact keys value to contact dict
        test_data.PROVIDER['contact'] = test_data.CONTACT

        self.assertTrue(prov == test_data.PROVIDER)

    @patch('esgf.wps.WebProcessingService')
    def test_str(self, mock_service):
        """ Testing __str__. """

        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        with MockPrint() as ctx:
            print wps

        self.assertNotEqual(ctx.value, {})

    @patch('esgf.wps.WebProcessingService')
    def test_repr(self, mock_service):
        """ Testing __repr__. """

        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        with MockPrint() as ctx:
            print '%r' % wps

        self.assertIsNotNone(re.match(r'WPS\(url=\'http://localhost:8000/' +
                                      r'wps\', service=.*\)', ctx.value))
