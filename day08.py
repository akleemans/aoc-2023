import math
from typing import List, Dict

# Day 8: Haunted Wasteland

test_data = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split('\n')

test_data2 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split('\n')


class Node:
    name: str
    neighbors: Dict[str, 'Node']

    def __init__(self, name):
        self.name = name

    def move(self, d: str):
        return self.neighbors[d]

    def __repr__(self):
        return self.name


def parse_input(data):
    instr = data[0]
    nodes_dict = {line.split()[0]: Node(line.split()[0]) for line in data[2:]}
    for line in data[2:]:
        name = line.split()[0]
        l_name = line.split()[2].replace('(', '').replace(',', '')
        l = next(n for n in nodes_dict.values() if n.name == l_name)
        r_name = line.split()[3].replace(')', '')
        r = next(n for n in nodes_dict.values() if n.name == r_name)
        current_node = next(n for n in nodes_dict.values() if n.name == name)
        current_node.neighbors = {'L': l, 'R': r}
    return instr, nodes_dict.values()


def part1(data: List[str]):
    instr, nodes = parse_input(data)
    current_node = next(n for n in nodes if n.name == 'AAA')
    move_count = 0
    while current_node.name != 'ZZZ':
        d = instr[move_count % len(instr)]
        current_node = current_node.move(d)
        move_count += 1
    return move_count


def part2(data: List[str]):
    instr, nodes = parse_input(data)
    current_nodes = [n for n in nodes if n.name.endswith('A')]
    cycles = []
    for node in current_nodes:
        move_count = 0
        while not node.name.endswith('Z'):
            d = instr[move_count % len(instr)]
            node = node.move(d)
            move_count += 1
        cycles.append(move_count)
    return math.lcm(*cycles)


def main():
    with open('inputs/day08.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 6, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 19951, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data2)
    assert part2_test_result == 6, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 16342438708751, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
