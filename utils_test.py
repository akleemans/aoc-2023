import unittest

import utils


class TestUtils(unittest.TestCase):

    def test_dir_map(self):
        self.assertEqual((0, 1), utils.dir_map['R'])
        self.assertEqual((0, -1), utils.dir_map['L'])
        self.assertEqual((1, 0), utils.dir_map['D'])
        self.assertEqual((-1, 0), utils.dir_map['U'])

    def test_turn_map(self):
        self.assertTrue('U' in utils.turn_map['R'])
        self.assertTrue('D' in utils.turn_map['R'])
        self.assertTrue('L' in utils.turn_map['D'])
        self.assertTrue('R' in utils.turn_map['D'])

    def test_in_bounds(self):
        grid = [[1, 1, 1], [2, 2, 2]]
        self.assertTrue(utils.in_bounds(0, 0, grid))
        self.assertTrue(utils.in_bounds(0, 1, grid))
        self.assertTrue(utils.in_bounds(1, 2, grid))
        self.assertFalse(utils.in_bounds(2, 1, grid))
        self.assertFalse(utils.in_bounds(-1, 1, grid))

    def test_add(self):
        self.assertEqual((3, 5), utils.add((1, 2), (2, 3)))
        self.assertEqual((4, 4), utils.add((0, 1), (4, 3)))

    def test_subtract(self):
        self.assertEqual((-1, -1), utils.subtract((1, 2), (2, 3)))
        self.assertEqual((0, 1), utils.subtract((4, 1), (4, 0)))

    def test_priority_queue(self):
        queue = utils.PriorityQueue()
        queue.put(4)
        queue.put(2)
        queue.put(1)
        queue.put(3)
        queue.put(5)
        self.assertEqual([1, 2, 3, 4, 5], queue.queue)
        self.assertEqual(1, queue.get())
        self.assertEqual([2, 3, 4, 5], queue.queue)

    def test_gcd(self):
        self.assertEqual(5, utils.gcd(10, 15))
        self.assertEqual(7, utils.gcd(7, 21))

    def test_lcm(self):
        self.assertEqual(70, utils.lcm([2, 5, 7]))
        self.assertEqual(420, utils.lcm([2, 3, 4, 5, 7]))
