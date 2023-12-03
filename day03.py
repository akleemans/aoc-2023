from typing import List, Optional, Tuple

# Day 3: Gear Ratios

test_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')


def get_coord(data, coord):
    x, y = coord
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return '.'
    return data[y][x]


def get_neighbors(data, coord):
    neighbors = []
    x, y = coord
    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            if a == b == 0:
                continue
            neighbors.append(get_coord(data, (x + b, y + a)))
    return neighbors


def part1(data: List[str]):
    symbols = {'&', '-', '@', '+', '$', '%', '/', '#', '*', '='}
    x, y, nr_sum = 0, 0, 0
    while y < len(data):
        x = 0
        while x < len(data[0]):
            nr_coords = []
            while x < len(data[0]) and data[y][x].isdigit():
                nr_coords.append((x, y))
                x += 1
            if len(nr_coords) > 0:
                neighbors = []
                for coord in nr_coords:
                    neighbors.extend(get_neighbors(data, coord))
                if len(set(neighbors).intersection(symbols)) > 0:
                    nr_sum += int(''.join([data[y][x] for (x, y) in nr_coords]))
            x += 1
        y += 1
    return nr_sum


def is_bound_to_gear(data, coords) -> Optional[Tuple[int, int]]:
    for coord in coords:
        x, y = coord
        for a in range(-1, 2, 1):
            for b in range(-1, 2, 1):
                candidate = (x + b, y + a)
                if get_coord(data, candidate) == '*':
                    return candidate
    return None


def part2(data: List[str]):
    x, y = 0, 0
    gear_numbers = []
    while y < len(data):
        x = 0
        while x < len(data[0]):
            nr_coords = []
            while x < len(data[0]) and data[y][x].isdigit():
                nr_coords.append((x, y))
                x += 1
            if len(nr_coords) > 0:
                bound_to_gear = is_bound_to_gear(data, nr_coords)
                if bound_to_gear is not None:
                    nr = int(''.join([data[y][x] for (x, y) in nr_coords]))
                    gear_numbers.append((bound_to_gear, nr))
            x += 1
        y += 1

    gear_ratio_sum = 0
    gear_numbers = sorted(gear_numbers, key=lambda x: x[0])
    for i in range(len(gear_numbers) - 1):
        # Count if bound to same gear
        if gear_numbers[i][0] == gear_numbers[i + 1][0]:
            gear_ratio_sum += gear_numbers[i][1] * gear_numbers[i + 1][1]

    return gear_ratio_sum


def main():
    with open('inputs/day03.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 4361, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 551094, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 467835, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 80179647, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
