from typing import List

# Day 12: Hot Springs

test_data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')


def solve(data: List[str]):
    total_place_calls = 0
    count_sums = []

    def place_next(state: str, groups: List[int], idx: int):
        nonlocal total_place_calls
        total_place_calls += 1
        # print('Trying', groups, 'starting at', idx)
        if idx > 0 and state[idx - 1] == '#':
            return

        # Sanity check: If less place left than stuff to place, it's impossible
        if (len(state) - idx) < (sum(groups) + len(groups) - 1):
            return

        # Try to place
        to_place = groups.pop(0)
        new_idx = 0
        if all(c in ['?', '#'] for c in state[idx:(idx + to_place)]) and (
                idx + to_place == len(state) or state[idx + to_place] != '#'):
            new_idx = idx + to_place + 1

        # If placing not possible, abort
        if new_idx == 0:
            return

        # If all groups placed and no more # left, count solution
        if len(groups) == 0:
            if state[new_idx:].count('#') == 0:
                count_sums[-1] += 1
            return

        # Else, continue search
        min_remaining = sum(groups) + len(groups) - 2 #  - min_remaining
        for i in range(new_idx, len(state)):
            place_next(state, [*groups], i)
            # Can't move past a given spring
            if state[i] == '#':
                break

    for line in data:
        # print('Working on line', line)
        state, group_str = line.split(' ')
        count_sums.append(0)
        for i in range(0, len(state)):
            place_next(state, [int(n) for n in group_str.split(',')], i)
            if state[i] == '#':
                break
    print('Total place calls:', total_place_calls)
    return sum(count_sums)


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
    print('Part 1 test input:', part1_test_result)
    assert part1_test_result == 21, f'Part 1 test input returned {part1_test_result}'
    another_test = part1(['.##.?#??.#.?# 2,1,1,1'])
    assert another_test == 1, f'Part 1, another test returned {another_test}'
    part1_result = part1(data)
    print('Part 1:', part1_result)
    assert part1_result == 7204, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    print('Part 2 test input:', part2_test_result)
    assert part2_test_result == 525152, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    print('Part 2:', part2_result)  # remove
    assert part2_result == 0, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
