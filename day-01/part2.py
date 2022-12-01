class Top3:
    def __init__(self):
        self.top1 = 0
        self.top2 = 0
        self.top3 = 0

    def try_add_to_top3(self, x):
        if x > self.top3:
            self.add_to_top3(x)

    def add_to_top3(self, x):
        if x > self.top1:
            self.top3 = self.top2
            self.top2 = self.top1
            self.top1 = x
        elif x > self.top2:
            self.top3 = self.top2
            self.top2 = x
        else:
            self.top3 = x

    def return_sum(self):
        return self.top1 + self.top2 + self.top3


def main():
    with open('input') as lines:
        elf_calories = 0
        top3 = Top3()

        for line in lines:
            line = line.rstrip()

            if line != '':
                calories = int(line)
                elf_calories += calories
            else:
                top3.try_add_to_top3(elf_calories)
                elf_calories = 0

    print(top3.return_sum())


if __name__ == "__main__":
    main()
