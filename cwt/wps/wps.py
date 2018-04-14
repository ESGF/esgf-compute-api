import datetime

from cwt.wps.raw.wps import *
from cwt.wps.raw import ows

def status_accepted(message):
    """ Status Accepted

    Args:
        message (str): Status message.

    Returns:
        cwt.wps.raw.wps.StatusType
    """
    status = StatusType()

    status.creationTime = datetime.datetime.now()

    status.ProcessAccepted = message

    return status

def process_started(message, percent):
    """ Process Started

    Args:
        message (str): Status message.
        percent (int): Status percent completed

    Returns:
        cwt.wps.raw.wps.ProcessStartedType
    """
    started = ProcessStartedType(message)

    started.percentComplete = percent

    return started

def status_started(message, percent):
    """ Status Started

    Args:
        message (str): Status message.
        percent (int): Status percent completed

    Returns:
        cwt.wps.raw.wps.StatusType
    """
    status = StatusType()

    status.creationTime = datetime.datetime.now()

    status.ProcessStarted = process_started(message, percent)

    return status

def status_paused(message, percent):
    """ Status Paused

    Args:
        message (str): Status message.
        percent (int): Status percent completed

    Returns:
        cwt.wps.raw.wps.StatusType
    """
    status = StatusType()

    status.creationTime = datetime.datetime.now()

    status.ProcessPaused = process_started(message, percent)

    return status

def status_succeeded(message):
    """ Status Succeeded

    Args:
        message (str): Status message.

    Returns:
        cwt.wps.raw.wps.StatusType
    """
    status = StatusType()

    status.creationTime = datetime.datetime.now()

    status.ProcessSucceeded = message

    return status

def status_failed(message, code, version, locator=None):
    """ Status Failed

    Args:
        message (str): Exception message.
        code (str): Exception code.
        version (str): Version string.
        locator (str): Locator of exception.

    Returns:
        cwt.wps.raw.wps.StatusType
    """
    status = StatusType()

    status.creationTime = datetime.datetime.now()

    failed = ProcessFailedType()

    report = ows.ExceptionReport()

    report.version = ows.VersionType(version)

    exception = ows.ExceptionType()

    exception.exceptionCode = code
    
    if locator is not None:
        exception.locator = locator

    exception.ExceptionText = message

    report.Exception = [exception]

    failed.ExceptionReport = report

    status.ProcessFailed = failed

    return status

def output_data(identifier, title, data):
    """ Output Data

    Args:
        identifier (str): Output identifier.
        title (str): Output title.
        data (str): Output data.

    Returns:
        cwt.wps.raw.wps.OutputDataType
    """
    output = OutputDataType()

    output.Identifier = identifier

    output.Title = title

    data = DataType()

    complex_data = ComplexDataType()

    complex_data.Data = data

    data.ComplexData = complex_data

    output.Data = data

    return output

def execute_response(process, status, version, lang, service_instance, status_location, outputs):
    """ Execute response

    Args:
        process (cwt.wps.raw.wps.ProcessBriefType): Description of the process.
        status (cwt.wps.raw.wps.StatusType): Status of the process.
        version (str): Version of the process.
        lang (str): Language code.
        service_instance (str): Url that the service was called at.
        status_location (str): Url that the service status can be retrieved.
        outputs (list): List of process outputs.

    Returns:
        cwt.wps.raw.wps.ExecuteResponse
    """
    ex = ExecuteResponse()

    ex.lang = lang

    ex.version = ows.VersionType(version)

    ex.service = 'WPS'

    ex.serviceInstance = service_instance

    ex.statusLocation = status_location

    ex.Process = process

    ex.Status = status

    process_outputs = CTD_ANON_5()

    process_outputs.Output = outputs

    ex.ProcessOutputs = process_outputs

    return ex

def data_input(identifier, title, data):
    """ Data Input

    Args:
        identifier (str): Input identifier.
        title (str): Input title.
        data (str): Input data.

    Returns:
        cwt.wps.raw.wps.InputType
    """
    data_input = InputType()

    data_input.Identifier = identifier

    data_input.Title = title

    data_input.Data = data

    return data_input

def execute(identifier, version, inputs):
    """ Execute

    Args:
        identifier (str): Process identifier.
        version (str): Process version.
        inputs (list): List of inputs for the process.

    Returns:
        cwt.wps.raw.wps.Execute
    """
    ex = Execute()

    ex.Identifier = identifier

    ex.version = ows.VersionType(version)

    ex.service = 'WPS'

    data_inputs = DataInputsType()

    data_inputs.Input = inputs

    ex.DataInputs = data_inputs

    return ex

