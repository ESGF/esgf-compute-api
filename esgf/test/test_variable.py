""" Variable Unittest. """

import json

from unittest import TestCase

from mock import patch, Mock

from esgf import Domain
from esgf import Variable
from esgf import WPSAPIError
from esgf import WPSClientError

MOCK_DATA = ['hello', ' ', 'you', ' ', 'person']

def mock_gen():
    """ Mock generator for requests.iter_content. """
    for item in MOCK_DATA:
        yield item

class TestVariable(TestCase):
    """ Variable Test Case. """

    def test_from_dict(self):
        """ Test creating variable from dict representation. """
        single_domain = {'uri': '/test.nc', 'id': 'tas|v0', 'domain': 'd0'}
        multiple_domain = {'uri': '/test.nc', 'id': 'tas|v0',
                           'domain': ['d0', 'd1']}
        missing_uri = {'id': 'tas|v0', 'domain': 'd0'}
        missing_id = {'uri': '/test.nc', 'domain': 'd0'}
        missing_name = {'uri': '/test.nc', 'domain': 'd0', 'id': 'tas'}
        missing_domain = {'uri': '/test.nc', 'id': 'tas|v0'}

        var = Variable.from_dict(single_domain)

        self.assertEqual(var.uri, '/test.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertEqual(var.name, 'v0')
        self.assertEqual(var.domains, 'd0')

        var = Variable.from_dict(multiple_domain)

        self.assertEqual(var.uri, '/test.nc')
        self.assertEqual(var.var_name, 'tas')
        self.assertEqual(var.name, 'v0')
        self.assertListEqual(var.domains, ['d0', 'd1'])

        with self.assertRaises(WPSAPIError) as ctx:
            var = Variable.from_dict(missing_uri)

        self.assertEqual(ctx.exception.message,
                         'Variable must provide a uri.')

        with self.assertRaises(WPSAPIError) as ctx:
            var = Variable.from_dict(missing_id)

        self.assertEqual(ctx.exception.message,
                         'Variable must provide an id.')

        with self.assertRaises(WPSAPIError) as ctx:
            var = Variable.from_dict(missing_name)

        self.assertEqual(ctx.exception.message,
                         'Variable id must contain a variable name and id.')

        with self.assertRaises(WPSAPIError) as ctx:
            var = Variable.from_dict(missing_domain)

        self.assertEqual(ctx.exception.message,
                         'Variable must provide a domain.')

    @patch('esgf.variable.requests')
    def test_download_as_str(self, mock_requests):
        """ Download output as string. """

        # Mock requests.reponse.iter_content method
        get_mock = Mock()
        get_mock.iter_content.return_value = mock_gen()

        # Mock requests.get returned response
        mock_requests.get.return_value = get_mock

        variable = Variable('file://test.nc', 'ta')

        self.assertEqual(variable.download_as_str(), 'hello you person')

    @patch('esgf.variable.requests')
    @patch('esgf.variable.open')
    def test_download(self, mock_open, mock_requests):
        """ Download output to file. """
        variable = Variable('file://test.nc', 'ta')

        with self.assertRaises(WPSClientError):
            variable.download('./test.json')

        # Mock requests.reponse.iter_content method
        get_mock = Mock()
        get_mock.iter_content.return_value = mock_gen()

        # Mock requests.get returned response
        mock_requests.get.return_value = get_mock

        # pylint: disable=too-few-public-methods
        class MockFile(object):
            """ Mock class for return value of open(). """
            def __init__(self):
                """ MockFile init. """
                self.data = []

            def __enter__(self):
                """ Enter """
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                """ Exit """
                pass

            def write(self, data):
                """ Mock file.write method. """
                self.data.append(data)

        mock_open.return_value = MockFile()

        variable = Variable('http://localhost:8000/wps/media/test.nc', 'ta')

        variable.download('./test.json')

        self.assertItemsEqual(mock_open.return_value.data, MOCK_DATA)

    def test_from_json(self):
        """ Creation from json. """
        result_obj = {
            'uri': 'file://test.nc',
            'id': 'ta',
            'domain': 'd0',
            'mime-type': 'application/netcdf'
        }

        result_json = json.dumps(result_obj)

        variable = Variable.from_json(result_json)

        self.assertEqual(variable.uri, 'file://test.nc')
        self.assertEqual(variable.var_name, 'ta')
        self.assertIsNotNone(variable.domains)
        self.assertEqual(variable.mime_type, 'application/netcdf')

    def test_optional_init(self):
        """ Tests optional init. """
        var = Variable('file:///test.nc', 'clt')

        self.assertEqual(var.uri, 'file:///test.nc')
        self.assertEqual(var.var_name, 'clt')
        self.assertIsNone(var.domains)
        self.assertIsNotNone(var.name)
        self.assertIsNone(var.mime_type)

    def test_name(self):
        """ Providing name argument. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
        }

        var = Variable('file://test.nc', 'ta', name='v0')

        self.assertEqual(var.parameterize(), expected)

    def test_single_domain(self):
        """ Passing single domain. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
            'domain': 'glbl',
        }

        domain = Domain(name='glbl')

        variable = Variable('file://test.nc', 'ta', name='v0', domains=domain)

        self.assertEqual(variable.parameterize(), expected)

    def test_multiple_domains(self):
        """ Passing multiple domains. """
        expected = {
            'uri': 'file://test.nc',
            'id': 'ta|v0',
            'domain': 'glbl|glbl2',
        }

        domain0 = Domain(name='glbl')
        domain1 = Domain(name='glbl2')

        variable = Variable(
            'file://test.nc',
            'ta',
            name='v0',
            domains=[
                domain0,
                domain1
            ]
        )

        self.assertEqual(variable.parameterize(), expected)
