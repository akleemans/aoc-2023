import unittest

import day18


class TestShoelace(unittest.TestCase):

    def test_shoelace(self):
        self.assertEqual(4, day18.area_shoelace([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]))
        self.assertEqual(9, day18.area_shoelace([(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]))
        self.assertEqual(13, day18.area_shoelace([(0, 0), (0, 2), (1, 2), (1, 4), (2, 4), (2, 0), (0, 0)]))
        self.assertEqual(23, day18.area_shoelace([(0, 0), (0, 7), (1, 7), (1, 6), (2, 6), (2, 0), (0, 0)]))
