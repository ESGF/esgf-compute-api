#! /usr/bin/env python

import re

from esgf.wps_lib import metadata
from esgf.wps_lib import namespace as ns
from esgf.wps_lib import xml

from esgf.wps_lib.test import metadata as md

class ExecuteResponse(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(ExecuteResponse, self).__init__(namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Attribute(required=True)
    def version(self):
        pass

    @xml.Attribute(required=True)
    def lang(self):
        pass

    @xml.Attribute()
    def status_location(self):
        pass

    @xml.Attribute(required=True)
    def service_instance(self):
        pass

    @xml.Element(value_type=metadata.Process)
    def process(self):
        pass

    @metadata.wps_element(value_type=(metadata.ProcessAccepted,
        metadata.ProcessStarted,
        metadata.ProcessPaused,
        metadata.ProcessSucceeded,
        metadata.ProcessFailed))
    def status(self):
        pass

    @xml.Attribute(attach_element='status', required=True)
    def creation_time(self):
        pass

    @metadata.wps_zero_many_element(path='DataInputs',
            nsmap={'DataInputs':ns.WPS},
            value_type=metadata.Input)
    def input(self):
        pass

    @metadata.wps_zero_many_element(value_type=metadata.DocumentOutputDefinition)
    def output_definitions(self):
        pass

    @metadata.wps_zero_many_element(value_type=metadata.Output)
    def process_outputs(self):
        pass

    def __call__(self, **kwargs):
        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        self.lang = kwargs.get('lang')

        self.status_location = kwargs.get('status_location')

        self.service_instance = kwargs.get('service_instance')

        self.process = kwargs.get('process')

        self.status = kwargs.get('status')

        self.creation_time = kwargs.get('creation_time')

        self.data_inputs = kwargs.get('data_inputs')

        self.output_definitions = kwargs.get('output_definitions')

        self.process_outputs = kwargs.get('process_outputs')

        return self.xml()

class ExecuteRequest(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(ExecuteRequest, self).__init__(tag='Execute',
                namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Attribute(required=True)
    def version(self):
        pass

    @metadata.ows_zero_one_element()
    def identifier(self):
        pass

    @metadata.wps_zero_many_element(path='DataInputs',
            value_type=metadata.Input, output_list=True)
    def input(self):
        pass

    @metadata.wps_zero_one_element(value_type=(metadata.ResponseDocument,
        metadata.RawDataOutput))
    def response_form(self):
        pass

    @xml.Attribute()
    def language(self):
        pass

    def __call__(self, **kwargs):
        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        self.identifier = kwargs.get('identifier')

        self.input = kwargs.get('input')

        self.response_form = kwargs.get('response_form')

        self.language = kwargs.get('language')

        return self.xml()

class DescribeProcessResponse(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(DescribeProcessResponse, self).__init__(tag='ProcessDescriptions',
                namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @metadata.zero_many_element(value_type=metadata.ProcessDescription)
    def process_description(self):
        pass

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Attribute(required=True)
    def version(self):
        pass

    @xml.Attribute(required=True)
    def lang(self):
        pass

    def __call__(self, **kwargs):
        self.process_description = kwargs.get('process_description')

        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        self.lang = kwargs.get('lang')

        return self.xml()

class DescribeProcessRequest(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(DescribeProcessRequest, self).__init__(tag='DescribeProcess',
                namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Attribute(required=True)
    def version(self):
        pass

    @xml.Attribute()
    def language(self):
        pass

    @xml.Element(maximum=None, output_list=True)
    def identifier(self):
        pass

    def __call__(self, **kwargs):
        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        self.language = kwargs.get('language')

        self.identifier = kwargs.get('identifier')

        return self.xml()

class GetCapabilitiesResponse(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(GetCapabilitiesResponse, self).__init__(tag='Capabilities',
                namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Attribute(required=True)
    def version(self):
        pass

    @xml.Attribute()
    def update_sequence(self):
        pass

    @xml.Attribute(required=True)
    def lang(self):
        pass

    @xml.Element(namespace=ns.OWS, value_type=metadata.ServiceIdentification)
    def service_identification(self):
        pass

    @xml.Element(namespace=ns.OWS, value_type=metadata.ServiceProvider)
    def service_provider(self):
        pass

    @xml.Element(namespace=ns.OWS,
            path='OperationsMetadata',
            nsmap={'OperationsMetadata': ns.OWS},
            value_type=metadata.Operation,
            output_list=True)
    def operation(self):
        pass
    #def operations_metadata(self):
    #    pass

    @xml.Element(namespace=ns.WPS, value_type=metadata.Process, output_list=True)
    def process_offerings(self):
        pass

    @xml.Element(namespace=ns.WPS, value_type=metadata.Languages)
    def languages(self):
        pass

    @xml.Element(namespace=ns.WPS, store_as_attr=True, name='href',
            nsmap={'href':ns.XLINK}, minimum=0)
    def wsdl(self):
        pass

    def __call__(self, **kwargs):
        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        self.update_sequence = kwargs.get('update_sequence')

        self.lang = kwargs.get('lang')

        self.service_identification = kwargs.get('service_identification')

        self.service_provider = kwargs.get('service_provider')

        self.operations_metadata = kwargs.get('operations_metadata')

        self.process_offerings = kwargs.get('process_offerings')

        self.languages = kwargs.get('languages')

        self.wsdl = kwargs.get('wsdl')

        return self.xml()

class GetCapabilitiesRequest(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(GetCapabilitiesRequest, self).__init__(tag='GetCapabilities',
                namespace=ns.WPS,
                nsmap=ns.NSMAP,
                translator=metadata.WPSTranslator())

    @xml.Attribute(namespace=ns.XSI)
    def schema_location(self):
        pass

    @xml.Attribute()
    def language(self):
        pass

    @xml.Attribute(required=True)
    def service(self):
        pass

    @xml.Element(minimum=0, namespace=ns.OWS, path='AcceptVersions',
            nsmap={'AcceptVersions': ns.WPS})
    def version(self):
        pass

    def __call__(self, **kwargs):
        self.language = kwargs.get('language')

        self.service = kwargs.get('service')

        self.version = kwargs.get('version')

        return self.xml()
