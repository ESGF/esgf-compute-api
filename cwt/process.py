"""
Process Module.
"""
from __future__ import print_function

from builtins import object
import datetime
import json
import logging
import time
import warnings

from cwt import utilities
from cwt.errors import CWTError
from cwt.errors import MissingRequiredKeyError
from cwt.errors import WPSServerError
from cwt.errors import WPSTimeoutError
from cwt.gridder import Gridder
from cwt.named_parameter import NamedParameter
from cwt.parameter import Parameter
from cwt.variable import Variable
from owslib import wps

logger = logging.getLogger("cwt.process")


def input_output_to_dict(value):
    data = value.__dict__.copy()

    data["metadata"] = [x.__dict__ for x in data["metadata"]]

    # Included from ComplexData
    try:
        data["defaultValue"] = data["defaultValue"].__dict__
    except KeyError:
        pass

    try:
        data["supportedValues"] = [
            x.__dict__ for x in data["supportedValues"]
        ]
    except KeyError:
        pass

    return data


class StatusTracker(object):
    def __init__(self):
        self.history = {}
        self.start = None

    @property
    def elapsed(self):
        elapsed = datetime.datetime.now() - self.start

        return elapsed.total_seconds()

    def update(self, message):
        now = datetime.datetime.now()

        if self.start is None:
            self.start = now

        if message not in self.history:
            self.history[message] = now

            print(message)

            logger.info(message)


def ensure_list(x):
    if not isinstance(x, (list, tuple)):
        return [
            x,
        ]

    return x


