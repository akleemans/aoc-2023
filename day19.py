from typing import List

# Day 19: Aplenty

test_data = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''.split('\n')


def parse_input(data):
    workflows = {}
    parts = []
    at_workflows = True
    for line in data:
        if len(line) == 0:
            at_workflows = False
            continue
        if at_workflows:
            name = line.split('{')[0]
            rules = []
            for r in line.split('{')[1][:-1].split(','):
                if ':' in r:
                    condition, result = r.split(':')
                    if '<' in condition:
                        letter, value = condition.split('<')
                        sign = '<'
                    else:
                        letter, value = condition.split('>')
                        sign = '>'
                    rule = (letter, sign, int(value), result)
                else:
                    rule = r
                rules.append(rule)
            workflows[name] = Workflow(rules)
        else:
            part = {}
            for letter, value in zip('xmas', line[1:-1].split(',')):
                part[letter] = int(value.split('=')[1])
            parts.append(part)

    return workflows, parts


class Workflow:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, part):
        for i, rule in enumerate(self.rules):
            if i == len(self.rules) - 1:
                return rule
            letter, sign, value, result = rule
            if sign == '>' and part[letter] > value:
                return result
            elif sign == '<' and part[letter] < value:
                return result


def part1(data: List[str]):
    workflows, parts = parse_input(data)
    total_sum = 0
    for part in parts:
        result = 'in'
        while result not in 'AR':
            result = workflows[result].evaluate(part)
        if result == 'A':
            total_sum += sum(part.values())
    return total_sum


sign_reverse = {'>': '<=', '<': '>='}


def part2(data: List[str]):
    workflows, parts = parse_input(data)
    # Start with always true condition, starting at 'in'
    branches = [[('s', '>', 0, 'in')]]
    # Collect all the rules for branch
    unresolved = True
    while unresolved:
        unresolved = False
        for branch in branches:
            last_rule = branch[-1]
            if isinstance(last_rule, str):
                next_workflow = last_rule
            else:
                next_workflow = last_rule[-1]
            # If R or A, end of branch. Else add expanded branches and remove original
            if next_workflow in 'RA':
                continue
            unresolved = True
            branches.remove(branch)
            previous_rules = []
            # Add all rules of the next workflow like this:
            # [!a], [a, !b], [a, b, !c] etc.
            for r in workflows[next_workflow].rules:
                branches.append([*branch, *previous_rules, r])
                if not isinstance(r, str):
                    letter, sign, value, result = r
                    negated_r = (letter, sign_reverse[sign], value, result)
                    previous_rules.append(negated_r)

    # Check which branches end in accepted and count those
    all_possible_values = []
    for branch in branches:
        possible_values = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        for rule in branch:
            if isinstance(rule, str):
                continue
            letter, sign, value, result = rule
            if sign == '>':
                possible_values[letter][0] = max(possible_values[letter][0], value + 1)
            elif sign == '>=':
                possible_values[letter][0] = max(possible_values[letter][0], value)
            elif sign == '<':
                possible_values[letter][1] = min(possible_values[letter][1], value - 1)
            elif sign == '<=':
                possible_values[letter][1] = min(possible_values[letter][1], value)
        last_rule = branch[-1]
        if isinstance(last_rule, str) and last_rule == 'A' or last_rule[-1] == 'A':
            all_possible_values.append(possible_values)

    # Count total possibilities by multiplying ranges
    count_total = 0
    for possible_values in all_possible_values:
        count = 1
        for letter in possible_values:
            count *= possible_values[letter][1] - possible_values[letter][0] + 1
        count_total += count

    return count_total


def main():
    with open('inputs/day19.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 19114, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 367602, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 167409079868000, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 125317461667458, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
