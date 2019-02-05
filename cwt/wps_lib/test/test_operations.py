#! /usr/bin/env python

import unittest

import os
from lxml import etree

from cwt.wps_lib import metadata as md
from cwt.wps_lib import namespace as ns
from cwt.wps_lib import operations as ops
from cwt.wps_lib import xml
from cwt.wps_lib.test import metadata

def read_file(filename):
    d = os.path.dirname(__file__)

    filename = os.path.join(d, '..', filename)

    with open(filename, 'r') as infile:
        return infile.read()

class ExecuteResponseTest(unittest.TestCase):

    def test_parse(self):
        data = read_file('./test/data/62_wpsExecute_response.xml')

        c = ops.ExecuteResponse.from_xml(data)

        self.assertEqual(c.status_location,
                'http://foo.bar/execute_response_url.xml')
        self.assertIsInstance(c.process, md.Process)
        self.assertIsInstance(c.status, md.ProcessSucceeded)
        self.assertIsInstance(c.data_inputs, list)
        self.assertEqual(len(c.data_inputs), 2)
        self.assertIsInstance(c.output_definitions, list)
        self.assertEqual(len(c.output_definitions), 1)
        self.assertIsInstance(c.output_definitions[0], md.OutputDefinitions)
        self.assertIsInstance(c.output, list)
        self.assertEqual(len(c.output), 1)
        self.assertIsInstance(c.output[0], md.Output)
        self.assertIsInstance(c.output[0].reference, md.Reference)

class ExecuteRequestTest(unittest.TestCase):

    def test_parse_complex_value(self):
        data = read_file('./test/data/53_wpsExecute_request_ComplexValue.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Reclassification')
        self.assertIsInstance(c.data_inputs, list)
        self.assertEqual(len(c.data_inputs), 2)

        inp = c.data_inputs[0]

        self.assertIsInstance(inp, md.Input)
        self.assertIsInstance(inp.data, md.ComplexData)
        self.assertIsInstance(inp.data.value, str)
        self.assertIsInstance(c.response_form, md.ResponseDocument)

    def test_parse_response_document2(self):
        data = read_file('./test/data/52_wpsExecute_request_ResponseDocument.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.data_inputs, list)
        self.assertEqual(len(c.data_inputs), 2)
        self.assertIsInstance(c.data_inputs[0], md.Input)
        self.assertIsInstance(c.response_form, md.ResponseDocument)

    def test_parse_response_document(self):
        data = read_file('./test/data/51_wpsExecute_request_ResponseDocument.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.data_inputs, list)
        self.assertEqual(len(c.data_inputs), 2)
        self.assertIsInstance(c.data_inputs[0], md.Input)
        self.assertIsInstance(c.response_form, md.ResponseDocument)
        self.assertIsInstance(c.response_form.output, list)        
        self.assertEqual(len(c.response_form.output), 1)
        self.assertEqual(c.response_form.output[0].identifier, 'BufferedPolygon')

    def test_parse_raw_data_output(self):
        data = read_file('./test/data/50_wpsExecute_request_RawDataOutput.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.data_inputs, list)
        self.assertEqual(len(c.data_inputs), 2)
        self.assertIsInstance(c.data_inputs[0], md.Input)
        self.assertIsInstance(c.response_form, md.RawDataOutput)
        self.assertEqual(c.response_form.identifier, 'BufferedPolygon')

class DescribeProcessResponseTest(unittest.TestCase):

    def test_parse(self):
        data = read_file('./test/data/40_wpsDescribeProcess_response.xml')

        c = ops.DescribeProcessResponse.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertIsInstance(c.process_description, list)
        self.assertEqual(len(c.process_description), 1)
        self.assertIsInstance(c.process_description[0], md.ProcessDescription)

class DescribeProcessRequestTest(unittest.TestCase):

    def test_parse(self):
        data = read_file('./test/data/30_wpsDescribeProcess_request.xml')

        c = ops.DescribeProcessRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.language, 'en-CA')
        self.assertIsInstance(c.identifier, list)
        self.assertEqual(len(c.identifier), 2)
        self.assertIn('intersection', c.identifier)
        self.assertIn('union', c.identifier)

class GetCapabilitiesResponseTest(unittest.TestCase):
    
    def test_parse(self):
        data = read_file('./test/data/20_wpsGetCapabilities_response.xml')

        c = ops.GetCapabilitiesResponse.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.update_sequence, '1')
        self.assertIsInstance(c.service_identification, md.ServiceIdentification)
        self.assertIsInstance(c.service_provider, md.ServiceProvider)
        self.assertIsInstance(c.operations_metadata, list)
        self.assertEqual(len(c.operations_metadata), 3)
        self.assertIsInstance(c.process_offerings, list)
        self.assertEqual(len(c.process_offerings), 1)
        self.assertIsInstance(c.languages, md.Languages)
        #self.assertIsNotNone(c.wsdl)

class GetCapabilitiesRequestTest(unittest.TestCase):
    
    def test_parse(self):
        data = read_file('./test/data/10_wpsGetCapabilities_request.xml')

        c = ops.GetCapabilitiesRequest.from_xml(data)

        self.assertEqual(c.language, 'en-CA')
        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')

if __name__ == '__main__':
    unittest.main(verbosity=2)
