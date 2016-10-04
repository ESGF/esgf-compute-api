"""
Gridder Unittest
"""

from unittest import TestCase

from esgf import Gridder
from esgf import Domain
from esgf import Variable

class TestGridder(TestCase):
    """ Gridder Test Case. """

    def test_repr(self):
        """ Test repr value. """
        gridder = Gridder('scrip', 'nearestneighbor', 'T95')

        self.assertEqual(repr(gridder),
                         """Gridder('scrip', 'nearestneighbor', 'T95', 'gridder')""")

    def test_str(self):
        """ Test str value. """
        gridder = Gridder('scrip', 'nearestneighbor', 'T95')

        self.assertEqual(str(gridder),
                         """scrip nearestneighbor T95 gridder""")

    def test_gridder(self):
        """ Init and type checking. """
        gridder = Gridder('scrip', 'nearestneighbor', 'T95')

        self.assertEqual(gridder.tool, 'scrip')
        self.assertEqual(gridder.method, 'nearestneighbor')
        self.assertEqual(gridder.grid, 'T95')
        self.assertIsNotNone(gridder.name)

        expected = {
            'tool': 'scrip',
            'method': 'nearestneighbor',
            'grid': 'T95',
        }

        self.assertEqual(gridder.parameterize(), expected)

    def test_domain(self):
        """ Passing domain as grid argument. """
        domain = Domain(name='d0')

        gridder = Gridder('scrip', 'nearestneighbor', grid=domain)

        self.assertEqual(gridder.grid, domain)

        expected = {
            'tool': 'scrip',
            'method': 'nearestneighbor',
            'grid': 'd0',
        }

        self.assertEqual(gridder.parameterize(), expected)

    def test_variable(self):
        """ Passing variable as grid argument. """
        variable = Variable('file://test.nc', 'ta', name='v0')

        gridder = Gridder('scrip', 'nearestneighbor', grid=variable)

        self.assertEqual(gridder.grid, variable)

        expected = {
            'tool': 'scrip',
            'method': 'nearestneighbor',
            'grid': 'v0',
        }

        self.assertEqual(gridder.parameterize(), expected)
