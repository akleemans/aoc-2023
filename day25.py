import random
from typing import List, Dict
from heapq import heappop, heappush

# Day 25: Snowverload

test_data = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''.split('\n')


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.self_references = {}

    def __str__(self):
        neighbor_names = '-'.join(n.name for n in self.neighbors)
        return f'{self.name} ({neighbor_names})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.name.__hash__()

    def __ne__(self, other):
        return self.name != other.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        """Used for comparing in PriorityQueue"""
        return self.name < other.name


def edge_hash(n0, n1):
    """Return edge hash"""
    if n0.name < n1.name:
        return n0.name + '-' + n1.name
    return n1.name + '-' + n0.name


def parse_input(data):
    node_dict = {}
    # Create nodes
    for line in data:
        source, targets = line.split(': ')
        for name in [source, *targets.split(' ')]:
            if name not in node_dict:
                node_dict[name] = Node(name)
    # Link
    for line in data:
        source, targets = line.split(': ')
        for name in targets.split(' '):
            node_dict[source].neighbors.append(node_dict[name])
            node_dict[name].neighbors.append(node_dict[source])
    return node_dict


def find_groups(nodes: Dict, cuts: List[str]):
    """Returns list of connected subgraphs given a list of cuts (node-node tuple)"""
    groups = []
    for node_name in nodes:
        visited = set()
        node = nodes[node_name]
        new_node = True
        for group in groups:
            if node in group:
                new_node = False
                break
        if not new_node:
            continue
        to_visit = [node]
        visited.add(node)
        while len(to_visit) > 0:
            current_node = to_visit.pop()
            for neighbor in current_node.neighbors:
                if edge_hash(current_node, neighbor) in cuts:
                    continue
                if neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.add(neighbor)
        if len(visited) > 0:
            groups.append(visited)
    return groups


def dijkstra(a, b, cuts):
    """BFS to find path from a to b, ignoring edges in 'cuts'"""
    queue = []
    visited_nodes = set()
    heappush(queue, (0, [a]))

    while len(queue) > 0:
        _, path = heappop(queue)
        last_node = path[-1]
        if last_node.name in visited_nodes:
            continue
        visited_nodes.add(last_node.name)
        if last_node == b:
            return path
        for neighbor in last_node.neighbors:
            if edge_hash(last_node, neighbor) not in cuts:
                new_path = [*path, neighbor]
                heappush(queue, (len(new_path), new_path))


def part1(data: List[str]):
    nodes = parse_input(data)
    groups = []
    while True:
        # Pick 2 random points and delete paths between them, 3 times
        # If we were lucky and picked two points from separate parts of the graph the 3 critical edges should be removed
        a = random.choice(list(nodes.values()))
        b = random.choice(list(nodes.values()))
        cuts = []
        for _ in range(3):
            path = dijkstra(a, b, cuts)
            for i in range(len(path) - 1):
                cuts.append(edge_hash(path[i], path[i + 1]))
        groups = find_groups(nodes, cuts)
        if len(groups) == 2:
            break

    return len(groups[0]) * len(groups[1])


def main():
    with open('inputs/day25.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 54, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 614655, f'Part 1 returned {part1_result}'


if __name__ == '__main__':
    main()
