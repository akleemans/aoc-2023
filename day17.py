from typing import List, Tuple, Set
from queue import PriorityQueue

test_data0 = '''19111
11291
91151'''.split('\n')

test_data = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split('\n')

dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
turn_map = {'R': 'UD', 'L': 'UD', 'U': 'LR', 'D': 'LR'}


class Move:
    def __init__(self, coord: Tuple[int, int], direction: str, cost: int, straight: int, path: str):
        self.coord = coord
        self.direction = direction
        self.cost = cost
        self.straight = straight
        self.path = path

    def hash(self):
        return f'{self.coord}-{self.direction}-{self.straight}'

    def __str__(self):
        return f'{self.coord}-{self.direction}-{self.cost}-{self.straight}'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        """Used for comparing in PriorityQueue"""
        return self.cost < other.cost


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def in_bounds(row, col, data) -> bool:
    return 0 <= row < len(data) and 0 <= col < len(data[0])


def dijkstra(cost_map: List[str], min_moves, max_moves) -> int:
    """
    Use a priority queue (!) on possible next nodes while keeping track of visited nodes. Because we always work with the
    move with the lowest cost, we can guarantee to be finished if we first reach the end.
    Uses a PriorityQueue (inserting: O(log n), removing: O(1))
    Inspiration: https://github.com/biggysmith/advent_of_code_2023/blob/master/src/day17/day17.cpp
    """
    queue = PriorityQueue()
    visited_moves: Set[str] = set()

    queue.put(Move((0, 0), 'R', 0, 0, ''))
    queue.put(Move((0, 0), 'D', 0, 0, ''))

    while not queue.empty():
        current_move = queue.get()
        if current_move.hash() in visited_moves:
            continue
        visited_moves.add(current_move.hash())

        if current_move.coord == (len(cost_map) - 1, len(cost_map[0]) - 1):
            return current_move.cost

        # Add turn moves
        if current_move.straight >= min_moves - 1:
            for d in turn_map[current_move.direction]:
                new_row, new_col = add(current_move.coord, dir_map[d])
                if in_bounds(new_row, new_col, cost_map):
                    cost = current_move.cost + int(cost_map[new_row][new_col])
                    queue.put(Move((new_row, new_col), d, cost, 0, current_move.path + d))

        # Add straight moves, if available
        if current_move.straight < max_moves - 1:
            new_row, new_col = add(current_move.coord, dir_map[current_move.direction])
            if in_bounds(new_row, new_col, cost_map):
                cost = current_move.cost + int(cost_map[new_row][new_col])
                queue.put(Move((new_row, new_col), current_move.direction, cost, current_move.straight + 1,
                               current_move.path + current_move.direction))


def part1(data: List[str]):
    return dijkstra(data, 1, 3)


def part2(data: List[str]):
    return dijkstra(data, 4, 10)


def main():
    with open('inputs/day17.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test0_result = part1(test_data0)
    assert part1_test0_result == 9, f'Part 1 test0 input returned {part1_test0_result}'
    part1_test_result = part1(test_data)
    assert part1_test_result == 102, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 785, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 94, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 922, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
