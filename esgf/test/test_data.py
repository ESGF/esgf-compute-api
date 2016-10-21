"""
Data for mock testing.
"""
MOCK_EXECUTE_REQUEST = """<wps100:Execute xmlns:wps100="http://www.opengis.net/wps/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="WPS" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd"><ows110:Identifier xmlns:ows110="http://www.opengis.net/ows/1.1">averager.mv</ows110:Identifier><wps100:DataInputs/><wps100:ResponseForm><wps100:ResponseDocument status="True" storeExecuteResponse="True"><wps100:Output asReference="true"><ows110:Identifier xmlns:ows110="http://www.opengis.net/ows/1.1">output</ows110:Identifier></wps100:Output></wps100:ResponseDocument></wps100:ResponseForm></wps100:Execute>"""

MOCK_EXECUTE_RESPONSE = """<?xml version="1.0" encoding="utf-8"?>
<wps:ExecuteResponse xmlns:wps="http://www.opengis.net/wps/1.0.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd" service="WPS" version="1.0.0" xml:lang="en-CA" serviceInstance="http://localhost:8000/wps?service=WPS&amp;request=GetCapabilities&amp;version=1.0.0">
    <wps:Process wps:processVersion="None">
        <ows:Identifier>averager.mv</ows:Identifier>
        <ows:Title>CDUtil Averager</ows:Title>
    </wps:Process>
    <wps:Status creationTime="2016-10-21T16:54:03Z">
        <wps:ProcessFailed>
            <ows:ExceptionReport version="1.0.0">
                <ows:Exception exceptionCode="MissingParameterValue" locator="domain" />
            </ows:ExceptionReport>
        </wps:ProcessFailed>
    </wps:Status>
</wps:ExecuteResponse>
"""


MOCK_GETCAPABILITIES = """<?xml version="1.0" encoding="utf-8"?>
<wps:Capabilities service="WPS" version="1.0.0" xml:lang="en-CA" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:wps="http://www.opengis.net/wps/1.0.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd" updateSequence="1">
	<ows:ServiceIdentification>
		<ows:Title>WPS_ESGF_CWT</ows:Title>
		<ows:Abstract>See http://pywps.wald.intevation.org and http://www.opengeospatial.org/standards/wps</ows:Abstract>
		<ows:Keywords>
			<ows:Keyword>ESGF</ows:Keyword>
			<ows:Keyword>CDS</ows:Keyword>
			<ows:Keyword>GIS</ows:Keyword>
			<ows:Keyword>WPS</ows:Keyword>
			<ows:Keyword>UV-CDAT</ows:Keyword>
			<ows:Keyword>UVCDAT</ows:Keyword>
			<ows:Keyword>ESGF-CWT</ows:Keyword>
			<ows:Keyword>CWT</ows:Keyword>
			<ows:Keyword>ESGCWT</ows:Keyword>
		</ows:Keywords>
		<ows:ServiceType>WPS</ows:ServiceType>
		<ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
		<ows:Fees>None</ows:Fees>
		<ows:AccessConstraints>none</ows:AccessConstraints>
	</ows:ServiceIdentification>
	<ows:ServiceProvider>
		<ows:ProviderName>ESGF-CWT</ows:ProviderName>
		<ows:ProviderSite xlink:href="https://esgf.llnl.gov"/>
		<ows:ServiceContact>
			<ows:IndividualName>Our Best Guy</ows:IndividualName>
			<ows:PositionName>Senior Scientist</ows:PositionName>
			<ows:ContactInfo>
				<ows:Phone>
					<ows:Voice>123-456-7890</ows:Voice>
				</ows:Phone>
				<ows:Address>
					<ows:DeliveryPoint>Mailbox</ows:DeliveryPoint>
					<ows:City>Anytown</ows:City>
					<ows:PostalCode>12345</ows:PostalCode>
					<ows:Country>USA</ows:Country>
					<ows:ElectronicMailAddress>esgf-cwt@llnl.gov</ows:ElectronicMailAddress>
				</ows:Address>
				<ows:OnlineResource xlink:href="https://esgf.llnl.gov"/>
				<ows:HoursOfService>0:00-24:00</ows:HoursOfService>
				<ows:ContactInstructions>none</ows:ContactInstructions>
			</ows:ContactInfo>
			<ows:Role>Lead Developer</ows:Role>
		</ows:ServiceContact>
	</ows:ServiceProvider>
	<ows:OperationsMetadata>
		<ows:Operation name="GetCapabilities">
			<ows:DCP>
				<ows:HTTP>
					<ows:Get xlink:href="http://localhost:8000/wps?"/>
					<ows:Post xlink:href="http://localhost:8000/wps"/>
				</ows:HTTP>
			</ows:DCP>
		</ows:Operation>
		<ows:Operation name="DescribeProcess">
			<ows:DCP>
				<ows:HTTP>
					<ows:Get xlink:href="http://localhost:8000/wps?"/>
					<ows:Post xlink:href="http://localhost:8000/wps"/>
				</ows:HTTP>
			</ows:DCP>
		</ows:Operation>
		<ows:Operation name="Execute">
			<ows:DCP>
				<ows:HTTP>
					<ows:Get xlink:href="http://localhost:8000/wps?"/>
					<ows:Post xlink:href="http://localhost:8000/wps"/>
				</ows:HTTP>
			</ows:DCP>
		</ows:Operation>
	</ows:OperationsMetadata>
	<wps:ProcessOfferings>
		<wps:Process>
			<ows:Identifier>averager.mv</ows:Identifier>
			<ows:Title>CDUtil Averager</ows:Title>
		</wps:Process>
		<wps:Process>
			<ows:Identifier>averager.ophidia</ows:Identifier>
			<ows:Title>Ophidia Average</ows:Title>
		</wps:Process>
		<wps:Process>
			<ows:Identifier>test.echo</ows:Identifier>
			<ows:Title>Test Echo</ows:Title>
		</wps:Process>
		<wps:Process>
			<ows:Identifier>test.sleep</ows:Identifier>
			<ows:Title>Test Sleep</ows:Title>
		</wps:Process>
	</wps:ProcessOfferings>
	<wps:Languages>
		<wps:Default>
			<ows:Language>en-CA</ows:Language>
		</wps:Default>
		<wps:Supported>
			<ows:Language>en-CA</ows:Language>
		</wps:Supported>
	</wps:Languages>
	<wps:WSDL xlink:href="http://localhost:8000/wps?WSDL"/>
</wps:Capabilities>
"""
