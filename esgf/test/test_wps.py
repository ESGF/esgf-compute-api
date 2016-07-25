from unittest import TestCase

from mock import patch

from esgf import WPS

import test_data

class TestWPS(TestCase):
    @patch('esgf.wps.WebProcessingService')
    def test_wps(self, mock_service):
        wps = WPS('http://localhost:8000/wps', 'username', 'password')

        mock_service.assert_called_once_with(
            'http://localhost:8000/wps',
            username='username',
            password='password',
            skip_caps=True,
            verbose=False)

    @patch('esgf.wps.WebProcessingService.getcapabilities')
    def test_init(self, mock_getcapabilities):
        wps = WPS('http://localhost:8000/wps')

        wps.init()

        mock_getcapabilities.assert_called_once()

    @patch('esgf.wps.WebProcessingService')
    def test_identification(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        ident = wps.identification

        self.assertTrue(ident == test_data._IDENTIFICATION)

    @patch('esgf.wps.WebProcessingService')
    def test_provider(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        prov = wps.provider

        test_data._PROVIDER['contact'] = test_data._CONTACT

        self.assertTrue(prov == test_data._PROVIDER)

    @patch('esgf.wps.WebProcessingService')
    def test_str(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.identification = test_data.generate_identification()
        mock_instance.provider = test_data.generate_provider()

        wps = WPS('http://localhost:8000/wps')

        self.assertFalse(wps.__str__() == '{}')
