"""
pyxb wps bindings unit tests
"""

import unittest

import pyxb
import mock

from cwt.wps import wps
from cwt.wps import ows

class TestOWS(unittest.TestCase):
    def test_operation(self):
        operation = ows.operation('GetCapabilities', 'http://test.com/get', 'http://test.com/post')

        self.assertTrue(operation.validateBinding())

    def test_operations_metadata(self):
        get_capabilities = ows.operation('GetCapabilities', 'http://test.com/get', 'http://test.com/post')

        describe_process = ows.operation('DescribeProcess', 'http://test.com/get', 'http://test.com/post')

        metadata = ows.operations_metadata([get_capabilities, describe_process])

        self.assertTrue(metadata.validateBinding())

    def test_service_contact(self):
        contact = ows.service_contact()

        self.assertTrue(contact.validateBinding())

    def test_service_provider(self):
        contact = ows.service_contact()

        service = ows.service_provider('name', contact)

        self.assertTrue(service.validateBinding())

    def test_service_identification(self):
        service = ows.service_identification('title', 'abstract')

        self.assertTrue(service.validateBinding())

class TestWPS(unittest.TestCase):
    def test_status_failed(self):
        status = wps.status_failed('failed', 'code', '1.0.0', 'locator')

        self.assertTrue(status.validateBinding())

    def test_status_succeeded(self):
        status = wps.status_succeeded('succeeded')

        self.assertTrue(status.validateBinding())

    def test_status_paused(self):
        status = wps.status_paused('paused', 10)

        self.assertTrue(status.validateBinding())

    def test_status_started(self):
        status = wps.status_started('start', 10)

        self.assertTrue(status.validateBinding())

    def test_status_accepted(self):
        status = wps.status_accepted('accepted')

        self.assertTrue(status.validateBinding())

    def test_output_data(self):
        data = wps.output_data('CDAT.subset', 'CDAT.subset', 'data')

        self.assertTrue(data.validateBinding())

    def test_execute_response(self):
        status = wps.status_accepted('Accepted')

        process = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        data = wps.output_data('CDAT.subset', 'CDAT.subset', 'data')

        response = wps.execute_response(process, status, '1.0.0', 'en-US', 'http://test.com/', 'http://test.com/status', [data])

        self.assertTrue(response.validateBinding())

    def test_data_input(self):
        data = wps.data_input('variables', 'Variables', 'test data')

        self.assertTrue(data.validateBinding())

    def test_execute(self):
        variables = wps.data_input('variables', 'Variables', 'test data')

        execute = wps.execute('CDAT.subset', '1.0.0', [variables])

        self.assertTrue(execute.validateBinding())

    def test_process_output_description(self):
        output = wps.process_output_description('output', 'output', 'application/json')

        self.assertTrue(output.validateBinding())

    def test_data_input_description(self):
        data = wps.data_input_description('variables', 'Variables', 'application/json', 1, 1)

        self.assertTrue(data.validateBinding())

    def test_process_description(self):
        data = wps.data_input_description('variables', 'Variables', 'application/json', 1, 1)

        output = wps.process_output_description('output', 'output', 'application/json')

        description = wps.process_description('CDAT.subset', 'CDAT.subset', '1.0.0', [data], [output])

        self.assertTrue(description.validateBinding())

    def test_process_descriptions(self):
        data = wps.data_input_description('variables', 'Variables', 'application/json', 1, 1)

        output = wps.process_output_description('output', 'output', 'application/json')

        description = wps.process_description('CDAT.subset', 'CDAT.subset', '1.0.0', [data], [output])

        descriptions = wps.process_descriptions('en-US', '1.0.0', description)

        self.assertTrue(descriptions.validateBinding())

    def test_describe_process(self):
        describe = wps.describe_process('CDAT.subset', '1.0.0')

        self.assertTrue(describe.validateBinding())

    def test_process(self):
        process = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        self.assertTrue(process.validateBinding())

    def test_process_offerings(self):
        subset = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        offerings = wps.process_offerings([subset])

        self.assertTrue(offerings.validateBinding())

    def test_capabilities(self):
        identification = ows.service_identification('title', 'abstract')

        contact = ows.service_contact()

        provider = ows.service_provider('name', contact)

        get_capabilities = ows.operation('GetCapabilities', 'http://test.com/get', 'http://test.com/post')

        describe_process = ows.operation('DescribeProcess', 'http://test.com/get', 'http://test.com/post')

        metadata = ows.operations_metadata([get_capabilities, describe_process])

        subset = wps.process('CDAT.subset', 'CDAT.subset', '1.0.0')

        offerings = wps.process_offerings([subset])

        capabilities = wps.capabilities(identification, provider, metadata, offerings, 'en-US', '1.0.0')

        self.assertTrue(capabilities.validateBinding())

    def test_get_capabilities(self):
        capabilities = wps.get_capabilities()

        self.assertTrue(capabilities.validateBinding())

if __name__ == '__main__':
    unittest.main()
