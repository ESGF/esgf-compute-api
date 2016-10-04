"""
Gridder Module.
"""

from .domain import Domain
from .parameter import Parameter
from .variable import Variable

class Gridder(Parameter):
    """ Gridder.
    
    Describes the regridder and target grid for an operation.

    Gridder from a known target grid.

    >>> Gridder('esmf', 'linear', 'T85')

    Gridder from a Domain.

    >>> new_grid = Domain([Dimension(90, -90, step=1)], name='lat')
    >>> Gridder('esmf', 'linear', new_grid)

    Gridder from a Variable.

    >>> tas = Variable('http://thredds/tas.nc', 'tas', name='tas')
    >>> Gridder('esmf', 'linear', tas)

    Attributes:
        tool: A String name of the regridding tool to be used.
        method: A String method that the regridding tool will use.
        grid: A String, Domain or Variable of the target grid.
    """
    def __init__(self, tool='esmf', method='linear', grid='T85'):
        """ Gridder Init. """
        super(Gridder, self).__init__('gridder')

        self._tool = tool
        self._method = method
        self._grid = grid

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

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

    def parameterize(self):
        """ Parameterizes a gridder. """
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

    def __repr__(self):
        return 'Gridder(%r, %r, %r, %r)' % (
            self._tool,
            self._method,
            self._grid,
            self.name)

    def __str__(self):
        return '%s %s %s %s' % (
            self._tool,
            self._method,
            self._grid,
            self.name)
