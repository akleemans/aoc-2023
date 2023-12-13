from typing import List

# Day 13: Point of Incidence

test_data = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''.split('\n')


def summarize_note(grid, ignore_value=-1) -> int:
    # Check horizontal mirrors
    for i in range(len(grid) - 1):
        mirror_found = True
        a, b = i, i + 1
        while mirror_found:
            if a < 0 or b == len(grid):
                break
            if grid[a] != grid[b]:
                mirror_found = False
            a, b = a - 1, b + 1
        value = (i + 1) * 100
        if mirror_found and value != ignore_value:
            return value

    # Check vertical mirrors
    for i in range(len(grid[0]) - 1):
        mirror_found = True
        a, b = i, i + 1
        while mirror_found:
            if a < 0 or b == len(grid[0]):
                break
            col_a = ''.join(line[a] for line in grid)
            col_b = ''.join(line[b] for line in grid)
            if col_a != col_b:
                mirror_found = False
            a, b = a - 1, b + 1
        value = i + 1
        if mirror_found and value != ignore_value:
            return value
    return 0


def get_grids(data):
    grids = []
    current_grid = []
    for i, line in enumerate(data):
        if len(line) == 0 or i == len(data) - 1:
            grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append(line)
    return grids


def part1(data: List[str]):
    total_sum = 0
    for grid in get_grids(data):
        total_sum += summarize_note(grid)
    return total_sum


def part2(data: List[str]):
    total_sum = 0
    for grid in get_grids(data):
        original_s = summarize_note(grid)
        s = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid_copy = [list(line) for line in grid]
                grid_copy[i][j] = '#' if grid_copy[i][j] == '.' else '.'
                s = summarize_note(grid_copy, original_s)
                if s not in [0, original_s]:
                    total_sum += s
                    break
            if s not in [0, original_s]:
                break

    return total_sum


def main():
    with open('inputs/day13.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 405, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 35521, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 400, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 34795, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
