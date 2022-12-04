def _process_section(section):
    start, end = section.split('-')
    return int(start), int(end)


def has_containment(line):
    section1, section2 = line.split(',')
    section1_start, section1_end = _process_section(section1)
    section2_start, section2_end = _process_section(section2)

    section1_contains_section2 = \
        section2_start >= section1_start and section2_end <= section1_end

    section2_contains_section1 = \
        section1_start >= section2_start and section1_end <= section2_end

    return section1_contains_section2 or section2_contains_section1


def main():
    with open('input') as lines:
        count_containments = 0
        for line in lines:
            line = line.rstrip()
            if has_containment(line):
                count_containments += 1

    print(count_containments)


if __name__ == "__main__":
    main()
