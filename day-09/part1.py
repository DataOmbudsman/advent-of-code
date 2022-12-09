class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_position(self):
        return self.x, self.y

    def move_in_direction(self, direction):
        if direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        else:
            raise RuntimeError("Unknown direction")

    def move_to_position(self, x, y):
        self.x = x
        self.y = y

    def is_touching_point(self, point: 'Point'):
        return abs(self.x - point.x) < 2 and abs(self.y - point.y) < 2


class Bridge:
    def __init__(self):
        self._head = Point()
        self._tail = Point()
        self._tail_positions = set(self._tail.get_position())

    def process_steps(self, direction, n):
        for _ in range(n):
            self._process_step(direction)

    def _process_step(self, direction):
        self._move_head(direction)
        if not self._head.is_touching_point(self._tail):
            self._move_tail()

    def _move_head(self, direction):
        self._head.move_in_direction(direction)

    def _move_tail(self):
        # same row
        if self._head.x == self._tail.x:
            self._move_tail_closer_horizontally()

        # same column
        elif self._head.y == self._tail.y:
            self._move_tail_closer_vertically()

        # diagonally
        else:
            self._move_tail_closer_horizontally()
            self._move_tail_closer_vertically()

        self._tail_positions.add(self._tail.get_position())

    def _move_tail_closer_horizontally(self):
        if self._head.y - self._tail.y > 0:
            self._tail.y += 1
        else:
            self._tail.y -= 1

    def _move_tail_closer_vertically(self):
        if self._head.x - self._tail.x > 0:
            self._tail.x += 1
        else:
            self._tail.x -= 1

    def count_tail_positions(self):
        return len(self._tail_positions)


def main():
    with open('input') as lines:
        bridge = Bridge()
        for line in lines:
            line = line.rstrip()
            direction, n_steps = line.split()
            bridge.process_steps(direction, int(n_steps))

    print(bridge.count_tail_positions())


if __name__ == "__main__":
    main()
