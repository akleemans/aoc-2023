from itertools import combinations
from typing import List, Tuple
from sympy import solve
from sympy.abc import a, b, c, d, e, f, t, u, v

# Day 24: Never Tell Me The Odds

test_data = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''.split('\n')


def intersect_2d(x0a, y0a, dxa, dya, x0b, y0b, dxb, dyb) -> Tuple[int, int, int, int]:
    """Modified from https://stackoverflow.com/a/41798064/811708"""
    d = (dxa * dyb - dxb * dya)
    if d == 0.0:
        # No intersection
        return -1, -1, -1, -1
    ta = (dyb * (x0b - x0a) - dxb * (y0b - y0a)) / d
    tb = (dya * (x0b - x0a) - dxa * (y0b - y0a)) / d
    # ta and tb are where the collisions happen from viewpoint of a and b
    return ta, tb, x0a + dxa * ta, y0a + dya * ta


def parse_input(data):
    hailstones = []
    for line in data:
        p, d = line.split(' @ ')
        x, y, z = [int(n) for n in p.split(', ')]
        dx, dy, dz = [int(n) for n in d.split(', ')]
        hailstones.append(((x, y, z), (dx, dy, dz)))
    return hailstones


def part1(data: List[str], xy_min, xy_max):
    hailstones = parse_input(data)
    in_test_area = 0
    for a, b in combinations(hailstones, 2):
        if a == b:
            continue
        pa, da = a
        pb, db = b
        ta, tb, ix, iy = intersect_2d(pa[0], pa[1], da[0], da[1], pb[0], pb[1], db[0], db[1])
        if ta >= 0.0 and tb >= 0.0 and xy_min <= ix <= xy_max and xy_min <= iy <= xy_max:
            in_test_area += 1

    return in_test_area


def part2(data: List[str]):
    """Create equations based on the first three hailstone trajectories.
    We don't know the starting position (3 unknowns) nor the velocity (3 unknowns)
    but at timesteps t/u/v they have to match hailstones 0/1/2."""
    hailstones = parse_input(data)
    h0, h1, h2 = hailstones[:3]
    # (a, b, c): position of rock
    # (d, e, f): velocity of rock
    # t, u, v: time parameters
    solutions = solve([
        a + t * d - h0[0][0] - t * h0[1][0],
        b + t * e - h0[0][1] - t * h0[1][1],
        c + t * f - h0[0][2] - t * h0[1][2],
        a + u * d - h1[0][0] - u * h1[1][0],
        b + u * e - h1[0][1] - u * h1[1][1],
        c + u * f - h1[0][2] - u * h1[1][2],
        a + v * d - h2[0][0] - v * h2[1][0],
        b + v * e - h2[0][1] - v * h2[1][1],
        c + v * f - h2[0][2] - v * h2[1][2],
    ], a, b, c, d, e, f, t, u, v)
    solution = solutions[0]
    pos_sum = solution[0] + solution[1] + solution[2]

    return pos_sum


def main():
    with open('inputs/day24.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 7, 27)
    assert part1_test_result == 2, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data, 2 * 10 ** 14, 4 * 10 ** 14)
    assert part1_result == 18098, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 47, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 886858737029295, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
