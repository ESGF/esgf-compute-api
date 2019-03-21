from cwt.wps_client import WPSClient  # noqa
from cwt.variable import Variable  # noqa
from cwt.process import Process  # noqa
from cwt.parameter import Parameter  # noqa
from cwt.named_parameter import NamedParameter  # noqa
from cwt.mask import Mask  # noqa
from cwt.gridder import Gridder  # noqa
from cwt.errors import WPSTimeoutError  # noqa
from cwt.errors import WPSClientError  # noqa
from cwt.errors import MissingRequiredKeyError  # noqa
from cwt.errors import CWTError  # noqa
from cwt.domain import Domain  # noqa
from cwt.dimension import Dimension  # noqa
from cwt.dimension import TIMESTAMPS  # noqa
from cwt.dimension import INDICES  # noqa
from cwt.dimension import VALUES  # noqa
from cwt.dimension import CRS  # noqa
"""
WPS Client library imports.
"""


import warnings

warnings.simplefilter('default')

__version__ = 'devel'


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
