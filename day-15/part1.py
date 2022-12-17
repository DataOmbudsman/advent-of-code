Y_LINE = 2_000_000
X_MIN = -10_000_000
X_MAX = 10_000_000


class Sensor:
    def __init__(self, raw_line):

        raw_coordinates_sensor, raw_coordinates_beacon = (
            raw_line.replace("Sensor at ", "").split(": closest beacon is at ")
        )

        self.sensor_location = self._parse_coordinates(raw_coordinates_sensor)
        self.beacon_location = self._parse_coordinates(raw_coordinates_beacon)
        self.distance =\
            self._manhattan_distance(self.sensor_location, self.beacon_location)
        self._set_global_limits()

    def is_point_closer_than_beacon(self, point):
        return self._manhattan_distance(self.sensor_location, point) <= \
               self.distance

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

    def _set_global_limits(self):
        global X_MIN, X_MAX
        X_MIN = min(X_MIN, self.sensor_location[0] - self.distance - 1)
        X_MAX = max(X_MIN, self.sensor_location[0] + self.distance + 1)


def main():
    global X_MIN, X_MAX

    sensors = []
    with open('input') as lines:
        for line in lines:
            line = line.rstrip()
            sensor = Sensor(line)
            sensors.append(sensor)

    impossible_points = set()
    for x in range(X_MIN, X_MAX + 1):
        y = Y_LINE
        candidate = x, y
        for sensor in sensors:
            if (
                    sensor.is_point_closer_than_beacon(candidate) and
                    candidate != sensor.sensor_location and
                    candidate != sensor.beacon_location
            ):
                impossible_points.add(candidate)

    print(len(impossible_points))


if __name__ == "__main__":
    main()
