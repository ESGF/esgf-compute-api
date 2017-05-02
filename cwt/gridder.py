"""
Gridder Module.
"""

from cwt import parameter

__all__ = ['Gridder']

class Gridder(parameter.Parameter):
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

        self.tool = tool
        self.method = method
        self.grid = grid

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def parameterize(self):
        """ Parameterizes a gridder. """
        # Handle different types of grids
        # pylint: disable=no-member
        if isinstance(self.grid, (str, unicode)):
            grid = self.grid
        else:
            grid = self.grid.name

        return {
            'tool': self.tool,
            'method': self.method,
            'grid': grid,
        }

    def __repr__(self):
        return 'Gridder(tool=%r, method=%r, grid=%r)' % (
            self._tool,
            self._method,
            self.grid)
