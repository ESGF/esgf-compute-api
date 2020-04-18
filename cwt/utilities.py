import argparse
import hashlib
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

    return _flatten_data_inputs(data_inputs)

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
    data_inputs = dict((x, json.dumps(y)) for x, y in data_inputs.items())

    variable = wps.ComplexDataInput(data_inputs['variable'], mimeType='application/json')

    domain = wps.ComplexDataInput(data_inputs['domain'], mimeType='application/json')

    operation = wps.ComplexDataInput(data_inputs['operation'], mimeType='application/json')

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

    return _flatten_data_inputs(data_inputs)

def process_to_data_inputs(process, inputs=None, domain=None, **kwargs):
    data_inputs = _prepare_data_inputs(process, inputs, domain, **kwargs)

    return _flatten_data_inputs(data_inputs)

def process_to_document(process, inputs=None, domain=None, **kwargs):
    data_inputs = _prepare_data_inputs(process, inputs, domain, **kwargs)

    return data_inputs_to_document(process.identifier, _flatten_data_inputs(data_inputs))

def command_document_to_data_inputs():
    parser = argparse.ArgumentParser()

    parser.add_argument('document', type=str)

    args = vars(parser.parse_args())

    print(json.dumps(document_to_data_inputs(args['document'])))

def command_data_inputs_to_document():
    parser = argparse.ArgumentParser()

    parser.add_argument('identifier', type=str)
    parser.add_argument('data-inputs', type=str)

    args = vars(parser.parse_args())

    print(data_inputs_to_document(args['identifier'], json.loads(args['data-inputs'])))

def _load_input(input):
    try:
        data_inputs = document_to_data_inputs(input)
    except Exception as e:
        print(e)
        data_inputs = json.loads(input)

    return data_inputs

def _load_data_inputs(data_inputs):
    variable = [cwt.Variable.from_dict(x) for x in data_inputs['variable']]
    variable = dict((x.name, x) for x in variable)

    domain = [cwt.Domain.from_dict(x) for x in data_inputs['domain']]
    domain = dict((x.name, x) for x in domain)

    operation = [cwt.Process.from_dict(x) for x in data_inputs['operation']]
    operation = dict((x.name, x) for x in operation)

    for name, x in operation.items():
        x.domain = domain.get(x.domain, None)

        x.inputs = [variable[y] if y in variable else operation[y] for y in x.inputs]

    return variable, domain, operation

def _build_init(data, vars):
    lines = []

    for x in data.values():
        name = '{}_{}'.format(x.__class__.__name__.lower(), hashlib.sha256(x.name.encode()).hexdigest()[:8])

        vars[x.name] = name

        lines.append('{} = {}\n'.format(name, repr(x)))

    return lines


def _build_code(data_inputs, **kwargs):
    variable, domain, operation = _load_data_inputs(data_inputs)

    sections = []

    imports = [
        'import os\n',
        'from cwt import Domain\n',
        'from cwt import Dimension\n',
        'from cwt import Variable\n',
        'from cwt import CRS\n',
    ]

    if kwargs['llnl_client']:
        imports.append('from cwt.llnl_client import LLNLClient\n')
    else:
        imports.append('from cwt.wps_client import WPSClient\n')

    sections.append(imports)

    if kwargs['llnl_client']:
        sections.append([
            'client = LLNLClient({!r})\n'.format(kwargs['wps_url']),
        ])
    else:
        sections.append([
            'client = WPSClient({!r})\n'.format(kwargs['wps_url']),
        ])

    vars = {}

    sections.append(_build_init(variable, vars))

    sections.append(_build_init(domain, vars))

    in_deg = dict((x.name, len([x for x in x.inputs if x.name in operation])) for x in operation.values())

    out_deg = dict((x.name, len([y for y in operation.values() if any(x.name == z.name for z in y.inputs)])) for x in operation.values())

    neighbors = dict((x, [y for y in operation.values() if x in [z.name for z in y.inputs]]) for x in in_deg.keys())

    queue = [operation[x] for x, y in in_deg.items() if y == 0]

    processes = []

    while len(queue) > 0:
        current = queue.pop(0)

        name = '{}_{}'.format(current.__class__.__name__.lower(), hashlib.sha256(current.name.encode()).hexdigest()[:8])

        vars[current.name] = name

        inputs = ', '.join([vars[x.name] for x in current.inputs])

        domain = ', domain={}'.format(vars[current.domain.name]) if current.domain is not None else ''

        params = ['{}={}'.format(x, y.values) for x, y in current.parameters.items()]

        params = ', {}'.format(', '.join(params)) if len(params) > 0 else ''

        processes.append('{} = client.{}({}{}{})\n\n'.format(name, current.identifier, inputs, domain, params))

        for x in neighbors[current.name]:
            in_deg[x.name] -= 1

            if in_deg[x.name] == 0:
                queue.append(x)

    sections.append(processes)

    outputs = [vars[x] for x, y in out_deg.items() if y == 0]

    outputs_str = ', '.join(outputs)

    sections.append([
        'client.execute({})\n\n'.format(outputs_str),
        '{}.wait()\n'.format(outputs[0]),
    ])

    return sections

def _write_script(data_inputs, **kwargs):
    sections = _build_code(data_inputs, **kwargs)

    with open(kwargs['output_path'], 'w') as f:
        for x in sections:
            f.writelines(x)

            f.write('\n')

def command_convert():
    parser = argparse.ArgumentParser()

    output_choices = ('script',)

    parser.add_argument('output', help='Conversion output.', choices=output_choices)
    parser.add_argument('input', help='Input can be WPS document or data_inputs.')
    parser.add_argument('--wps-url', help='Url for the WPS server.', default='https://aims2.llnl.gov/wps')
    parser.add_argument('--llnl-client', action='store_true', help='Uses LLNL Client.')
    parser.add_argument('--output-path', help='Output path for file.', default='compute.py')

    kwargs = vars(parser.parse_args())

    try:
        data_inputs = _load_input(kwargs['input'])
    except Exception:
        raise cwt.CWTError('Failed to load input')

    if kwargs['output'] == 'script':
        _write_script(data_inputs, **kwargs)
