#!/usr/bin/python3

import aoc
import flights


def _visit_next(last_visit, total, visited, distances):
    unvisited = [i for i, x in enumerate(visited) if x == 0]
    if unvisited:
        min_route = None
        for index in unvisited:
            search_key = str(sorted([last_visit, index]))
            visited[index] = 1
            min_local = _visit_next(
                index, total + distances[search_key], visited, distances
            )
            if (min_route is None) or (min_local < min_route):
                min_route = min_local
            visited[index] = 0

        return min_route
    return total


def _run(reader):
    (distances, ids) = flights.parse_flights(reader)
    visited = []
    for i in range(len(ids)):
        visited.append(0)

    min_route = None
    for name, id in ids.items():
        visited[id] = 1
        min_local = _visit_next(id, 0, visited, distances)
        if (min_route is None) or (min_local < min_route):
            min_route = min_local
        visited[id] = 0
    return min_route


aoc.load(_run)
