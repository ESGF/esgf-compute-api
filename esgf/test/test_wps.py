"""
WPS unittest.
"""

from unittest import TestCase

from mock import patch

from esgf import WPS

from . import test_data

class TestWPS(TestCase):
    """ Test Case for WPS class.
    """

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

        self.assertFalse(wps.__str__() == '{}')
