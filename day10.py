from typing import List, Tuple

from utils import add

# Day 10: Pipe Maze

test_data = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''.split('\n')

test_data2 = '''..........
.S------7.
.|F----7|.
.||.-F.||.
.||77..||.
.|L-7F-J|.
.|-.||J.|.
.L--JL--J.
..........'''.split('\n')

test_data3 = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''.split('\n')

reverses = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
dir_pairs = {'F': 'DR', '7': 'DL', 'J': 'LU', 'L': 'RU', '|': 'UD', '-': 'LR'}
directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
neighbor_coord_diffs = [(-1, 0, 'L'), (1, 0, 'R'), (0, -1, 'U'), (0, 1, 'D')]


def get_coord(data, coord, oob_char='.'):
    """Get character at coord. Handles out-of-bounds by returning oob_char"""
    x, y = coord
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return oob_char
    return data[y][x]


def find_start(data: List[str]) -> Tuple[int, int]:
    """Find coordinates of starting point"""
    for i, line in enumerate(data):
        if 'S' in line:
            return line.index('S'), i


def find_loop(data: List[str]):
    """Find complete loop and return coordinates & directions"""
    start = find_start(data)
    loop_coords = []
    loop_dirs = []
    for d in neighbor_coord_diffs:
        current_coord = add(start, d)
        current_dir = d[2]
        loop_coords = [current_coord]
        loop_dirs = [current_dir]
        while True:
            if get_coord(data, current_coord) == '.':
                break
            if current_coord == start:
                break
            current_symbol = get_coord(data, current_coord)
            dir_pair = dir_pairs[current_symbol]
            next_dir = dir_pair.replace(reverses[current_dir], '')
            current_coord = add(current_coord, directions[next_dir])
            loop_coords.append(current_coord)
            current_dir = next_dir
            loop_dirs.append(current_dir)
        if current_coord == start:
            break
    return loop_coords, loop_dirs


def part1(data: List[str]):
    loop_coords, loop_dirs = find_loop(data)
    return len(loop_coords) // 2


def print_grid(grid: List[List[str]]) -> None:
    """Print grid for debugging"""
    for line in grid:
        print(''.join(line))


def flood_fill(new_grid, queue: List[Tuple[int, int]]):
    while len(queue) > 0:
        c = queue.pop()
        if get_coord(new_grid, c, '?') == '.':
            for d in neighbor_coord_diffs:
                queue.append(add(c, d))
            new_grid[c[1]][c[0]] = 'I'


# Relative direction change. 1: clockwise, -1: counter-clockwise
rel_dir_change = {'UL': -1, 'UR': 1, 'RU': -1, 'RD': 1, 'DL': -1, 'DR': 1, 'LD': -1, 'LU': 1}


def part2(data: List[str]):
    loop_coords, loop_dirs = find_loop(data)
    loop_direction_sum = sum(rel_dir_change.get(a + b, 0) for a, b in zip(loop_dirs, loop_dirs[1:]))
    loop_direction = 'R' if loop_direction_sum > 0 else 'L'

    # Indicate what is "inside" the grid based on symbol and loop direction (L=clockwise or R=cc)
    right_loop_inside = {'UF': [], 'LF': [(-1, 0), (0, -1)], 'R7': [], 'U7': [(1, 0), (0, -1)],
                         'RJ': [(1, 0), (0, 1)], 'DJ': [], 'DL': [(-1, 0), (0, 1)], 'LL': [],
                         'D|': [(-1, 0)], 'U|': [(1, 0)], 'R-': [(0, 1)], 'L-': [(0, -1)]}
    left_loop_inside = {'UF': [(-1, 0), (0, -1)], 'LF': [], 'R7': [(1, 0), (0, -1)], 'U7': [],
                        'RJ': [], 'DJ': [(1, 0), (0, 1)], 'DL': [], 'LL': [(-1, 0), (0, 1)],
                        'D|': [(1, 0)], 'U|': [(-1, 0)], 'R-': [(0, -1)], 'L-': [(0, 1)]}
    inside_grid = right_loop_inside if loop_direction == 'R' else left_loop_inside

    # Create empty grid with only loop drawn
    new_grid = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
    for i, coord in enumerate(loop_coords):
        x, y = coord
        new_grid[y][x] = 'x'
        current_dir = loop_dirs[i]
        for coord_diff in inside_grid.get(current_dir + data[y][x], []):
            c = add(coord, coord_diff)
            if get_coord(new_grid, c) == '.':
                new_grid[c[1]][c[0]] = 'I'

    # Flood fill from Is
    for y in range(len(data)):
        for x in range(len(data[0])):
            if new_grid[y][x] == 'I':
                queue = [add((x, y), d) for d in neighbor_coord_diffs]
                flood_fill(new_grid, queue)

    # print_grid(new_grid)
    return sum(sum([1 for c in line if c == 'I']) for line in new_grid)


def main():
    with open('inputs/day10.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 8, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 7005, f'Part 1 returned {part1_result}'

    part2_test1_result = part2(test_data2)
    assert part2_test1_result == 4, f'Part 2 test input 1 returned {part2_test1_result}'
    part2_test2_result = part2(test_data3)
    assert part2_test2_result == 10, f'Part 2 test input 2 returned {part2_test2_result}'

    part2_result = part2(data)
    assert part2_result == 417, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
