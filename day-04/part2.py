def _process_section(section):
    start, end = section.split('-')
    return int(start), int(end)


def has_overlap(line):
    section1, section2 = line.split(',')
    section1_start, section1_end = _process_section(section1)
    section2_start, section2_end = _process_section(section2)

    return section2_end >= section1_start and section1_end >= section2_start


def main():
    with open('input') as lines:
        count_overlaps = 0
        for line in lines:
            line = line.rstrip()
            if has_overlap(line):
                count_overlaps += 1

    print(count_overlaps)


if __name__ == "__main__":
    main()
