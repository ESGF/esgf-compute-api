"""
WPS unittest.
"""

import os
import json

from unittest import TestCase

from mock import Mock
from mock import patch
from mock import PropertyMock
from mock import call

from esgf import Operation
from esgf import Variable
from esgf import WPS
from esgf import WPSServerError
from esgf import WPSClientError

from esgf.test import test_data

class TestWPS(TestCase):
    """ Test Case for WPS class. """

    @patch.object(WPS, 'execute')
    def test_execute_op(self, execute):
        wps = WPS('http://localhost:8000/wps')

        tas = Variable('file:///test.nc', 'tas')

        test = Operation('OP.test', inputs=[tas])

        wps.execute_op(test)

        self.assertEqual(execute.mock_calls[0],
                         call(
                             'OP.test',
                             {
                                 'variable': [tas.parameterize()],
                                 'domain': [],
                                 'operation': [test.parameterize()]
                             },
                             method='POST',
                             status=False,
                             store=False
                         ))

        test2 = Operation('OP.test2', inputs=[test])

        wps.execute_op(test2)

        self.assertEqual(execute.mock_calls[1],
                         call(
                             'OP.test2',
                             {
                                 'variable': [tas.parameterize()],
                                 'domain': [],
                                 'operation': [test.parameterize(), test2.parameterize()],
                             },
                             method='POST',
                             status=False,
                             store=False
                         ))

    @patch('esgf.wps.requests.Session')
    def test_iter_processes(self, mock_session):
        """ Tests iterating processes. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        identifiers = []
        expected = [
            'averager.mv',
            'averager.ophidia',
            'test.echo',
            'test.sleep'
        ]

        for process in wps:
            identifiers.append(process._operation.identifier)

        self.assertListEqual(expected, identifiers)

    def test_logging(self):
        """ Tests logging. """
        wps = WPS('http://localhost:8000/wps', log=True, log_file='test.log')

        from esgf import wps as wps_ns

        self.assertTrue(os.path.exists(os.path.join(os.path.curdir, 'test.log')))
        self.assertEqual(len(wps_ns.logger.handlers), 2)

    @patch('esgf.wps.requests.Session')
    def test_authorization(self, mock_session):
        """ Tests authorization. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        self.assertIsNone(wps._service._username)
        self.assertIsNone(wps._service._password)

        wps = WPS('http://localhost:8000/wps', username='user', password='test')

        self.assertEqual(wps._service._username, 'user')
        self.assertEqual(wps._service._password, 'test')

        wps.identification

        self.assertEqual(
            wps._service._session.get.mock_calls[0][2]['auth'],
            ('user', 'test'))

    @patch('esgf.wps.requests.Session')
    def test_language(self, mock_session):
        """ Tests language. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        self.assertEqual(wps._service._language, None)

        wps = WPS('http://localhost:8000/wps', language='en-US')

        self.assertEqual(wps._service._language, 'en-US')

        wps.identification

        self.assertEqual(
            wps._service._session.get.mock_calls[0][2]['params']['language'],
            'en-US')

    @patch('esgf.wps.requests.Session')
    def test_accept_versions(self, mock_session):
        """ Tests accept versions. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        self.assertEquals(wps._service._accept_versions, None)

        wps = WPS('http://localhost:8000/wps', accept_versions='1.0.0')

        self.assertEquals(wps._service._accept_versions, '1.0.0')

        wps.identification

        self.assertEqual(
            wps._service._session.get.mock_calls[0][2]['params']['acceptversions'],
            '1.0.0')

    def test_execute_unsupported(self):
        """ Tests running execute as an unknown request. """
        wps = WPS('http://localhost:8000/wps')

        with self.assertRaises(WPSClientError) as ctx:
            wps.execute('averager.mv', { }, False, False, 'UPDATE')

        self.assertEqual(ctx.exception.message,
                         'HTTP method UPDATE is not supported')

    @patch('esgf.wps.requests.Session')
    def test_execute_get(self, mock_session):
        """ Tests running execute as a GET request. """
        get_resp = self.create_get_response(mock_session,
                                            test_data.MOCK_EXECUTE_RESPONSE)    

        wps = WPS('http://localhost:8000/wps')

        wps.execute('averager.mv', { }, False, False, 'GET')

        self.assertEqual(get_resp.mock_calls[0][2]['params']['status'], False)
        self.assertEqual(get_resp.mock_calls[0][2]['params']['store'], False)

        wps.execute('averager.mv', { }, True, True, 'GET')

        self.assertEqual(get_resp.mock_calls[1][2]['params']['status'], True)
        self.assertEqual(get_resp.mock_calls[1][2]['params']['store'], True)

        variable = Variable('file:///test.nc', 'tas')

        wps.execute('averager.mv', {
            'variable': [json.dumps(variable.parameterize())], 
        }, False, False, 'GET')

        self.assertTrue('datainputs' in get_resp.mock_calls[2][2]['params'])

    def create_get_response(self, mock_session, text_data):
        inst_session = mock_session.return_value
        inst_session.get = Mock(
            return_value = Mock(
                text = text_data,
                url = 'http://localhost:8000/wps'
            )
        )

        return inst_session.get

    @patch('esgf.wps.requests.Session')
    def test_get_process(self, mock_session):
        """ Tests retrieving a process. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        process = wps.get_process('averager.mv')

        self.assertIsNotNone(process)
        self.assertIsNotNone(process._operation)
        self.assertEqual(process._operation.identifier, 'averager.mv')

        with self.assertRaises(WPSClientError) as ctx:
            process = wps.get_process('no.exist')

        self.assertEqual(ctx.exception.message,
                         'No process named \'no.exist\' was found.')

    @patch('esgf.wps.requests.Session')
    def test_provider(self, mock_session):
        """ Tests provider processing. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        prov = wps.provider

        self.assertEqual(prov['url'], 'https://esgf.llnl.gov')

    @patch('esgf.wps.requests.Session')
    def test_identification(self, mock_session):
        """ Tests identification processing. """
        self.create_get_response(mock_session, test_data.MOCK_GETCAPABILITIES)

        wps = WPS('http://localhost:8000/wps')

        id = wps.identification

        self.assertEqual(id['service'], 'WPS')

    def test_no_service(self):
        """ Tests error handling with a non existent server. """
        cap_error = 'GetCapabilities Request failed, check logs.'

        wps = WPS('http://localhost:9999/wps')

        with self.assertRaises(WPSServerError) as ctx:
            wps.identification

        self.assertEqual(ctx.exception.message, cap_error)

        wps = WPS('http://localhost:9999/wps')

        with self.assertRaises(WPSServerError) as ctx:
            wps.provider

        self.assertEqual(ctx.exception.message, cap_error)

        wps = WPS('http://localhost:9999/wps')

        with self.assertRaises(WPSServerError) as ctx:
            wps.get_process('averager.mv')

        self.assertEqual(ctx.exception.message, cap_error)

        wps = WPS('http://localhost:9999/wps')

        with self.assertRaises(WPSServerError) as ctx:
            wps.execute('identifier.mv', { }, False, False, 'GET')

        self.assertEqual(ctx.exception.message,
                         'Execute Request failed, check logs.')
