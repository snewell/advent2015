import re

_LINE_RE = re.compile(R"^([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)$")

_NEXT_ID = 0


def _get_city_id(cities, name):
    global _NEXT_ID

    if name not in cities:
        id = _NEXT_ID
        _NEXT_ID += 1
        cities[name] = id
        return id
    return cities[name]


def parse_flights(reader):
    cities = {}
    distances = {}
    line = reader.readline()
    while line:
        m = _LINE_RE.match(line)
        first = m.group(1)
        second = m.group(2)
        distance = int(m.group(3))
        first_id = _get_city_id(cities, first)
        second_id = _get_city_id(cities, second)
        distances[str(sorted([first_id, second_id]))] = distance
        line = reader.readline()

    return (distances, cities)
