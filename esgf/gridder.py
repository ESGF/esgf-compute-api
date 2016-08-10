"""
Gridder Module.
"""

from .domain import Domain
from .parameter import Parameter
from .variable import Variable

class Gridder(Parameter):
    """ Gridder class.

    Defines a regridding to be performed during an operation.
    """
    def __init__(self, tool='esmf', method='linear', grid='T85', name=None):
        """ Gridder Init. """
        super(Gridder, self).__init__(name)

        self._tool = tool
        self._method = method
        self._grid = grid

    @property
    def tool(self):
        """ Tool property. """
        return self._tool

    @property
    def method(self):
        """ Method property. """
        return self._method

    @property
    def grid(self):
        """ Grid property. """
        return self._grid

    def _check_grid(self):
        """ Check that a grid is a string/Domain/Variable. """
        if (not isinstance(self._grid, str) and
                not isinstance(self._grid, Domain) and
                not isinstance(self._grid, Variable)):
            return False

        return True

    def parameterize(self):
        """ Parameterizes a gridder. """
        if not self._check_grid():
            raise TypeError(
                'Grid cannot be of type %s, only str, Domain or Variable.' %
                (type(self._grid),))

        # Handle different types of grids
        # pylint: disable=no-member
        if isinstance(self._grid, str):
            grid = self._grid
        else:
            grid = self._grid.name

        return {
            'tool': self._tool,
            'method': self._method,
            'grid': grid,
        }
