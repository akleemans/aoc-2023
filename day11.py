import itertools
from typing import List

# Day 11: Cosmic Expansion

test_data = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.split('\n')


def solve(data, expansion):
    # Prepare distances
    dist_rows, dist_cols = {}, {}
    for i in range(len(data)):
        if all(c == '.' for c in data[i]):
            dist_rows[i] = expansion
        if all(data[j][i] == '.' for j in range(len(data))):
            dist_cols[i] = expansion

    # Collect galaxies
    galaxies = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[j][i] == '#':
                galaxies.append((i, j))

    # Calculate distances for all pairs
    def calculate_distance(a, b):
        dist = 0
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            dist += dist_cols.get(x, 1)
        for y in range(min(a[1], b[1]), max(a[1], b[1])):
            dist += dist_rows.get(y, 1)
        return dist

    total_sum = 0
    for a, b in itertools.combinations(galaxies, 2):
        total_sum += calculate_distance(a, b)
    return total_sum


def part1(data: List[str]):
    return solve(data, 2)


def part2(data: List[str]):
    return solve(data, 10 ** 6)


def main():
    with open('inputs/day11.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 374, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 9403026, f'Part 1 returned {part1_result}'

    part2_test_result = solve(test_data, 10)
    assert part2_test_result == 1030, f'Part 2 test input (10x) returned {part2_test_result}'
    part2_test_result = solve(test_data, 100)
    assert part2_test_result == 8410, f'Part 2 test input (100x) returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 543018317006, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
