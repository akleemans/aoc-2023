# Day 22: Sand Slabs

test_data = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''.split('\n')


def parse_input(data):
    bricks = []
    for line in data:
        current_brick = []
        a, b = line.split('~')
        ax, ay, az = [int(x) for x in a.split(',')]
        bx, by, bz = [int(x) for x in b.split(',')]
        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                for z in range(az, bz + 1):
                    current_brick.append((x, y, z))
        bricks.append(current_brick)
        bricks.sort(key=lambda brick: min(c[2] for c in brick))
    return bricks


def has_collision(new_brick, bricks, ignore_brick):
    for i, brick in enumerate(bricks):
        if i == ignore_brick:
            continue
        for coord in new_brick:
            if coord in brick:
                return True
    return False


def enable_gravity(original_bricks):
    bricks = [*original_bricks]
    change = True
    while change:
        change = False
        for i, brick in enumerate(bricks):
            if min(c[2] for c in brick) == 1:
                continue
            new_brick = [(c[0], c[1], c[2] - 1) for c in brick]
            if not has_collision(new_brick, bricks, i):
                bricks[i] = new_brick
                change = True
    return bricks


def part1(data):
    bricks = parse_input(data)
    bricks = enable_gravity(bricks)

    useless_bricks = 0
    for i, brick in enumerate(bricks):
        other_bricks = bricks[:i] + bricks[i + 1:]
        modified_bricks = enable_gravity(other_bricks)
        # If nothing happens, should be good to disintegrate
        if other_bricks == modified_bricks:
            useless_bricks += 1
    return useless_bricks


def part2(data):
    bricks = parse_input(data)
    bricks = enable_gravity(bricks)

    sum_of_fallen = 0
    for i, brick in enumerate(bricks):
        other_bricks = bricks[:i] + bricks[i + 1:]
        modified_bricks = enable_gravity(other_bricks)
        # If nothing happens, should be good to disintegrate
        for a, b in zip(other_bricks, modified_bricks):
            if a != b:
                sum_of_fallen += 1
    return sum_of_fallen


def main():
    with open('inputs/day22.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 5, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 409, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 7, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 61097, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
