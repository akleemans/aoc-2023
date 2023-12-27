from typing import List, Tuple

from utils import dir_map, add, subtract

# Day 18: Lavaduct Lagoon

test_data = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.split('\n')


def area_shoelace(coords: List[Tuple[int, int]]):
    """Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    Inspired by https://stackoverflow.com/a/717367/811708"""
    area = 0
    for i in range(1, len(coords) - 1):
        area += coords[i][0] * (coords[i + 1][1] - coords[i - 1][1])
    area = abs(area / 2)

    # Because we're working with an integer grid, add side length / 2
    side_length = 0
    for i in range(len(coords) - 1):
        coord_diff = subtract(coords[i], coords[i + 1])
        side = max(abs(c) for c in coord_diff)
        side_length += side
    total_area = area + side_length / 2 + 1
    return int(total_area)


def part1(data: List[str]):
    coords = [(0, 0)]
    for line in data:
        d, amount, color = line.split()
        add_coords = tuple(int(amount) * x for x in dir_map[d])
        coords.append(add(coords[-1], add_coords))
    return area_shoelace(coords)


def part2(data: List[str]):
    coords = [(0, 0)]
    dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    for line in data:
        _, _, color = line.split()
        color = color[2:-1]
        d = dirs[color[-1]]
        amount = int('0x' + color[:-1], 16)
        add_coords = tuple(int(amount) * x for x in dir_map[d])
        coords.append(add(coords[-1], add_coords))
    return area_shoelace(coords)


def main():
    with open('inputs/day18.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 62, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 49578, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 952408144115, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 52885384955882, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
