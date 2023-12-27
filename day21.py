from typing import List

from utils import add, dir_map

# Day 21: Step Counter

test_data = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''.split('\n')


def part1(data: List[str], steps=64):
    start = (0, 0)
    h, w = len(data), len(data[0])
    for row in range(h):
        for col in range(w):
            if data[row][col] == 'S':
                start = (row, col)
                break
        if start[0] > 0:
            break

    queue = {start}
    for current_step in range(1, steps + 1):
        next_queue = set()
        for node in queue:
            for d in 'URDL':
                new_row, new_col = add(node, dir_map[d])
                if data[new_row % h][new_col % w] != '#':
                    next_queue.add((new_row, new_col))
        queue = next_queue
        # Find values for part 2
        # if (current_step - h // 2) % h == 0:
        #    print(current_step, '->', len(queue))

    return len(queue)


def quadratic_fit(x) -> int:
    """Based on quadratic fit with three data points f(n), f(n+X), f(n+2X)
    Wolfram link: https://www.wolframalpha.com/input?i=quadratic+fit+calculator
    65 -> 3832
    196 -> 33967
    327 -> 94056"""
    return int(3832 + 15158 * x + 14977 * x ** 2)


def part2(data: List[str]):
    """Solved with inspiration from Reddit.
    https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/"""
    m = len(data)
    offset = m // 2

    assert 3832 == quadratic_fit((65 - offset) / m)
    assert 33967 == quadratic_fit((196 - offset) / m)
    assert 94056 == quadratic_fit((327 - offset) / m)

    phase = int((26501365 - offset) / m)
    # print('phase:', phase)
    return quadratic_fit(phase)


def main():
    with open('inputs/day21.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 6)
    assert part1_test_result == 16, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 3649, f'Part 1 returned {part1_result}'

    # To get values [3832, 33967, 94056]
    # part1(data, 340)
    part2_result = part2(data)
    assert part2_result == 612941134797232, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
