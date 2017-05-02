"""
WPS Client library imports.
"""
from __future__ import absolute_import

__version__ = '2.0.0'

from .dimension import *
from .domain import *
from .gridder import *
from .mask import *
from .named_parameter import *
from .parameter import *
from .process import *
from .variable import *
from .wps import *

T21 = Gridder(grid='gaussian~32'
T42 = Gridder(grid='gaussian~64'
T63 = Gridder(grid='gaussian~128'

UF25 = Gridder(grid='uniform~.25'
UF5 = Gridder(grid='uniform~.5'
U1 = Gridder(grid='uniform~1'
U2 = Gridder(grid='uniform~2'
