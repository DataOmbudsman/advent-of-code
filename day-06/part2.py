def _are_different_chars(chars):
    for i, char1 in enumerate(chars):
        for j, char2 in enumerate(chars):
            if i != j and char1 == char2:
                return False
    return True


def find_marker(line, marker_length):
    i = 0
    while not _are_different_chars(line[i: i+marker_length]):
        i += 1
    return i + marker_length


def main():
    with open('input') as lines:
        line = lines.readline()

    marker = find_marker(line, 14)
    print(marker)


if __name__ == "__main__":
    main()
