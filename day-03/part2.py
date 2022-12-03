from string import ascii_letters

PRIORITY_OF_ITEM_TYPE = {char: ix + 1 for ix, char in enumerate(ascii_letters)}


def calculate_priority(lines):
    common_item_type = set.intersection(
        set(lines[0]), set(lines[1]), set(lines[2])
    ).pop()
    priority = PRIORITY_OF_ITEM_TYPE[common_item_type]
    return priority


def main():
    with open('input') as lines:
        total_priorities = 0
        triple = []
        for ix, line in enumerate(lines):
            line = line.rstrip()
            triple.append(line)
            if ix % 3 == 2:
                priority = calculate_priority(triple)
                total_priorities += priority
                triple = []

    print(total_priorities)


if __name__ == "__main__":
    main()
