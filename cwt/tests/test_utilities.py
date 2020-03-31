import cwt

V0 = cwt.Variable('file:///test1.nc', 'tas')

D0 = cwt.Domain(time=slice(10, 20))

P0 = cwt.Process(identifier='CDAT.workflow', inputs=V0, domain=D0)

DATA_INPUTS = {
    'variable': [V0,],
    'domain': [D0,],
    'operation': [P0,],
}

RAW_DOC = '<wps100:Execute xmlns:ows110="http://www.opengis.net/ows/1.1" xmlns:wps100="http://www.opengis.net/wps/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="WPS" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd"><ows110:Identifier>CDAT.workflow</ows110:Identifier><wps100:DataInputs><wps100:Input><ows110:Identifier>variable</ows110:Identifier><wps100:Data><wps100:ComplexData mimeType="application/json">[{"uri": "file:///test1.nc", "id": "tas|170df910-ad06-4420-ad87-7256e0e839b7"}]</wps100:ComplexData></wps100:Data></wps100:Input><wps100:Input><ows110:Identifier>domain</ows110:Identifier><wps100:Data><wps100:ComplexData mimeType="application/json">[{"id": "d00832c5-9171-4d5f-abfb-334b7987c8d4", "time": {"start": 10, "end": 20, "step": 1, "crs": "indices"}}]</wps100:ComplexData></wps100:Data></wps100:Input><wps100:Input><ows110:Identifier>operation</ows110:Identifier><wps100:Data><wps100:ComplexData mimeType="application/json">[{"name": "CDAT.workflow", "result": "f7adec78-503a-4123-bfc2-81e1c62d457e", "domain": "d00832c5-9171-4d5f-abfb-334b7987c8d4", "input": ["170df910-ad06-4420-ad87-7256e0e839b7"]}]</wps100:ComplexData></wps100:Data></wps100:Input></wps100:DataInputs></wps100:Execute>'

def test_data_inputs_to_doc():
    doc = cwt.utilities.data_inputs_to_doc('CDAT.workflow', DATA_INPUTS).decode()

    assert V0.uri in doc
    assert V0.name in doc
    assert V0.var_name in doc

    assert D0.name in doc

    assert P0.name in doc
    assert P0.identifier in doc

def test_doc_to_data_inputs():
    identifier, data_inputs = cwt.utilities.doc_to_data_inputs(RAW_DOC)

    assert 'CDAT.workflow' == identifier

    assert 'variable' in data_inputs

    assert 'domain' in data_inputs

    assert 'operation' in data_inputs
