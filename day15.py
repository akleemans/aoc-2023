from typing import List

# Day 15: Lens Library

test_data = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''.split('\n')


def get_hash(s: str):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def part1(data: List[str]):
    total_sum = 0
    for part in data[0].split(','):
        total_sum += get_hash(part)
    return total_sum


def part2(data: List[str]):
    boxes = [[] for _ in range(256)]
    for part in data[0].split(','):
        if '-' in part:
            lens = part.split('-')[0]
            idx = get_hash(lens)
            boxes[idx] = [b for b in boxes[idx] if b[0] != lens]
        elif '=' in part:
            lens, value = part.split('=')
            idx = get_hash(lens)
            value = int(value)
            replaced = False
            for i in range(len(boxes[idx])):
                if boxes[idx][i][0] == lens:
                    boxes[idx][i] = (lens, value)
                    replaced = True
            if not replaced:
                boxes[idx].append((lens, value))

    total_sum = 0
    for i, box in enumerate(boxes):
        for j, slot in enumerate(box):
            total_sum += (i + 1) * (j + 1) * slot[1]
    return total_sum


def main():
    with open('inputs/day15.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 1320, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 510273, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 145, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 212449, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
