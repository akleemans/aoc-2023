from typing import List

# Day 4: Scratchcards

test_data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')


def part1(data: List[str]):
    card_sum = 0
    for card in data:
        card = card.split(':')[1].replace('  ', ' ').strip()
        winning, own = card.split(' | ')
        matches = sum([1 for n in own.split(' ') if n in winning.split(' ')])
        card_sum += int(2 ** (matches - 1))
    return card_sum


def part2(data: List[str]):
    card_pile = [[line, 1] for line in data]
    for i in range(len(card_pile)):
        card, count = card_pile[i]
        card = card.split(':')[1].replace('  ', ' ').strip()
        winning, own = card.split(' | ')
        matches = sum([1 for n in own.split(' ') if n in winning.split(' ')])
        for j in range(1, matches + 1):
            card_pile[i + j][1] += count
        i += 1
    return sum(x[1] for x in card_pile)


def main():
    with open('inputs/day04.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 13, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 21158, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 30, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 6050769, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