class Process(Parameter):
    """A WPS Process

    Wraps a WPS Process.

    Arguments:
        process: A DescribeProcessResponse object.
        name: A string name for the process to be used as the input of another process.
    """

    def __init__(self, **kwargs):
        super(Process, self).__init__(kwargs.get("name", None))

        self._identifier = kwargs.get("identifier", None)

        self._client = kwargs.get("client", None)

        self.process = kwargs.get("process", None)

        self.inputs = ensure_list(kwargs.get("inputs", []))

        self.parameters = kwargs.get("parameters", {})

        self.domain = kwargs.get("domain", None)

        self.context = None

        self.processed = False

        self.status_tracker = None

    def _repr_html_(self):
        header = "<div><h1>{} ({})</h1></div><hr/>".format(
            self.title, self.identifier
        )

        inputs = "\n".join(["<li>{!r}</li>".format(x) for x in self.inputs])

        if self.domain is not None:
            domain = "<li>{!r}</li>".format(self.domain)
        else:
            domain = ""

        body = (
            "<div>"
            "<h3>Abstract</h3>"
            "<pre>{}</pre>"
            "<h3>Inputs</h3>"
            "<ul>{}</ul>"
            "<h3>Domain</h3>"
            "<ul>{}</ul>"
            "</div>"
        ).format(self.abstract, inputs, domain)

        return "{}{}".format(header, body)

    def __repr__(self):
        fmt = (
            "Process("
            "name={}, "
            "identifier={}, "
            "inputs={}, "
            "parameters={}, "
            "domain={}, "
            "title={}, "
            "process_outputs={}, "
            "data_inputs={}, "
            "status_supported={}, "
            "store_supported={}, "
            "process_version={})"
        )

        return fmt.format(
            self.name,
            self.identifier,
            self.inputs,
            self.parameters,
            self.domain,
            self.title,
            self.process_outputs,
            self.data_inputs,
            self.status_supported,
            self.store_supported,
            self.process_version,
        )

    @classmethod
    def from_owslib(cls, client, process):
        obj = cls(client=client, process=process)

        return obj

    @classmethod
    def from_dict(cls, data):
        """ Attempts to load a process from a dict. """
        obj = cls()

        try:
            obj._identifier = data["name"]

            obj.name = data["result"]

            obj.inputs = data["input"]
        except KeyError as e:
            raise MissingRequiredKeyError(e)

        obj.domain = data.get("domain", None)

        ignore = ("name", "input", "result", "domain")

        for name, value in list(data.items()):
            if name not in ignore:
                if name == "gridder":
                    obj.parameters[name] = Gridder.from_dict(value)
                else:
                    obj.parameters[name] = NamedParameter.from_string(
                        name, value
                    )

        return obj

    @property
    def identifier(self):
        try:
            return self.process.identifier
        except AttributeError:
            return self._identifier

    @property
    def title(self):
        try:
            return self.process.title
        except AttributeError:
            return None

    @property
    def process_outputs(self):
        try:
            return [
                input_output_to_dict(x) for x in self.process.processOutputs
            ]
        except AttributeError:
            return None

    @property
    def data_inputs(self):
        try:
            return [input_output_to_dict(x) for x in self.process.dataInputs]
        except AttributeError as e:
            return None

    @property
    def status_supported(self):
        try:
            return self.process.statusSupported
        except AttributeError:
            return None

    @property
    def store_supported(self):
        try:
            return self.process.storeSupported
        except AttributeError:
            return None

    @property
    def process_version(self):
        try:
            return self.process.processVersion
        except AttributeError:
            return None

    @property
    def abstract(self):
        try:
            return self.process.abstract
        except AttributeError:
            return None

    @property
    def metadata(self):
        try:
            return [x.__dict__ for x in self.process.metadata]
        except AttributeError:
            return None

    @property
    def processing(self):
        """Checks if the process is still working.

        This will update the wrapper with the latest status and return
        True if the process is waiting or running.

        Returns:
            A boolean denoting whether the process is still working.
        """
        if getattr(self, "_old_parse_response", None) is None:
            setattr(self, "_old_parse_response", self.context.parseResponse)

            def _new_parse_response(response):
                self._old_parse_response(response)

                wpsns = wps.getNamespace(response)

                status_element = response.find(
                    wps.nspath("Status/*", ns=wpsns)
                )

                self.context.percentCompleted = float(
                    status_element.attrib.get("percentCompleted", 0.0)
                )

            self.context.parseResponse = _new_parse_response

        self.context.checkStatus(sleepSecs=0)

        return self.accepted or self.started

    @property
    def exception_dict(self):
        if self.errored:
            return [x.__dict__ for x in self.context.errors]

        return None

    @property
    def accepted(self):
        return self.check_context_status("ProcessAccepted")

    @property
    def started(self):
        return self.check_context_status("ProcessStarted")

    @property
    def paused(self):
        return self.check_context_status("ProcessPaused")

    @property
    def failed(self):
        return self.check_context_status("ProcessFailed")

    @property
    def succeeded(self):
        return self.check_context_status("ProcessSucceeded")

    @property
    def errored(self):
        return self.check_context_status("Exception")

    @property
    def output(self):
        """ Return the output of the process if done. """
        if not self.succeeded:
            raise CWTError("No output available process has not succeeded")

        logger.debug(
            "Process output %r", self.context.processOutputs[0].data[0]
        )

        try:
            # CWT only expects a single output in json format
            data = json.loads(self.context.processOutputs[0].data[0])
        except json.JSONDecoderError:
            raise WPSServerError("Failed to decode process output as JSON")

        if isinstance(data, dict) and "uri" in data:
            output_data = Variable.from_dict(data)
        elif isinstance(data, (tuple, list)) and "uri" in data[0]:
            output_data = [Variable.from_dict(x) for x in data]
        else:
            output_data = data

        return output_data

    @property
    def status(self):
        msg = None

        if self.accepted:
            msg = "ProcessAccepted {!s}".format(self.context.statusMessage)
        elif self.started:
            msg = "ProcessStarted {!s} {!s}".format(
                self.context.statusMessage, self.context.percentCompleted
            )
        elif self.paused:
            msg = "ProcessPaused {!s} {!s}".format(
                self.context.statusMessage, self.context.percentCompleted
            )
        elif self.failed:
            msg = "ProcessFailed {!s}".format(self.context.statusMessage)
        elif self.succeeded:
            msg = "ProcessSucceeded"
        elif self.errored:
            exception_msg = "->".join(
                [x["text"] for x in self.exception_dict]
            )

            msg = "Exception {!s}".format(exception_msg)
        else:
            msg = "Status unavailable"

        return msg

    def describe(self):
        self.process = self._client._client.describeprocess(self.identifier)

    def __call__(self, *inputs, domain=None, **kwargs):
        new_process = self.copy(True)

        # Take inputs or override with keyword
        inputs = inputs or kwargs.pop("inputs", [])

        if not all([isinstance(x, (Process, Variable)) for x in inputs]):
            invalid = ", ".join(
                [
                    str(type(x))
                    for x in inputs
                    if not isinstance(x, (Process, Variable))
                ]
            )

            raise CWTError(
                "Positional arguments can only be Variable or Process. The following are invalid {}",
                invalid,
            )

        new_process.add_inputs(*inputs)

        new_process.set_domain(domain)

        new_process.add_parameters(**kwargs)

        return new_process

    def copy(self, blank=False):
        if self.process is not None:
            obj = Process.from_owslib(self._client, self.process)
        else:
            obj = Process(identifier=self.identifier, name=self.name)

        obj.context = self.context

        if not blank:
            try:
                obj.inputs = self.inputs.copy()
            except AttributeError:
                # Python2 compat
                obj.inputs = self.inputs[:]

            obj.parameters = self.parameters.copy()

            obj.domain = self.domain

        return obj

    def check_context_status(self, value):
        try:
            return self.context.status == value
        except AttributeError:
            raise CWTError("Process is missing a context")

    def wait(self, timeout=None, sleep=None):
        self.status_tracker = StatusTracker()

        if sleep is None:
            sleep = 1.0

        self.status_tracker.update(self.status)

        while self.processing:
            self.status_tracker.update(self.status)

            time.sleep(sleep)

            if timeout is not None and self.status_tracker.elapsed > timeout:
                raise WPSTimeoutError(self.status_tracker.elapsed)

        self.status_tracker.update(self.status)

        return self.succeeded

    @property
    def gridder(self):
        return self.get_parameter("gridder")

    @gridder.setter
    def gridder(self, value):
        if not isinstance(value, Gridder):
            raise CWTError("Value must be a cwt.Gridder instance")

        self.parameters["gridder"] = value

    def set_domain(self, domain):
        self.domain = domain

    def get_parameter(self, name, required=False):
        """Retrieves a parameter

        Args:
            name: A string name of the parameter.
            required: A boolean flag denoting whether the parameter is required.

        Returns:
            A NamedParameter object.

        Raises:
            Exception: The parameter is required and not present.
        """
        if name not in self.parameters and required:
            raise CWTError("Parameter {} is required but not present", name)

        return self.parameters.get(name, None)

    def add_parameters(self, *args, **kwargs):
        """Add a parameter.

        kwargs can contain two formats.

        k=v where v is a NamedParameter

        Args:
            args: A list of NamedParameter objects.
            kwargs: A dict of NamedParameter objects or k=v where k is the name and v is string.
        """
        for a in args:
            if not isinstance(a, NamedParameter):
                raise CWTError(
                    'Invalid parameter type "{}", should be a NamedParameter',
                    type(a),
                )

            self.parameters[a.name] = a

        for name, value in list(kwargs.items()):
            if not isinstance(value, (list, tuple)):
                value = [value]

            self.parameters[name] = NamedParameter(name, *value)

    def add_inputs(self, *args):
        """Set the inputs of the Process.

        Args:
            args: A list of Process/Variable objects.
        """
        self.inputs.extend(args)

    def to_data_inputs(self):
        return utilities.process_to_data_inputs(self)

    def to_document(self):
        return utilities.process_to_document(self)

    def visualize(self, filename="compute", format="png"):
        processes, _ = self.collect_input_processes()

        dot = utilities._build_graph(processes)

        dot.render(filename, format=format, cleanup=True)

        return dot

    def collect_input_processes(self):
        """Aggregates the process trees inputs.

        A DFS to collect the trees inputs into two lists, Operations and Variables.

        Returns:
            A two lists, one of Processes and the other of Variables.
        """
        processes = {}
        inputs = {}
        stack = [
            self,
        ]

        while stack:
            item = stack.pop()

            logger.info("Processing %r", item)

            for x in item.inputs:
                if isinstance(x, Process):
                    if x.name not in processes:
                        stack.append(x)
                elif isinstance(x, Variable):
                    inputs[x.name] = x

            processes[item.name] = item

        return processes, inputs

    def to_dict(self):
        """ Returns a dictionary representation."""
        data = {"name": self.identifier, "result": self.name}

        if self.domain is not None:
            try:
                data["domain"] = self.domain.name
            except AttributeError:
                data["domain"] = self.domain

        inputs = []

        for i in self.inputs:
            try:
                inputs.append(i.name)
            except AttributeError:
                inputs.append(i)

        data["input"] = inputs

        gridder = self.parameters.get("gridder", None)

        if gridder is not None:
            data.update(
                {
                    "gridder": gridder.to_dict(),
                }
            )

        for name, value in list(self.parameters.items()):
            if name in ("gridder",):
                continue

            data.update(value.to_dict())

        return data

    def parameterize(self):
        """ Create a dictionary representation of the Process. """
        warnings.warn(
            "parameterize is deprecated, use to_dict instead",
            DeprecationWarning,
        )

        return self.to_dict()
