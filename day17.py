from typing import List, Tuple

# Day 17: Clumsy Crucible

test_data0 = '''19211
11191
99191
99911'''.split('\n')

test_data = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split('\n')

dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
dir_turn = {'R': 'DU', 'L': 'DU', 'U': 'RL', 'D': 'RL'}


def add(a, b) -> Tuple[int, int]:
    """Add two coordinates"""
    return a[0] + b[0], a[1] + b[1]


def in_bounds(row: int, col: int, data: List[str]):
    return 0 <= row < len(data) and 0 <= col < len(data[0])


def part1(data: List[str]):
    heat_losses = [[[10 ** 6] * 3 for _ in data[0]] for _ in data]
    queue = [(0, 0, 0, 'R'), (0, 0, 0, 'D')]
    count = 0
    while len(queue) > 0:
        if count % 10 ** 6 == 0:
            print("count:", count, len(queue))
        count += 1
        row, col, last_value, path = queue.pop(0)
        if min(heat_losses[-1][-1]) < last_value:
            continue
        direction = path[-1]
        straights_left = 2
        for i in range(2, 5):
            if len(path) < i or path[-i] != direction:
                break
            straights_left -= 1
        add_coord = dir_map[direction]
        new_row, new_col = add((row, col), add_coord)
        if not in_bounds(new_row, new_col, data):
            continue
        next_value = last_value + int(data[new_row][new_col])
        # Update value
        if heat_losses[new_row][new_col][straights_left] < next_value:
            continue

        for i in range(straights_left, -1, -1):
            heat_losses[new_row][new_col][i] = min(next_value, heat_losses[new_row][new_col][i])
        # If bottom right reached, stop search
        if new_row == len(data) - 1 and new_col == len(data[0]) - 1:
            continue

        new_nodes = []
        # Turn
        for d in dir_turn[direction]:
            new_nodes.append((new_row, new_col, next_value, path + d))
        # If not yet 3 times straight, go
        if path[-3:] != direction * 3:
            new_nodes.append((new_row, new_col, next_value, path + direction))
        # Simple heuristic: visit nodes closer to goal first
        new_nodes.sort(key=lambda x: x[0] + x[1], reverse=True)
        # queue.extend(new_nodes)
        queue = [*new_nodes, *queue]

    return min(heat_losses[-1][-1])


def part2(data: List[str]):
    return 1


def main():
    with open('inputs/day17.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test0_result = part1(test_data0)
    print('Test input:', part1_test0_result)
    assert part1_test0_result == 10, f'Part 1 test input returned {part1_test0_result}'

    part1_test_result = part1(test_data)
    print('Test input:', part1_test_result)
    assert part1_test_result == 102, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    print('Part 1:', part1_result)  # remove
    assert part1_result == 0, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 0, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    print('Part 2:', part2_result)  # remove
    assert part2_result == 0, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
