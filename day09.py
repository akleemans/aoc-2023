from typing import List

# Day 9: Mirage Maintenance

test_data = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split('\n')


def solve(data, backwards=False):
    total_sum = 0
    for line in data:
        numbers = [int(x) for x in line.split()]
        current_nr = 0
        mult = 1
        while not all(n == 0 for n in numbers):
            current_nr += mult * numbers[0 if backwards else -1]
            mult *= -1 if backwards else 1
            numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        total_sum += current_nr
    return total_sum


def part1(data: List[str]):
    return solve(data)


def part2(data: List[str]):
    return solve(data, backwards=True)


def main():
    with open('inputs/day09.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 114, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 1974913025, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 2, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 884, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
