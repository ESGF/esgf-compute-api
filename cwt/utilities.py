import json

import owslib
from owslib import wps
from owslib.etree import etree
from owslib.namespaces import Namespaces

import cwt

def prepare_data_inputs(process, inputs, domain, **kwargs):
    """ Preparse a process inputs for the data_inputs string.

    Args:
        process: A object of type Process to be executed.
        inputs: A list of Variables/Operations.
        domain: A Domain object.
        kwargs: A dict of addiontal named_parameters or k=v pairs.

    Returns:
        A dictionary containing the operations, domains and variables
        associated with the process.
    """
    data_inputs = _prepare_data_inputs(process, inputs, domain, **kwargs)

    variable = json.dumps([x.to_dict() for x in list(data_inputs['variable'])])

    domain = json.dumps([x.to_dict() for x in list(data_inputs['domain'])])

    operation = json.dumps([x.to_dict() for x in list(data_inputs['operation'])])

    return variable, domain, operation

def _prepare_data_inputs(process, inputs, domain, **kwargs):
    temp_process = process.copy()

    domains = {}

    if domain is not None:
        domains[domain.name] = domain

        temp_process.domain = domain

    if inputs is not None:
        if not isinstance(inputs, (list, tuple)):
            inputs = [inputs, ]

        temp_process.inputs.extend(inputs)

    if 'gridder' in kwargs:
        temp_process.gridder = kwargs.pop('gridder')

    temp_process.add_parameters(**kwargs)

    operation, variable = temp_process.collect_input_processes()

    # Collect all the domains from nested processes
    for item in list(operation.values()):
        if item.domain is not None and item.domain.name not in domains:
            domains[item.domain.name] = item.domain

    return {
        'variable': list(variable.values()),
        'domain': list(domains.values()),
        'operation': list(operation.values()),
    }

def patch_ns(path, ns):
    new_path = []

    for x in path.split('/'):
        p = x.split(':')

        if len(p) > 1:
            new_path.append('{{{0}}}{1}'.format(ns.get_namespace(p[0]), p[1]))
        else:
            new_path.append(p[0])

    return '/'.join(new_path)

def data_inputs_to_document(identifier, data_inputs):
    variable = json.dumps([x.to_dict() for x in data_inputs.get('variable', [])])

    domain = json.dumps([x.to_dict() for x in data_inputs.get('domain', [])])

    operation = json.dumps([x.to_dict() for x in data_inputs.get('operation', [])])

    variable = wps.ComplexDataInput(variable, mimeType='application/json')

    domain = wps.ComplexDataInput(domain, mimeType='application/json')

    operation = wps.ComplexDataInput(operation, mimeType='application/json')

    data_inputs = [('variable', variable), ('domain', domain), ('operation', operation)]

    execution = owslib.wps.WPSExecution()

    requestElement = execution.buildRequest(identifier, data_inputs)

    return etree.tostring(requestElement).decode()

def _document_to_data_inputs(doc):
    ns = Namespaces()

    doc = etree.fromstring(doc)

    identifier= doc.find(patch_ns('./ows110:Identifier', ns))

    data_inputs = {}

    for x in doc.findall(patch_ns('./wps100:DataInputs/wps100:Input', ns)):
        input_identifier = x.find(patch_ns('./ows110:Identifier', ns)).text

        value = x.find(patch_ns('./wps100:Data/wps100:ComplexData', ns))

        if input_identifier == 'variable':
            data_inputs[input_identifier] = [cwt.Variable.from_dict(x) for x in json.loads(value.text)]
        elif input_identifier == 'domain':
            data_inputs[input_identifier] = [cwt.Domain.from_dict(x) for x in json.loads(value.text)]
        elif input_identifier == 'operation':
            data_inputs[input_identifier] = [cwt.Process.from_dict(x) for x in json.loads(value.text)]
        else:
            raise Exception('Unsupported input {0}'.format(input_identifier))

    return identifier.text, data_inputs

def _flatten_data_inputs(data_inputs):
    output = {}

    output['variable'] = [x.to_dict() for x in data_inputs['variable']]

    output['domain'] = [x.to_dict() for x in data_inputs['domain']]

    output['operation'] = [x.to_dict() for x in data_inputs['operation']]

    return output

def document_to_data_inputs(document):
    _, data_inputs = _document_to_data_inputs(document)

    return json.dumps(_flatten_data_inputs(data_inputs))

def process_to_data_inputs(process, inputs=None, domain=None, **kwargs):
    data_inputs = _prepare_data_inputs(process, inputs, domain, **kwargs)

    return json.dumps(_flatten_data_inputs(data_inputs))

def process_to_document(process, inputs=None, domain=None, **kwargs):
    data_inputs = _prepare_data_inputs(process, inputs, domain, **kwargs)

    return data_inputs_to_document(process.identifier, data_inputs)
