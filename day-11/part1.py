class Item:
    def __init__(self, x):
        self._score = x

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def __repr__(self):
        return str(self._score)


class Monkey:
    def __init__(self,
                 starting_items,
                 operation,
                 test_divisor,
                 to_if_true,
                 to_if_false):

        self.items = [Item(score) for score in starting_items]
        self._operation = lambda old: eval(operation)
        self.test_divisor = test_divisor
        self._to_if_true = to_if_true
        self._to_if_false = to_if_false
        self._inspection_count = 0

    def inspect_and_throw_item_to(self):
        self._inspection_count += 1
        item_to_throw = self.items[0]
        self.items = self.items[1:]

        item_to_throw.score = self._operation(item_to_throw.score)
        item_to_throw.score = item_to_throw.score // 3

        if item_to_throw.score % self.test_divisor == 0:
            return item_to_throw, self._to_if_true
        else:
            return item_to_throw, self._to_if_false

    def catch_item(self, item: Item):
        self.items.append(item)

    def get_monkey_score(self):
        return self._inspection_count


class PlayingMonkeys:
    def __init__(self):
        self._monkeys = {}
        self._global_divisor = 1

    def parse_and_create_monkey(self, raw_lines):
        monkey_id = raw_lines[0].replace("Monkey ", "").replace(":", "")

        starting_items = [
            int(score) for score
            in raw_lines[1].replace("  Starting items: ", "").split(", ")
        ]

        operation = raw_lines[2].replace("  Operation: new = ", "")

        test_divisor = int(raw_lines[3].replace("  Test: divisible by ", ""))

        to_if_true = raw_lines[4].replace("    If true: throw to monkey ", "")
        to_if_false = \
            raw_lines[5].replace("    If false: throw to monkey ", "")

        monkey = Monkey(
            starting_items, operation, test_divisor, to_if_true, to_if_false)
        self._monkeys[monkey_id] = monkey

    def play(self, n_rounds):
        for _ in range(n_rounds):
            self._play_round()

    def _play_round(self):
        for throwing_monkey in self._monkeys.values():
            for _ in range(len(throwing_monkey.items)):
                item, to_id = throwing_monkey.inspect_and_throw_item_to()
                catching_monkey = self._monkeys[to_id]
                catching_monkey.catch_item(item)

    def calculate_monkey_business(self):
        monkey_scores = [monkey.get_monkey_score()
                         for monkey in self._monkeys.values()]
        monkey_scores = sorted(monkey_scores)
        return monkey_scores[-2] * monkey_scores[-1]


def main():
    with open('input') as lines:
        monkeys = PlayingMonkeys()
        raw_input_for_next_monkey = []
        for line in lines:
            line = line.rstrip()
            if line != '':
                raw_input_for_next_monkey.append(line)
                if "If false" in line:
                    monkeys.parse_and_create_monkey(raw_input_for_next_monkey)
                    raw_input_for_next_monkey = []

    monkeys.play(n_rounds=20)
    print(monkeys.calculate_monkey_business())


if __name__ == "__main__":
    main()
