from typing import List

# Day 2: Cube Conundrum

test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split('\n')


class Game:
    def __init__(self, id, grabs):
        self.id = id
        self.grabs = grabs


def parse_input(data):
    games = []
    color_map = {'red': 0, 'green': 1, 'blue': 2, }
    for line in data:
        idx, grabs = line.split(':')
        grabs = grabs.split(';')
        grab_list = []
        for grab in grabs:
            g = [0, 0, 0]
            for color_str in grab.split(','):
                amount, color = color_str.strip().split(' ')
                g[color_map[color]] = int(amount)
            grab_list.append(g)
            # print(grab, '=>', g)
        games.append(Game(int(idx.split(' ')[1]), grab_list))
    return games


def part1(data: List[str]):
    games = parse_input(data)
    id_sum = 0
    for game in games:
        max_red = max([g[0] for g in game.grabs])
        max_green = max([g[1] for g in game.grabs])
        max_blue = max([g[2] for g in game.grabs])
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            id_sum += game.id
    return id_sum


def part2(data: List[str]):
    games = parse_input(data)
    power_sum = 0
    for game in games:
        min_red = max([g[0] for g in game.grabs])
        min_green = max([g[1] for g in game.grabs])
        min_blue = max([g[2] for g in game.grabs])
        power_sum += min_red * min_green * min_blue
    return power_sum


def main():
    with open('inputs/day02.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 8, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 2512, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 2286, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 67335, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
