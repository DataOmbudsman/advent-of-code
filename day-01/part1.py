def main():
    with open('input') as lines:
        elf_calories = 0
        max_elf_calories = 0

        for line in lines:
            line = line.rstrip()

            if line != '':
                calories = int(line)
                elf_calories += calories
            else:
                max_elf_calories = max(elf_calories, max_elf_calories)
                elf_calories = 0

    print(max_elf_calories)


if __name__ == "__main__":
    main()
