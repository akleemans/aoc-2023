from typing import List

# Day 5: If You Give A Seed A Fertilizer

test_data = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.split('\n')


def parse_input(data):
    seeds = [int(s) for s in data[0].split(':')[1].strip().split(' ')]
    maps = []
    entries = []
    for line in data[2:]:
        if ':' in line:
            entries = []
            continue
        if len(line) == 0:
            maps.append(entries)
            continue
        a, b, c = [int(n) for n in line.strip().split(' ')]
        from_range = b
        to_range = b + c - 1
        subtract = b - a
        entries.append((from_range, to_range, subtract))
    maps.append(entries)
    return seeds, maps


def map_seed(entries, seed: int):
    for e in entries:
        if e[0] <= seed <= e[1]:
            return seed - e[2]
    return seed


def part1(data: List[str]):
    seeds, maps = parse_input(data)
    lowest_location = 10 ** 10
    for seed in seeds:
        for m in maps:
            seed = map_seed(m, seed)
        lowest_location = min(seed, lowest_location)
    return lowest_location


def part2(data: List[str]):
    seeds, maps = parse_input(data)
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    lowest_location = 10 ** 10
    for r in seed_ranges:
        for seed in range(r[0], r[1]):
            for m in maps:
                seed = map_seed(m, seed)
            lowest_location = min(seed, lowest_location)
    return lowest_location


def main():
    with open('inputs/day05.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 35, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 240320250, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 46, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 28580589, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
