import unittest

import day03


class TestNeighbors(unittest.TestCase):
    data = ['123', '456', '789']

    def test_get_coord(self):
        self.assertEqual('1', day03.get_coord(self.data, (0, 0)))
        self.assertEqual('6', day03.get_coord(self.data, (2, 1)))
        self.assertEqual('9', day03.get_coord(self.data, (2, 2)))

    def test_get_coord_oob(self):
        self.assertEqual('.', day03.get_coord(self.data, (-1, 0)))
        self.assertEqual('.', day03.get_coord(self.data, (-2, -1)))
        self.assertEqual('.', day03.get_coord(self.data, (0, -1)))
        self.assertEqual('.', day03.get_coord(self.data, (3, 0)))
        self.assertEqual('.', day03.get_coord(self.data, (0, 3)))

    def test_get_neighbors_corner(self):
        neighbor_set = set(day03.get_neighbors(self.data, (0, 0)))
        self.assertEqual({'.', '2', '5', '4'}, neighbor_set)

    def test_get_neighbors_edge(self):
        neighbor_set = set(day03.get_neighbors(self.data, (2, 1)))
        self.assertEqual({'.', '2', '3', '5', '8', '9'}, neighbor_set)

    def test_get_neighbors_center(self):
        neighbor_set = set(day03.get_neighbors(self.data, (1, 1)))
        self.assertEqual({'1', '2', '3', '4', '6', '7', '8', '9'}, neighbor_set)
