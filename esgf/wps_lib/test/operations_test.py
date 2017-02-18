#! /usr/bin/env python

import unittest

from lxml import etree

from esgf.wps_lib import metadata as md
from esgf.wps_lib import namespace as ns
from esgf.wps_lib import operations as ops
from esgf.wps_lib import xml
from esgf.wps_lib.test import metadata

class ExecuteResponseTest(unittest.TestCase):

    def test_parse(self):
        with open('./test/data/62_wpsExecute_response.xml') as infile:
            data = infile.read()

        e = ops.ExecuteResponse.from_xml(data)

        self.assertIsInstance(e.process, md.Process)
        self.assertIsInstance(e.data_inputs, list)
        #self.assertEqual(len(e.data_inputs), 2)
        #self.assertIsInstance(e.data_inputs[0], md.Input)
        self.assertIsInstance(e.output_definitions, list)
        self.assertEqual(len(e.output_definitions), 1)
        self.assertIsInstance(e.output_definitions[0], md.DocumentOutputDefinition)
        self.assertIsInstance(e.process_outputs, list)
        self.assertEqual(len(e.process_outputs), 1)
        self.assertIsInstance(e.process_outputs[0], md.Output)

    def test_generate(self):
        attrs = {
                'lang': 'en-CA',
                'version': '1.0.0',
                'service': 'WPS',
                'service_instance': 'llnl.gov',
                'status': 'Done',
                'process': 1,
                }

        execute = ops.ExecuteResponse()

        self.assertIsNotNone(execute(**attrs))

class ExecuteRequestTest(unittest.TestCase):

    def test_parse_complex(self):
        with open('./test/data/53_wpsExecute_request_ComplexValue.xml') as infile:
            data = infile.read()

        e = ops.ExecuteRequest.from_xml(data)

        self.assertIsInstance(e.input, list)
        self.assertEqual(len(e.input), 2)
        #self.assertEqual(e.input[0].data.href,
        #        'http://orchestra.pisa.intecs.it/geoserver/test/height.tif')

    def test_parse_response_document_2(self):
        with open('./test/data/52_wpsExecute_request_ResponseDocument.xml') as infile:
            data = infile.read()

        e = ops.ExecuteRequest.from_xml(data)

        self.assertTrue(e.response_form.lineage)
        self.assertTrue(e.response_form.status)

    def test_parse_response_document(self):
        with open('./test/data/51_wpsExecute_request_ResponseDocument.xml') as infile:
            data = infile.read()

        e = ops.ExecuteRequest.from_xml(data)

        self.assertIsInstance(e.response_form, md.ResponseDocument)
        self.assertIsInstance(e.response_form.output, list)
        self.assertEqual(len(e.response_form.output), 1)
        
        output = e.response_form.output[0]

        self.assertTrue(output.as_reference)
        self.assertEqual(output.identifier, 'BufferedPolygon')

    def test_parse_raw_data_output(self):
        with open('./test/data/50_wpsExecute_request_RawDataOutput.xml') as infile:
            data = infile.read()

        e = ops.ExecuteRequest.from_xml(data)

        self.assertIsInstance(e.input, list)
        self.assertEqual(len(e.input), 2)
        self.assertIsInstance(e.input[0], md.Input)
        #self.assertIsInstance(e.input[0].data, md.LiteralData)
        #self.assertIsInstance(e.input[1].data, md.Reference)
        self.assertIsInstance(e.response_form, md.RawDataOutput)

    def test_generate(self):
        attrs = {
                'version': '1.0.0',
                'service': 'WPS',
                }

        execute = ops.ExecuteRequest()

        self.assertIsNotNone(execute(**attrs))

class ProcessDescriptionsTest(unittest.TestCase):

    def test_parse(self):
        with open('./test/data/40_wpsDescribeProcess_response.xml') as infile:
            data = infile.read()

        d = ops.DescribeProcessResponse.from_xml(data)

        self.assertIsInstance(d.process_description, list)
        self.assertEqual(len(d.process_description), 1)
        self.assertIsInstance(d.process_description[0], md.ProcessDescription) 

        process = d.process_description[0]

        self.assertEqual(process.identifier, 'Buffer')
        self.assertEqual(len(process.input), 2)
        self.assertEqual(len(process.output), 1)

    def test_generate(self):
        attrs = {
                'lang': 'en-CA',
                'version': '1.0.0',
                'service': 'WPS',
                'process_description': [metadata.describe_sum],
                }

        describe = ops.DescribeProcessResponse()

        self.assertIsNotNone(describe(**attrs))

class DescribeProcessRequestTest(unittest.TestCase):

    def test_parse(self):
        with open('./test/data/30_wpsDescribeProcess_request.xml') as infile:
            data = infile.read()

        d = ops.DescribeProcessRequest.from_xml(data)

        self.assertEqual(d.service, 'WPS')
        self.assertEqual(d.version, '1.0.0')
        self.assertEqual(d.language, 'en-CA')
        self.assertIsInstance(d.identifier, list)
        self.assertIn('intersection', d.identifier)
        self.assertIn('union', d.identifier)
    
    def test_generate(self):
        attrs = {
                'version': '1.0.0',
                'service': 'WPS',
                'identifier': ['intersection', 'union'],
                }

        describe = ops.DescribeProcessRequest()

        self.assertIsNotNone(describe(**attrs))

class GetCapabilitiesResponseTest(unittest.TestCase):

    def test_parse(self):
        with open('./test/data/20_wpsGetCapabilities_response.xml') as infile:
            data = infile.read()

        c = ops.GetCapabilitiesResponse.from_xml(data)

        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')
        self.assertEqual(c.update_sequence, '1')
        self.assertIsInstance(c.service_identification, md.ServiceIdentification)
        self.assertIsInstance(c.service_provider, md.ServiceProvider)
        self.assertIsInstance(c.operations_metadata[0], md.Operation)
        self.assertIsInstance(c.process_offerings[0], md.Process)
        self.assertIsInstance(c.languages, md.Languages)
    
    def test_generate(self):
        attrs = {
                'lang': 'en-CA',
                'version': '1.0.0',
                'service': 'WPS',
                'service_identification': metadata.identification,
                'process_offerings': [metadata.process_avg, metadata.process_sum],
                'languages': metadata.languages,
                'operations_metadata': metadata.operation_execute,
                'service_provider': metadata.provider,
                }

        capabilities = ops.GetCapabilitiesResponse()

        self.assertIsNotNone(capabilities(**attrs))

class GetCapabilitiesRequestTest(unittest.TestCase):

    def test_parse(self):
        with open('./test/data/10_wpsGetCapabilities_request.xml') as infile:
            data = infile.read()

        c = ops.GetCapabilitiesRequest.from_xml(data)

        self.assertEqual(c.language, 'en-CA')
        self.assertEqual(c.service, 'WPS')
        self.assertEqual(c.version, '1.0.0')

    def test_generate(self):
        attrs = {
                'service': 'WPS',
                }

        capabilities = ops.GetCapabilitiesRequest()

        self.assertIsNotNone(capabilities(**attrs))

if __name__ == '__main__':
    import logging
    import sys

    #logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    unittest.main(verbosity=2)
