from typing import List, Dict, Tuple, Set

from utils import dir_map, add, in_bounds

# Day 23: A Long Walk

test_data = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''.split('\n')

valid_dir_tiles = {'R': '.>', 'L': '.<', 'U': '.^', 'D': '.v'}


def end_pos(grid):
    return len(grid) - 1, len(grid[0]) - 2


def walk(grid, pos, next_dir, length, slopes_walkable) -> int:
    possible_dirs = [next_dir]
    while len(possible_dirs) == 1:
        # First, do next step
        next_dir = possible_dirs.pop()
        pos = add(pos, dir_map[next_dir])
        row, col = pos
        length += 1
        grid[row][col] = 'O'
        if pos == end_pos(grid):
            return length

        # Find next possible directions
        for d in 'ULDR':
            new_row, new_col = add((row, col), dir_map[d])
            valid_tiles = '.^>v<' if slopes_walkable else valid_dir_tiles[d]
            if grid[new_row][new_col] in valid_tiles:
                possible_dirs.append(d)

    if len(possible_dirs) == 0:
        return 0
    else:
        results = []
        for d in possible_dirs:
            results.append(walk([line[:] for line in grid], pos, d, length, slopes_walkable))
        return max(results)


def part1(data: List[str]):
    start = (-1, 1)
    grid = [list(line) for line in data]
    return walk(grid, start, 'D', -1, False)


def part2(data: List[str]):
    # Build simplified graph
    nodes: Dict[Tuple[int, int], List[Tuple[Tuple[int, int], int]]] = {}
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] != '#':
                neighbors = []
                for d in 'ULDR':
                    new_row, new_col = add((row, col), dir_map[d])
                    if in_bounds(new_row, new_col, data) and data[new_row][new_col] != '#':
                        neighbors.append(((new_row, new_col), 1))
                nodes[(row, col)] = neighbors

    # Contract nodes
    changed = True
    while changed:
        changed = False
        for node_name in nodes:
            neighbors = nodes[node_name]
            if len(neighbors) == 2:
                nodes.pop(node_name)
                n0, n1 = neighbors
                dist = n0[1] + n1[1]
                # Wire neighbors together
                nodes[n0[0]] = [n for n in nodes[n0[0]] if n[0] != node_name] + [(n1[0], dist)]
                nodes[n1[0]] = [n for n in nodes[n1[0]] if n[0] != node_name] + [(n0[0], dist)]
                changed = True
                break

    # DFS
    start_node = (0, 1)
    end_node = (len(data) - 1, len(data[0]) - 2)

    def walk2(node_name: Tuple[int, int], visited: Set[Tuple[int, int]], length: int) -> int:
        if node_name == end_node:
            return length
        visited.add(node_name)
        next_nodes = [-1]
        for neighbor, dist in nodes[node_name]:
            if neighbor not in visited:
                next_nodes.append(walk2(neighbor, visited.copy(), length + dist))
        return max(next_nodes)

    return walk2(start_node, set(), 0)


def main():
    with open('inputs/day23.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 94, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 2430, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 154, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 6534, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
