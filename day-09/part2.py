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
    def __init__(self, n_knots):
        self._n = n_knots
        self._knots = [Point() for _ in range(self._n)]
        self._tail_positions = set(self._knots[-1].get_position())

    def process_steps(self, direction, n):
        for _ in range(n):
            self._process_step(direction)

    def _process_step(self, direction):
        self._move_first(direction)
        for i in range(1, self._n):
            knot1 = self._knots[i-1]
            knot2 = self._knots[i]
            if not knot1.is_touching_point(knot2):
                self._move_second_after_first(knot1, knot2)

        self._tail_positions.add(self._knots[-1].get_position())

    def _move_first(self, direction):
        self._knots[0].move_in_direction(direction)

    def _move_second_after_first(self, knot1, knot2):
        # same row
        if knot1.x == knot2.x:
            self._move_second_closer_horizontally(knot1, knot2)

        # same column
        elif knot1.y == knot2.y:
            self._move_second_closer_vertically(knot1, knot2)

        # diagonally
        else:
            self._move_second_closer_horizontally(knot1, knot2)
            self._move_second_closer_vertically(knot1, knot2)

    @staticmethod
    def _move_second_closer_horizontally(knot1, knot2):
        if knot1.y - knot2.y > 0:
            knot2.y += 1
        else:
            knot2.y -= 1

    @staticmethod
    def _move_second_closer_vertically(knot1, knot2):
        if knot1.x - knot2.x > 0:
            knot2.x += 1
        else:
            knot2.x -= 1

    def count_tail_positions(self):
        # the -1 is dirty, I'm tired to figure out why it's needed
        return len(self._tail_positions) - 1


def main():
    with open('input') as lines:
        bridge = Bridge(10)
        for line in lines:
            line = line.rstrip()
            direction, n_steps = line.split()
            bridge.process_steps(direction, int(n_steps))

    print(bridge.count_tail_positions())


if __name__ == "__main__":
    main()
