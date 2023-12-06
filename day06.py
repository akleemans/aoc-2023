from typing import List

# Day 6: Wait For It

test_data = '''Time:      7  15   30
Distance:  9  40  200'''.split('\n')


def part1(data: List[str]):
    times = [int(t) for t in data[0].split()[1:]]
    distances = [int(d) for d in data[1].split()[1:]]
    total_ways = 1
    for t, d in zip(times, distances):
        total_ways *= sum([1 for i in range(1, t) if i * (t - i) > d])
    return total_ways


def part2(data: List[str]):
    times = [int(t) for t in data[0].replace(' ', '').split(':')[1:]]
    distances = [int(d) for d in data[1].replace(' ', '').split(':')[1:]]
    total_ways = 1
    for t, d in zip(times, distances):
        total_ways *= sum([1 for i in range(1, t) if i * (t - i) > d])
    return total_ways


def main():
    with open('inputs/day06.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 288, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 1083852, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 71503, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 23501589, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
