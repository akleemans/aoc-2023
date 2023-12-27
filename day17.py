import queue
from typing import List, Set

from utils import dir_map, turn_map, add, in_bounds

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


def get_hash(coord, direction, straight):
    return f'{coord}-{direction}-{straight}'


def dijkstra(cost_map: List[str], min_moves, max_moves) -> int:
    """
    Use a priority queue (!) on possible next nodes while keeping track of visited nodes. Because we always work with the
    move with the lowest cost, we can guarantee to be finished if we first reach the end.
    Uses a PriorityQueue (inserting: O(log n), removing: O(1))
    Inspiration: https://github.com/biggysmith/advent_of_code_2023/blob/master/src/day17/day17.cpp
    """
    pqueue = queue.PriorityQueue()
    visited_moves: Set[str] = set()
    cost_map = [[int(c) for c in line] for line in cost_map]

    # Tuple: cost, coord, direction, straight
    pqueue.put((0, (0, 0), 'R', 0))
    pqueue.put((0, (0, 0), 'D', 0))

    while not pqueue.empty():
        cost, coord, direction, straight = pqueue.get()
        move_hash = get_hash(coord, direction, straight)
        if move_hash in visited_moves:
            continue
        visited_moves.add(move_hash)

        if coord == (len(cost_map) - 1, len(cost_map[0]) - 1):
            return cost

        # Add turn moves
        if straight >= min_moves - 1:
            for d in turn_map[direction]:
                new_row, new_col = add(coord, dir_map[d])
                if in_bounds(new_row, new_col, cost_map):
                    new_cost = cost + cost_map[new_row][new_col]
                    pqueue.put((new_cost, (new_row, new_col), d, 0))

        # Add straight moves, if available
        if straight < max_moves - 1:
            new_row, new_col = add(coord, dir_map[direction])
            if in_bounds(new_row, new_col, cost_map):
                new_cost = cost + cost_map[new_row][new_col]
                pqueue.put((new_cost, (new_row, new_col), direction, straight + 1))


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
