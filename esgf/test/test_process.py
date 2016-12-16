"""
Process Unittest.
"""
from unittest import TestCase

import mock

import esgf

def patch_property(obj, prop_name, value):
    mock_prop = mock.PropertyMock(return_value = value)

    setattr(type(obj), prop_name, mock_prop)

class TestProcess(TestCase):
    """ Process Test Case. """

    def test_execute(self):
        """ Process execution. """
        wps = mock.Mock()

        proc = esgf.Process.from_identifier(wps, 'cdat.averager', 'cdat_avg')

        tas = esgf.Variable('file:///tas.nc', 'tas', name='tas')
        nh = esgf.Domain(dimensions=[
            esgf.Dimension('latitude', 0, 90),
        ], name='NorthHemi')
        axes = esgf.NamedParameter('axes', 'latitude')

        proc.execute(inputs=[tas],
                     domain=nh,
                     parameters=[axes],
                     store=True,
                     status=True,
                     method='GET',
                     bins='month|day')


        wps.execute.assert_called_once()

        expected = mock.call('cdat.averager',
                             {
                                 'variable': [{
                                     'uri': 'file:///tas.nc',
                                     'id': 'tas|tas',
                                 }],
                                 'domain': [{
                                     'latitude': {
                                         'start': 0,
                                         'step': 1,
                                         'end': 90,
                                         'crs': 'values',
                                     },
                                     'id': 'NorthHemi',
                                 }],
                                 'operation': [{
                                     'input': ['tas'],
                                     'bins': 'month|day',
                                     'domain': 'NorthHemi',
                                     'axes': 'latitude',
                                     'name': 'cdat.averager',
                                     'result': 'cdat_avg',
                                 }]
                             },
                             method='GET', 
                             status=True,
                             store=True)

        self.assertEqual(wps.execute.mock_calls[-1], expected)

    def test_bool(self):
        """ Object truthfullness """
        wps = mock.Mock()

        proc = esgf.Process.from_identifier(wps, 'cdat.averager')

        proc._result = mock.Mock()

        patch_property(proc._result, 'status', 'ProcessFailure')        

        self.assertTrue(proc)

        patch_property(proc._result, 'status', 'ProcessSucceeded')        

        self.assertFalse(proc)

    def test_check_status(self):
        """ Check status """
        wps = mock.Mock()

        proc = esgf.Process.from_identifier(wps, 'cdat.averager')

        proc._result = mock.Mock()

        patch_property(proc._result, 'status_location', None)

        with self.assertRaises(esgf.WPSServerError):
            proc.check_status()

        patch_property(proc._result, 'status_location', 'http://test/status')

        proc.check_status()

        proc._result.check_status.assert_called_once()

    def test_output(self):
        """ Process output. """
        wps = mock.Mock()

        proc = esgf.Process.from_identifier(wps, 'cdat.averager')

        proc._result = mock.Mock()

        patch_property(proc._result, 'status', 'ProcessFailure')

        with self.assertRaises(esgf.WPSServerError):
            output = proc.output

        patch_property(proc._result, 'status', 'ProcessSucceeded')

        var_txt = '{"uri":"file:///test.nc","id":"tas|v0"}'

        patch_property(proc._result, 'output', var_txt)

        output = proc.output

        self.assertIsInstance(output, esgf.Variable)
