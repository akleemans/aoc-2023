import math
from typing import List, Tuple, Dict

# Day 20: Pulse Propagation

test_data = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''.split('\n')

test_data2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''.split('\n')


class Module:
    mtype: str
    name: str
    receivers: List[str]
    out_signals: List[Tuple[str, str, str]]
    flip_flop_on: bool
    conjunction_input_signals: Dict[str, str]
    conjunction_triggered: bool

    def __init__(self, mtype: str, name: str, receivers: List[str]):
        self.mtype = mtype
        self.name = name
        self.receivers = receivers
        self.out_signals = []
        if self.is_flip_flop():
            self.flip_flop_on = False
        elif self.is_conjunction():
            self.conjunction_input_signals = {}
            self.conjunction_triggered = False

    def is_flip_flop(self):
        return self.mtype == '%'

    def is_broadcast(self):
        return self.mtype == 'b'

    def is_conjunction(self):
        return self.mtype == '&'

    def receive_pulse(self, signal_type, sender):
        if self.is_broadcast():
            self.out_signals = [(self.name, signal_type, r) for r in self.receivers]
        elif self.is_flip_flop():
            if signal_type == 'low':
                self.flip_flop_on = not self.flip_flop_on
                if self.flip_flop_on:
                    out_signal = 'high'
                else:
                    out_signal = 'low'
                self.out_signals = [(self.name, out_signal, r) for r in self.receivers]
        elif self.is_conjunction():
            self.conjunction_input_signals[sender] = signal_type
            self.conjunction_triggered = True

    def get_out_signals(self) -> List:
        if self.is_conjunction():
            out_signals = []
            if self.conjunction_triggered:
                out_signal = 'low' if all(s == 'high' for s in self.conjunction_input_signals.values()) else 'high'
                out_signals = [(self.name, out_signal, r) for r in self.receivers]
                self.conjunction_triggered = False
        else:
            out_signals = [*self.out_signals]
        self.out_signals = []
        return out_signals

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


def build_modules(data):
    modules = {}
    for line in data:
        name, receivers = line.split(' -> ')
        mtype = name[0]
        if name != 'broadcaster':
            name = name[1:]
        modules[name] = Module(mtype, name, receivers.split(', '))
    # Get in-signals for conjunctions
    for conjunction_name in modules:
        if modules[conjunction_name].is_conjunction():
            in_connections = {}
            for in_module_name in modules:
                if conjunction_name in modules[in_module_name].receivers:
                    in_connections[in_module_name] = 'low'
            modules[conjunction_name].conjunction_input_signals = in_connections
    return modules


def simulate(modules, cycles):
    counter = {'low': 0, 'high': 0}
    for i in range(cycles):
        queue = [[('start', 'low', 'broadcaster')]]
        time_step = 0
        while len(queue) > 0:
            # print(f'Time step: {time_step}')
            current_pulses = queue.pop(0)

            # First, process pulses
            for pulse in current_pulses:
                sender, signal_type, receiver = pulse
                counter[signal_type] += 1
                # print(f'{sender} -{signal_type}-> {receiver}')
                if receiver in modules:
                    modules[receiver].receive_pulse(signal_type, sender)
                    queue.append(modules[receiver].get_out_signals())
            time_step += 1
    return counter['high'] * counter['low']


def part1(data: List[str], cycles=1000):
    modules = build_modules(data)
    return simulate(modules, cycles)


def part2(data: List[str]):
    modules = build_modules(data)
    counter = {'low': 0, 'high': 0}
    button_presses = 1
    critical_senders = ['rk', 'cd', 'zf', 'qx']
    sender_values = {'rk': 0, 'cd': 0, 'zf': 0, 'qx': 0}
    while any(v == 0 for v in sender_values.values()):
        queue = [[('start', 'low', 'broadcaster')]]
        while len(queue) > 0:
            current_pulses = queue.pop(0)
            for pulse in current_pulses:
                sender, signal_type, receiver = pulse
                counter[signal_type] += 1
                if sender in critical_senders and sender_values[sender] == 0 and signal_type == 'high':
                    sender_values[sender] = button_presses
                    # print(f'sender {sender} has phase {button_presses}')
                if receiver in modules:
                    modules[receiver].receive_pulse(signal_type, sender)
                    queue.append(modules[receiver].get_out_signals())
        button_presses += 1
    return math.lcm(*sender_values.values())


def main():
    with open('inputs/day20.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 1)
    assert part1_test_result == 32, f'Part 1 test1 input (1 cycle) returned {part1_test_result}'
    part1_test_result = part1(test_data)
    assert part1_test_result == 32000000, f'Part 1 test1 input (1k cycles) returned {part1_test_result}'
    part1_test2_result = part1(test_data2, 1)
    assert part1_test2_result == 16, f'Part 1 test2 input (1 cycle) returned {part1_test2_result}'
    part1_test2_result = part1(test_data2, 4)
    assert part1_test2_result == 187, f'Part 1 test2 input (4 cycles) returned {part1_test2_result}'
    part1_test2_result = part1(test_data2)
    assert part1_test2_result == 11687500, f'Part 1 test2 input (1k cycles) returned {part1_test2_result}'
    part1_result = part1(data)
    assert part1_result == 730797576, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 226732077152351, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
