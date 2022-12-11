class CRT:
    def __init__(self):
        self.cycle = 1
        self.register = 1
        self.total_signal_strength = 0
        self.notable_cycles = [20, 60, 100, 140, 180, 220]

    def update_register(self, value):
        self.register += value

    def increment_cycle(self):
        if self.cycle in self.notable_cycles:
            self._increase_total_signal_strength()
        self.cycle += 1

    def _increase_total_signal_strength(self):
        signal_strength = self.cycle * self.register
        self.total_signal_strength += signal_strength


def main():
    with open('input') as lines:
        crt = CRT()

        for line in lines:
            line = line.rstrip()
            if line == 'noop':
                crt.increment_cycle()
            else:
                value = int(line.split()[1])
                crt.increment_cycle()
                crt.increment_cycle()
                crt.update_register(value)

    print(crt.total_signal_strength)


if __name__ == "__main__":
    main()
