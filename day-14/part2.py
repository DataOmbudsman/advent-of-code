class Sand:
    def __init__(self):
        self.x = 500
        self.y = 0

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def __repr__(self):
        return f'{str(self.x)}, {str(self.y)}'


class Cave:
    def __init__(self):
        self._rocks = set()
        self._sands = set()
        self._bottom = 1000

    def _init_bottom_rocks(self):
        min_rock_y = min(y for x, y in self._rocks)
        max_rock_y = max(y for x, y in self._rocks)

        height = max_rock_y - min_rock_y
        bottom_rock_x_min = 500 - height * 2 - 1
        bottom_rock_x_max = 500 + height * 2 + 1

        bottom_rock_y = max_rock_y + 2

        for x in range(bottom_rock_x_min, bottom_rock_x_max + 1):
            self._rocks.add((x, bottom_rock_y))

    @property
    def _blocked(self):
        return self._rocks.union(self._sands)

    def parse_input_line(self, line):
        coordinates = line.split(' -> ')
        for i in range(len(coordinates) - 1):
            x1, y1 = coordinates[i].split(',')
            x2, y2 = coordinates[i+1].split(',')
            xs = int(x1), int(x2)
            ys = int(y1), int(y2)
            for x in range(min(xs), max(xs)+1):
                for y in range(min(ys), max(ys)+1):
                    self._rocks.add((x, y))

    def sand_pouring_until_rest(self):
        self._init_bottom_rocks()
        sand = Sand()
        while True:
            below = sand.x, sand.y + 1
            if below in self._blocked:
                below_left = sand.x - 1, sand.y + 1
                # try to fall down & left
                if below_left in self._blocked:
                    below_right = sand.x + 1, sand.y + 1
                    # try to fall down & right
                    if below_right in self._blocked:
                        # cannot fall, has to stop
                        self._sands.add((sand.x, sand.y))
                        if sand.x == 500 and sand.y == 0:
                            break
                        sand = Sand()
                    else:
                        sand.move_down()
                        sand.move_right()
                else:
                    sand.move_down()
                    sand.move_left()

            else:
                sand.move_down()

        print(f'{len(self._sands)} came to rest')


def main():
    with open('input') as lines:
        cave = Cave()
        for line in lines:
            line = line.rstrip()
            cave.parse_input_line(line)

    cave.sand_pouring_until_rest()


if __name__ == "__main__":
    main()
