from string import ascii_letters

PRIORITY_OF_ITEM_TYPE = {char: ix + 1 for ix, char in enumerate(ascii_letters)}


def calculate_priority(rucksack):
    size_half = int(len(rucksack) / 2)
    part1, part2 = rucksack[:size_half], rucksack[size_half:]
    common_item_type = set.intersection(set(part1), set(part2)).pop()
    priority = PRIORITY_OF_ITEM_TYPE[common_item_type]
    return priority


def main():
    with open('input') as lines:
        total_priorities = 0
        for line in lines:
            line = line.rstrip()
            priority = calculate_priority(line)
            total_priorities += priority

    print(total_priorities)


if __name__ == "__main__":
    main()
