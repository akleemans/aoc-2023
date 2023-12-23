from typing import List, Tuple

# Day 23: A Long Walk

test_data = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''.split('\n')

dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
valid_dir_tiles = {'R': '.>', 'L': '.<', 'U': '.^', 'D': '.v'}


def end_pos(grid):
    return len(grid) - 1, len(grid[0]) - 2


def add(a, b) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def walk(grid, pos, next_dir, length, slopes_walkable) -> int:
    possible_dirs = [next_dir]
    while len(possible_dirs) == 1:
        # First, do next step
        next_dir = possible_dirs.pop()
        pos = add(pos, dir_map[next_dir])
        row, col = pos
        length += 1
        grid[row][col] = 'O'
        if pos == end_pos(grid):
            # if length >= 6430:
            #    print('New length found:', length)
            return length

        # Find next possible directions
        for d in 'ULDR':
            new_row, new_col = add((row, col), dir_map[d])
            valid_tiles = '.^>v<' if slopes_walkable else valid_dir_tiles[d]
            if grid[new_row][new_col] in valid_tiles:
                possible_dirs.append(d)

    if len(possible_dirs) == 0:
        return 0
    else:
        results = []
        for d in possible_dirs:
            results.append(walk([line[:] for line in grid], pos, d, length, slopes_walkable))
        return max(results)


def part1(data: List[str]):
    start = (-1, 1)
    grid = [list(line) for line in data]
    return walk(grid, start, 'D', -1, False)


def part2(data: List[str]):
    start = (-1, 1)
    grid = [list(line) for line in data]
    return walk(grid, start, 'D', -1, True)


def main():
    with open('inputs/day23.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 94, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 2430, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 154, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 6534, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
