from typing import Tuple, List

# Graph / node related stuff

dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
dir_reverse = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
turn_map = {'R': 'UD', 'L': 'UD', 'U': 'LR', 'D': 'LR'}


def in_bounds(row, col, grid) -> bool:
    """Check if coordinates are in bounds of grid"""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def add(a, b) -> Tuple[int, int]:
    """Add two coordinate tuples"""
    return a[0] + b[0], a[1] + b[1]


def subtract(a, b) -> Tuple[int, int]:
    """Subtract two coordinate tuples"""
    return a[0] - b[0], a[1] - b[1]


# Math

def gcd(n, m):
    """Calculate GCD (greatest common divisor)"""
    if m == 0:
        return n
    return gcd(m, n % m)


def lcm(numbers):
    """Calculates the LCM (least common multiple) for a list of numbers"""
    l = 1
    for n in numbers:
        l = l * n // gcd(l, n)
    return l


# PriorityQueue


class PriorityQueue:
    queue: List[Tuple[int, Tuple[int, int], str, int]]

    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def ceil(self, n: float):
        return int(-1 * n // 1 * -1)

    def floor(self, n):
        return int(n // 1)

    def put(self, el):
        """Insert using binary search"""
        queue = self.queue
        if len(queue) == 0:
            queue.append(el)
            return
        l = 0
        r = len(queue) - 1
        while l != r:
            m = self.ceil((l + r) / 2)
            if queue[m] > el:
                r = m - 1
            else:
                l = m
        if queue[l] < el:
            l += 1
        queue.insert(l, el)

    def get(self):
        return self.queue.pop(0)
