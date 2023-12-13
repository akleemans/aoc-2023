from functools import cache
from typing import List, Tuple

# Day 12: Hot Springs

test_data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')


@cache
def place_next(state: str, groups: Tuple) -> int:
    # Try to place group
    to_place = groups[0]
    groups = groups[1:]
    if all(c in ['?', '#'] for c in state[:to_place]) and (
            to_place == len(state) or state[to_place] != '#'):
        new_idx = to_place + 1

        # If all groups placed and no more # left, count solution
        if len(groups) == 0:
            if state[new_idx:].count('#') == 0:
                return 1
        else:
            count_sum = 0
            min_rem = sum(groups) + len(groups) - 1
            for j in range(new_idx, len(state) - min_rem + 1):
                count_sum += place_next(state[j:], groups)
                # Can't move past a given spring
                if state[j] == '#':
                    break
            return count_sum
    return 0


def solve(data: List[str]):
    total_sum = 0
    for line_nr in range(len(data)):
        initial_state, group_str = data[line_nr].split(' ')
        all_groups = [int(n) for n in group_str.split(',')]
        min_remaining = sum(all_groups) + len(all_groups) - 1
        for i in range(0, len(initial_state) - min_remaining + 1):
            total_sum += place_next(initial_state[i:], tuple(all_groups))
            if initial_state[i] == '#':
                break
    return total_sum


def part1(data: List[str]):
    return solve(data)


def part2(data: List[str]):
    unfolded = []
    for line in data:
        state, group_str = line.split(' ')
        unfolded.append('?'.join([state] * 5) + ' ' + ','.join([group_str] * 5))
    return solve(unfolded)


def main():
    with open('inputs/day12.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_first_line = part1(['?###???????? 3,2,1'])
    assert part1_test_first_line == 10, f'Part 1 test input, first line returned {part1_test_first_line}'
    part1_test_result = part1(test_data)
    assert part1_test_result == 21, f'Part 1 test input returned {part1_test_result}'
    another_test = part1(['.##.?#??.#.?# 2,1,1,1'])
    assert another_test == 1, f'Part 1, another test returned {another_test}'
    part1_result = part1(data)
    assert part1_result == 7204, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 525152, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 1672318386674, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
