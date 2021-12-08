#!/usr/bin/python3

import aoc
import flights


def _visit_next(last_visit, total, visited, distances):
    unvisited = [i for i, x in enumerate(visited) if x == 0]
    if unvisited:
        max_route = 0
        for index in unvisited:
            search_key = str(sorted([last_visit, index]))
            visited[index] = 1
            max_local = _visit_next(
                index, total + distances[search_key], visited, distances
            )
            if max_local > max_route:
                max_route = max_local
            visited[index] = 0

        return max_route
    return total


def _run(reader):
    (distances, ids) = flights.parse_flights(reader)
    visited = []
    for i in range(len(ids)):
        visited.append(0)

    max_route = 0
    for name, id in ids.items():
        visited[id] = 1
        max_local = _visit_next(id, 0, visited, distances)
        if max_local > max_route:
            max_route = max_local
        visited[id] = 0
    return max_route


aoc.load(_run)
