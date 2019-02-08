"""
WPS Client library imports.
"""
from __future__ import absolute_import

import warnings

warnings.simplefilter('default')

__version__ = 'devel'

from cwt.dimension import CRS
from cwt.dimension import VALUES
from cwt.dimension import INDICES
from cwt.dimension import TIMESTAMPS
from cwt.dimension import Dimension
from cwt.domain import Domain
from cwt.errors import CWTError
from cwt.errors import MissingRequiredKeyError
from cwt.errors import WPSClientError
from cwt.errors import WPSTimeoutError
from cwt.gridder import Gridder
from cwt.mask import Mask
from cwt.named_parameter import NamedParameter
from cwt.parameter import Parameter
from cwt.process import Process
from cwt.variable import Variable
from cwt.wps_client import WPSClient

NorthernHemisphere = Dimension('latitude', 0, 90)
SouthernHemisphere = Dimension('latitude', -90, 0)
Tropics = Dimension('latitude', -23.4, 23.4)
ArticZone = Dimension('latitude', 66.6, 90.0)
AntarcticZone = Dimension('latitude', -90, -66.6)

T21 = Gridder(grid='gaussian~32')
T42 = Gridder(grid='gaussian~64')
T63 = Gridder(grid='gaussian~96')

UQuart = Gridder(grid='uniform~.25x.25')
UHalf = Gridder(grid='uniform~.5x.5')
U1 = Gridder(grid='uniform~1x1')
U2 = Gridder(grid='uniform~2x2')
