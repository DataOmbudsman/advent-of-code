import re
from collections import defaultdict, deque


class Stack:
    def __init__(self, initial_state):
        self._stack = deque()
        for element in initial_state:
            self.put_on_top(element)

    def put_on_top(self, element):
        self._stack.append(element)

    def get_from_top(self):
        return self._stack.pop()

    def get_copy_of_top(self):
        stack_to_print = self._stack.copy()
        top = stack_to_print.pop()
        return top


class Crates:
    def __init__(self, initial_states):
        self._stacks = {name: Stack(state)
                        for name, state in initial_states.items()}
        self._move_pattern = re.compile("^move (\\d+) from (\\d+) to (\\d+)$")

    def process_line(self, line):
        match = self._move_pattern.match(line)
        if match:
            how_many, from_, to,  = match.groups()
            self.move(int(how_many), from_, to)

    def move(self, how_many, position_from, position_to):
        crates_to_move = []
        stack_from = self._stacks[position_from]
        stack_to = self._stacks[position_to]

        for _ in range(how_many):
            crate = stack_from.get_from_top()
            crates_to_move.append(crate)

        for crate in crates_to_move[::-1]:
            stack_to.put_on_top(crate)

    def print_top(self):
        tops = [stack.get_copy_of_top()
                for stack in self._stacks.values()]
        print(''.join(tops))


class StateReader:
    def __init__(self):
        self._indexed_states_start_from_top = defaultdict(lambda: [])
        self._state_names = []
        self.still_reading = True

    def read_line(self, line):
        if line.replace(' ', '').replace('[', '').replace(']', '').isalpha():
            self._process_state_line(line)
        elif line.replace(' ', '').isnumeric():
            self._process_name_line(line)
        elif line == '':
            self.still_reading = False

    def _process_state_line(self, line):
        i = 0
        pos = 1
        while pos + 1 < len(line):
            name = line[pos: pos+1]
            if name != ' ':
                self._indexed_states_start_from_top[i].append(name)
            i += 1
            pos += 4

    def _process_name_line(self, line):
        line = line.strip()
        self._state_names = line.split('   ')

    def get_initial_states(self):
        initial_states = {}
        for i, name in enumerate(self._state_names):
            corresponding_state = self._indexed_states_start_from_top[i]
            initial_states[name] = corresponding_state[::-1]
        return initial_states


def main():
    with open('input') as lines:
        state_reader = StateReader()
        initial_reading = True

        for line in lines:
            line = line.rstrip()
            if initial_reading:
                state_reader.read_line(line)
                initial_reading = state_reader.still_reading
                if not initial_reading:
                    initial_states = state_reader.get_initial_states()
                    crates = Crates(initial_states)
            else:
                crates.process_line(line)

    crates.print_top()


if __name__ == "__main__":
    main()
