#! /usr/bin/env python

import unittest

from lxml import etree

from esgf.wps_lib import metadata as md
from esgf.wps_lib import namespace as ns
from esgf.wps_lib import operations as ops
from esgf.wps_lib import xml
from esgf.wps_lib.test import metadata

def read_file(filename):
    with open(filename, 'r') as infile:
        return infile.read()

class ExecuteResponseTest(unittest.TestCase):

    def test_parse(self):
        data = read_file('./test/data/62_wpsExecute_response.xml')

        c = ops.ExecuteResponse.from_xml(data)

        self.assertEqual(c.status_location,
                'http://foo.bar/execute_response_url.xml')
        self.assertIsInstance(c.process, md.Process)
        self.assertIsInstance(c.status, str)
        self.assertIsInstance(c.input, list)
        self.assertEqual(len(c.input), 2)
        self.assertIsInstance(c.output_definitions, list)
        self.assertEqual(len(c.output_definitions), 1)
        self.assertIsInstance(c.output_definitions[0], md.DocumentOutputDefinition)
        self.assertIsInstance(c.process_outputs, list)
        self.assertEqual(len(c.process_outputs), 1)
        self.assertIsInstance(c.process_outputs[0], md.Output)
        self.assertIsInstance(c.process_outputs[0].reference, md.OutputReference)

class ExecuteRequestTest(unittest.TestCase):

    def test_parse_complex_value(self):
        data = read_file('./test/data/53_wpsExecute_request_ComplexValue.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Reclassification')
        self.assertIsInstance(c.input, list)
        self.assertEqual(len(c.input), 2)
        self.assertIsInstance(c.input[0], md.Input)
        self.assertIsInstance(c.input[0].data, md.ComplexData)
        self.assertIsInstance(c.input[0].data.value, list)
        self.assertIsInstance(c.response_form, md.ResponseDocument)

    def test_parse_response_document2(self):
        data = read_file('./test/data/52_wpsExecute_request_ResponseDocument.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.input, list)
        self.assertEqual(len(c.input), 2)
        self.assertIsInstance(c.input[0], md.Input)
        self.assertIsInstance(c.response_form, md.ResponseDocument)

    def test_parse_response_document(self):
        data = read_file('./test/data/51_wpsExecute_request_ResponseDocument.xml')

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.input, list)
        self.assertEqual(len(c.input), 2)
        self.assertIsInstance(c.input[0], md.Input)
        self.assertIsInstance(c.response_form, md.ResponseDocument)
        self.assertIsInstance(c.response_form.output, list)        
        self.assertEqual(len(c.response_form.output), 1)
        self.assertEqual(c.response_form.output[0].identifier, 'BufferedPolygon')

    def test_parse_raw_data_output(self):
        with open('./test/data/50_wpsExecute_request_RawDataOutput.xml') as infile:
            data = infile.read()

        c = ops.ExecuteRequest.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.identifier, 'Buffer')
        self.assertIsInstance(c.input, list)
        self.assertEqual(len(c.input), 2)
        self.assertIsInstance(c.input[0], md.Input)
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
        self.assertIsInstance(c.operation, list)
        self.assertEqual(len(c.operation), 3)
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
