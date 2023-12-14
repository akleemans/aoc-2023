from typing import List

# Day 14: Parabolic Reflector Dish

test_data = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.split('\n')


def move_rocks(grid, d='U'):
    grid = [list(line) for line in grid]
    movement = True
    while movement:
        movement = False
        if d == 'U':
            for i in range(len(grid) - 1, 0, -1):
                for j in range(len(grid[i])):
                    if grid[i][j] == 'O' and grid[i - 1][j] == '.':
                        grid[i][j] = '.'
                        grid[i - 1][j] = 'O'
                        movement = True
        elif d == 'D':
            for i in range(0, len(grid) - 1):
                for j in range(len(grid[i])):
                    if grid[i][j] == 'O' and grid[i + 1][j] == '.':
                        grid[i][j] = '.'
                        grid[i + 1][j] = 'O'
                        movement = True
        elif d == 'L':
            for line in grid:
                for j in range(len(line) - 1, 0, -1):
                    if line[j] == 'O' and line[j - 1] == '.':
                        line[j] = '.'
                        line[j - 1] = 'O'
                        movement = True
        elif d == 'R':
            for line in grid:
                for j in range(0, len(line) - 1):
                    if line[j] == 'O' and line[j + 1] == '.':
                        line[j] = '.'
                        line[j + 1] = 'O'
                        movement = True
    return grid


def count_sum(grid):
    load_sum = 0
    for i, line in enumerate(grid[::-1]):
        load_sum += (i + 1) * line.count('O')
    return load_sum


def part1(data: List[str]):
    grid = move_rocks(data)
    return count_sum(grid)


def part2(data: List[str]):
    grid = [list(line) for line in data]
    i = 0
    states = []
    counts = []
    while True:
        for d in ['U', 'L', 'D', 'R']:
            grid = move_rocks(grid, d=d)
        count = count_sum(grid)
        counts.append(count)
        state = ''.join([''.join(line) for line in grid])
        states.append(state)
        if state in states[:-1]:
            break
        i += 1

    offset = states.index(states[-1])
    cycle_length = i - offset
    count_cycles = counts[offset:-1]
    idx = (10 ** 9 - 1 - offset) % cycle_length
    return count_cycles[idx]


def main():
    with open('inputs/day14.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 136, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 106186, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 64, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 106390, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
