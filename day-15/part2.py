XY_MIN = 0
XY_MAX = 4_000_000


class Sensor:
    def __init__(self, raw_line):

        raw_coordinates_sensor, raw_coordinates_beacon = (
            raw_line.replace("Sensor at ", "").split(": closest beacon is at ")
        )

        self.sensor_location = self._parse_coordinates(raw_coordinates_sensor)
        self.beacon_location = self._parse_coordinates(raw_coordinates_beacon)
        self.distance =\
            self._manhattan_distance(self.sensor_location, self.beacon_location)

    def is_point_closer_than_beacon(self, point):
        return self._manhattan_distance(self.sensor_location, point) <= \
               self.distance

    def next_x_in_row_within_range(self, candidate):
        x, y = candidate
        sensor_x, sensor_y = self.sensor_location
        y_diff = abs(y - sensor_y)
        x_diff_max = self.distance - y_diff
        new_x = sensor_x + x_diff_max
        return new_x

    def _parse_coordinates(self, raw_coordinates):
        raw_x, raw_y = raw_coordinates.split(", ")
        x = self._parse_coordinate(raw_x)
        y = self._parse_coordinate(raw_y)
        return x, y

    @staticmethod
    def _parse_coordinate(raw_coordinate):
        return int(raw_coordinate.split("=")[1])

    @staticmethod
    def _manhattan_distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)


def main():
    sensors = []
    with open('input') as lines:
        for line in lines:
            line = line.rstrip()
            sensor = Sensor(line)
            sensors.append(sensor)

    y = XY_MIN
    candidate = None

    while y <= XY_MAX:
        print('New y starts', y)
        x = XY_MIN
        not_covered = True

        while x <= XY_MAX:
            candidate = x, y
            not_covered = True

            for sensor in sensors:
                if sensor.is_point_closer_than_beacon(candidate):
                    not_covered = False
                    new_x = sensor.next_x_in_row_within_range(candidate)
                    x = new_x
                    break

            if not_covered:
                break
            else:
                x += 1

        if not_covered:
            break
        else:
            y += 1

    print(candidate)
    print(candidate[0] * 4_000_000 + candidate[1])


if __name__ == "__main__":
    main()
