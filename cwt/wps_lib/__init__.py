#! /usr/bin/env python

from __future__ import absolute_import

from .metadata import ProcessAccepted
from .metadata import ProcessStarted
from .metadata import ProcessPaused
from .metadata import ProcessSucceeded
from .metadata import ProcessFailed

accepted = ProcessAccepted()
started = ProcessStarted()
paused = ProcessPaused()
succeeded = ProcessSucceeded()
failed = ProcessFailed()

from .metadata import MissingParameterValue
from .metadata import InvalidParameterValue
from .metadata import VersionNegotiationFailed
from .metadata import InvalidUpdateSequence
from .metadata import NoApplicableCode
from .metadata import NotEnoughStorage
from .metadata import ServerBusy
from .metadata import FileSizeExceeded
from .metadata import StorageNotSupported

from .metadata import ExceptionReport
