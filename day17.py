from typing import List, Tuple
#import sys
#sys.setrecursionlimit(10000)

# Day 17: Clumsy Crucible

test_data0 = '''19211
11191
99191
99911'''.split('\n')

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
dir_turn = {'R': 'DU', 'L': 'DU', 'U': 'RL', 'D': 'RL'}


def add(a, b) -> Tuple[int, int]:
    """Add two coordinates"""
    return a[0] + b[0], a[1] + b[1]


def in_bounds(row: int, col: int, data: List[str]):
    return 0 <= row < len(data) and 0 <= col < len(data[0])


def part1(data: List[str]):
    heat_losses = [[10 ** 6 for i in data[0]] for j in data]

    def go_next(row, col, last_value: int, path: str, not_optimal_for):
        if not_optimal_for >= 3 or heat_losses[-1][-1] < last_value:
            return
        direction = path[-1]
        add_coord = dir_map[direction]
        new_row, new_col = add((row, col), add_coord)
        if not in_bounds(new_row, new_col, data):
            return
        next_value = last_value + int(data[new_row][new_col])
        # Update value
        if heat_losses[new_row][new_col] < next_value:
            # Can't be too low, else a simpler way is possible
            #if heat_losses[new_row][new_col] < (next_value - 10):
            #    return
            not_optimal_for += 1
        else:
            not_optimal_for = 0

        heat_losses[new_row][new_col] = min(next_value, heat_losses[new_row][new_col])
        if new_row == len(data) - 1 and new_col == len(data[0]) - 1:
            return

        # Turn
        for d in dir_turn[direction]:
            go_next(new_row, new_col, next_value, path + d, not_optimal_for)

        # If not yet 3 times straight, go
        if path[-3:] != direction * 3:
            go_next(new_row, new_col, next_value, path + direction, not_optimal_for)


    go_next(0, 0, 0, 'R', 0)
    go_next(0, 0, 0, 'D', 0)

    return heat_losses[-1][-1]


def part2(data: List[str]):
    return 1


def main():
    with open('inputs/day17.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test0_result = part1(test_data0)
    print('Test input:', part1_test0_result)
    assert part1_test0_result == 10, f'Part 1 test input returned {part1_test0_result}'

    part1_test_result = part1(test_data)
    print('Test input:', part1_test_result)
    assert part1_test_result == 102, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    print('Part 1:', part1_result)  # remove
    assert part1_result == 0, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 0, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    print('Part 2:', part2_result)  # remove
    assert part2_result == 0, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