def process_output_description(identifier, title, mime_type):
    """ Process Output Description

    Args:
        identifier (str): Output identifier.
        title (str): Output title.
        mime_type (str): Mimetype of the output data.

    Returns:
        cwt.wps.raw.wps.OutputDescriptionType
    """
    output = OutputDescriptionType()

    output.Identifier = identifier

    output.Title = title

    complex_output = SupportedComplexDataType()

    combination_type = ComplexDataCombinationType()

    format = ComplexDataDescriptionType()

    format.MimeType = mime_type

    combination_type.Format = format

    complex_output.Default = combination_type

    combinations_type = ComplexDataCombinationsType()

    combinations_type.Format = [format]

    complex_output.Supported = combinations_type

    output.ComplexOutput = complex_output

    return output

def data_input_description(identifier, title, mime_type, min_occurs, max_occurs):
    """ Data Input Description

    Args:
        identifier (str): Input identifier.
        title (str): Input title.
        mime_type (str): Excepted mime_type of input data.
        min_occurs (int): Minimum number of allowed.
        max_occurs (int): Maximum number of allowed.

    Returns:
        cwt.wps.raw.wps.InputDescriptionType
    """
    description = InputDescriptionType()

    description.Identifier = identifier

    description.Title = title

    description.minOccurs = min_occurs

    description.maxOccurs = max_occurs

    data = SupportedComplexDataInputType()

    combination_type = ComplexDataCombinationType()

    format = ComplexDataDescriptionType()

    format.MimeType = mime_type

    combination_type.Format = format

    data.Default = combination_type

    combinations_type = ComplexDataCombinationsType()

    combinations_type.Format = [format]

    data.Supported = combinations_type

    description.ComplexData = data

    return description

def process_description(identifier, title, version, data_inputs, process_outputs):
    """ Process Description

    Args:
        identifier (str): Process identifier.
        title (str): Process title.
        version (str): Process version.
        data_inputs (list): List of input descriptions.
        process_outputs (list): List of output descriptions.

    Returns:
        cwt.wps.raw.wps.ProcessDescriptionType
    """
    process = ProcessDescriptionType()

    process.Identifier = identifier

    process.Title = title

    process.DataInputs = CTD_ANON()

    process.DataInputs.Input = data_inputs

    process.ProcessOutputs = CTD_ANON_()

    process.ProcessOutputs.Output = process_outputs

    process.processVersion = ows.VersionType(version)

    return process

def process_descriptions(lang, version, process):
    """ Process Descriptions

    Args:
        lang (str): Language code.
        version (str): Version of the process offerings.
        process (cwt.wps.raw.wps.Process): Process being described.

    Returns:
        cwt.wps.raw.wps.ProcessDescriptions
    """
    descriptions = ProcessDescriptions()

    descriptions.service = 'WPS'

    descriptions.lang = lang

    descriptions.version = ows.VersionType(version)

    descriptions.ProcessDescription = [process]

    return descriptions

def describe_process(identifier, version):
    """ Describe Process

    Args:
        identifier (str): Process identifier to describe.
        version (str): Version of the process to describe.

    Returns:
        cwt.wps.raw.cwt.DescribProcess:
    """
    process = DescribeProcess()

    process.Identifier = identifier

    process.version = ows.VersionType(version)

    process.service = 'WPS'

    return process

def process(identifier, title, version):
    """ Process

    Args:
        identifier (str): Process identifier.
        title (str): Process title.
        version (str): Process version.

    Returns:
        cwt.wps.raw.wps.ProcessBriefType:
    """
    process = ProcessBriefType()

    process.Identifier = identifier

    process.Title = title

    process.processVersion = version

    return process

def process_offerings(processes):
    """ Process Offerings

    Args:
        processes (list): List of processes available.

    Returns:
        cwt.wps.raw.wps.ProcessOfferings:
    """
    offerings = ProcessOfferings()

    offerings.Process = processes

    return offerings

def get_capabilities():
    """ GetCapabilities request

    Returns:
        cwt.wps.raw.wps.GetCapabilities:
    """
    capabilities = GetCapabilities()

    capabilities.service = 'WPS'

    return capabilities

def capabilities(identification, provider, metadata, offerings, lang, version):
    """ Capabilities response

    Args:
        identification (cwt.wps.raw.ows.ServiceIdentification): Service Identification.
        provider (cwt.wps.raw.ows.ServiceProvider): Service Provider.
        metadata (cwt.wps.raw.ows.OperationsMetadata): Operations Metadata.
        offerings (cwt.wps.raw.wps.ProcessOfferings): Process Offerings.
        lang (str): Language.
        version (str): Supported version.

    Returns:
        cwt.wps.raw.wps.Capabilities: 
    """
    capabilities = Capabilities()

    capabilities.ServiceIdentification = identification

    capabilities.ServiceProvider = provider

    capabilities.OperationsMetadata = metadata

    capabilities.ProcessOfferings = offerings

    languages = Languages()

    languages.Default = lang

    languages.Supported = lang

    capabilities.Languages = languages

    capabilities.version = ows.VersionType(version)

    capabilities.lang = lang

    capabilities.service = 'WPS'

    return capabilities
