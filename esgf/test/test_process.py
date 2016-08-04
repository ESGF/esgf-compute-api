"""
Process Unittest.
"""

from unittest import TestCase

from mock import patch

from esgf import WPS
from esgf import Process
from esgf import Variable
from esgf import Dimension
from esgf import Domain

class TestProcess(TestCase):
    """ Process Test Case. """

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
