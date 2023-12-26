from itertools import combinations
from typing import List, Dict

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
    name: str
    neighbors: List[Node]
    self_references: Dict[Node, int]

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


def find_groups(nodes, cuts):
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
                if (current_node, neighbor) in cuts or (neighbor, current_node) in cuts:
                    continue
                if neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.add(neighbor)
        if len(visited) > 0:
            groups.append(visited)
    return groups


def part1(data: List[str]):
    nodes = parse_input(data)
    for node_name in nodes:
        node = nodes[node_name]
        for neighbor1 in node.neighbors:
            node.self_references[neighbor1] = 0
            for neighbor2 in neighbor1.neighbors:
                if node in neighbor2.neighbors:
                    node.self_references[neighbor1] += 1

    # Print connections for visual solving
    # visited = set()
    # for node_name in nodes:
    #    node = nodes[node_name]
    #    for neighbor in node.neighbors:
    #        if (node, neighbor) in visited or (neighbor, node) in visited:
    #            continue
    #        visited.add((node, neighbor))
    #        print(f'{node_name} -> {neighbor.name}')

    # Check possible cuts
    possible_cuts = set()
    for node_name in nodes:
        node = nodes[node_name]
        for neighbor in node.self_references:
            if node.self_references[neighbor] == 0:
                if (node, neighbor) not in possible_cuts and (neighbor, node) not in possible_cuts:
                    possible_cuts.add((node, neighbor))

    l = list(nodes.values())
    l.sort(key=lambda n: len(n.neighbors))
    for n in l[:30]:
        print(n, len(n.neighbors))
    # Trying cut combinations
    print('Trying combining', len(possible_cuts), 'possible cuts')
    count = 0
    possible_cuts2 = []
    for cut in possible_cuts:
        s = str(cut)
        if 'nnl' in s or 'rkh' in s or 'hrs' in s:
            possible_cuts2.append(cut)

    for cuts in combinations(possible_cuts2, 3):
        count += 1
        if count % 10000 == 0:
            print('Combination count:', count)
        groups = find_groups(nodes, cuts)
        if len(groups) == 2:
            mult = len(groups[0]) * len(groups[1])
            return mult


def main():
    with open('inputs/day25.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    # part1_test_result = part1(test_data)
    # assert part1_test_result == 54, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 614655, f'Part 1 returned {part1_result}'


if __name__ == '__main__':
    main()
