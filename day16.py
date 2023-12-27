from typing import List

from utils import in_bounds, dir_map

# Day 16: The Floor Will Be Lava

test_data = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''.split('\n')

symbol_map = {
    '\\': {'R': ['D'], 'L': ['U'], 'U': ['L'], 'D': ['R']},
    '/': {'R': ['U'], 'L': ['D'], 'U': ['R'], 'D': ['L']},
    '|': {'R': ['D', 'U'], 'L': ['U', 'D'], 'U': ['U'], 'D': ['D']},
    '-': {'R': ['R'], 'L': ['L'], 'U': ['L', 'R'], 'D': ['R', 'L']},
    '.': {'R': ['R'], 'L': ['L'], 'U': ['U'], 'D': ['D']},
}


def solve(data, start_beam) -> int:
    coord_tracking = {}
    active_beams = [start_beam]
    while len(active_beams):
        next_active_beams = []
        for beam in active_beams:
            row, col, d = beam
            coord_history = coord_tracking.get((row, col), [])
            if d in coord_history:
                continue
            else:
                coord_history.append(d)
                coord_tracking[(row, col)] = coord_history
            current_symbol = data[row][col]
            next_dirs = symbol_map[current_symbol][d]
            for next_dir in next_dirs:
                add_row, add_col = dir_map[next_dir]
                next_beam = (row + add_row, col + add_col, next_dir)
                if in_bounds(next_beam[0], next_beam[1], data):
                    next_active_beams.append(next_beam)
        active_beams = next_active_beams
    return len(coord_tracking)


def part1(data: List[str]):
    return solve(data, (0, 0, 'R'))


def part2(data: List[str]):
    max_energized = 0
    for row in range(len(data)):
        max_energized = max(max_energized, solve(data, (row, 0, 'R')))
        max_energized = max(max_energized, solve(data, (row, len(data[0]) - 1, 'L')))

    for col in range(len(data[0])):
        max_energized = max(max_energized, solve(data, (0, col, 'D')))
        max_energized = max(max_energized, solve(data, (len(data) - 1, col, 'U')))

    return max_energized


def main():
    with open('inputs/day16.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 46, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 7472, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 51, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 7716, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
