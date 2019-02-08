"""
Process Unittest.
"""

import unittest
import mock

import cwt

class TestProcess(unittest.TestCase):
    """ Process Test Case. """

    def setUp(self):
        self.process_dict = {
            'name': 'CDAT.subset',
            'input': [{
                'uri': 'file:///test.nc',
                'id': 'v0|tas',
            }],
            'domain': {
                'time': {
                    'start': 0,
                    'end': 365,
                    'step': 1,
                    'crs': 'VALUES',
                },
                'id': 'd0',
            },
            'result': 'subset',
            'weightoption': 'random',
        }

        self.process = cwt.Process.from_dict(self.process_dict)

        self.process.context = mock.MagicMock()

        type(self.process.context).percentCompleted = mock.PropertyMock(return_value=20)

        type(self.process.context).statusMessage = mock.PropertyMock(return_value='Hello')

        self.process2 = cwt.Process.from_dict({
            'name': 'CDAT.aggregate',
            'input': [{
                'uri': 'file:///test.nc',
                'id': 'v0|tas',
            }],
            'domain': {
                'time': {
                    'start': 0,
                    'end': 365,
                    'step': 1,
                    'crs': 'VALUES',
                },
                'id': 'd1',
            },
            'result': 'subset',
        })

    def test_processing_accepted(self):
        type(self.process.context).status = mock.PropertyMock(return_value='ProcessAccepted')

        self.assertTrue(self.process.processing)

    def test_processing_started(self):
        type(self.process.context).status = mock.PropertyMock(return_value='ProcessStarted')

        self.assertTrue(self.process.processing)

    def test_processing(self):
        self.assertFalse(self.process.processing)

    def test_output(self):
        type(self.process.context).status = mock.PropertyMock(return_value='ProcessSucceeded')

        data = '{"id": "tas|v0", "uri": "file:///test.nc"}'

        self.process.context.processOutputs.__getitem__.return_value.data.__getitem__.return_value = data

        output = self.process.output

        self.assertIsInstance(output, cwt.Variable)
        self.assertEqual(output.uri, 'file:///test.nc')
        self.assertEqual(output.var_name, 'tas')
        self.assertEqual(output.name, 'v0')

    def test_output_not_succeeded(self):
        with self.assertRaises(cwt.CWTError):
            self.process.output

    def test_status(self):
        tests = [
            ('ProcessAccepted', 'ProcessAccepted Hello'),
            ('ProcessStarted', 'ProcessStarted Hello 20'),
            ('ProcessPaused', 'ProcessPaused Hello 20'),
            ('ProcessFailed', 'ProcessFailed Hello'),
            ('ProcessSucceeded', 'ProcessSucceeded Hello'),
            ('Exception', 'Exception '),
        ]

        for status, message in tests:
            type(self.process.context).status = mock.PropertyMock(return_value=status)

            self.assertEqual(self.process.status, message)

    @mock.patch('cwt.process.StatusTracker')
    def test_wait_timeout(self, mock_tracker):
        processing = [True, True, False]

        type(self.process).processing = mock.PropertyMock(side_effect=processing)

        type(mock_tracker.return_value).elapsed = mock.PropertyMock(return_value=20)

        with self.assertRaises(cwt.WPSTimeoutError):
            self.process.wait(timeout=10)

    @mock.patch('cwt.process.StatusTracker')
    def test_wait(self, mock_tracker):
        processing = [True, True, False]

        type(self.process).processing = mock.PropertyMock(side_effect=processing)

        self.process.wait(stale_threshold=10)

        mock_tracker.called_with(10)

        self.assertEqual(mock_tracker.return_value.update.call_count, 4)

    def test_get_parameter_missing_required(self):
        with self.assertRaises(cwt.CWTError):
            self.process.get_parameter('axes', required=True)

    def test_get_parameter(self):
        param = self.process.get_parameter('weightoption')

        self.assertIsNotNone(param)
        self.assertEqual(param.values, ('random',))

    def test_add_parameters_kwargs_list(self):
        self.process.add_parameters(axes=['lat', 'lon'])

        self.assertIn('axes', self.process.parameters)

        self.assertEqual(self.process.parameters['axes'].values, ('lat', 'lon'))

    def test_add_parameters_kwargs(self):
        self.process.add_parameters(axes='lat')

        self.assertIn('axes', self.process.parameters)

        self.assertEqual(self.process.parameters['axes'].values, ('lat',))

    def test_add_parameters_wrong_type_arg(self):
        with self.assertRaises(cwt.CWTError):
            self.process.add_parameters('axis')

    def test_add_parameters(self):
        param = cwt.NamedParameter('axes', 'time')

        self.process.add_parameters(param)

        self.assertIn('axes', self.process.parameters)

        self.assertEqual(self.process.parameters['axes'], param)

    def test_collect_input_processes(self):
        self.process.add_inputs(self.process2)

        processes, inputs = self.process.collect_input_processes()

        self.assertEqual(processes, [self.process2])

        self.assertEqual(inputs, [])

    def test_to_dict(self):
        data = self.process.to_dict()

        self.assertDictContainsSubset(data, self.process_dict)
