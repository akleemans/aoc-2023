from typing import List

# Day 1: Trebuchet?!

test_data = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
4hmfzdzf'''.split('\n')

test_data2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.split('\n')


def part1(data: List[str]):
    count = 0
    for line in data:
        first = ''
        last = ''
        for i in range(len(line)):
            if first == '' and line[i].isdigit():
                first = line[i]
            if last == '' and line[-(i + 1)].isdigit():
                last = line[-(i + 1)]
            if len(first + last) == 2:
                # print('line:', line, '=>', first + last)
                count += int(first + last)
                break
    return count


def is_digit(line: str, pos: int) -> str:
    numerals = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                'nine': '9'}
    if line[pos].isdigit():
        return line[pos]

    for key in numerals:
        if line[pos:].startswith(key):
            return numerals[key]
    return ''


def part2(data: List[str]):
    count = 0
    for line in data:
        first = ''
        last = ''
        for i in range(len(line)):
            if first == '' and is_digit(line, i) != '':
                first = is_digit(line, i)
            if is_digit(line, i) != '':
                last = is_digit(line, i)
        count += int(first + last)
    return count


def main():
    with open('inputs/day01.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 142 + 44, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 52974, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data2)
    assert part2_test_result == 281, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 53340, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
