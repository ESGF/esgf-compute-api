"""
WPS Client library imports.
"""
from __future__ import absolute_import

__version__ = '2.0.0'

from .mask import Mask

from .gridder import Gridder

from .process import Process
from .process import ProcessError

from .named_parameter import NamedParameter

from .variable import Variable

from .domain import Domain

from .dimension import CRS
from .dimension import Dimension

from .parameter import Parameter
from .parameter import ParameterError

from .wps import WPS
