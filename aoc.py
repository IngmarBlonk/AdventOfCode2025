import fileinput
import sys
import re
from collections import namedtuple
import heapq


def input(*, day=None, example=False):
    """Read the raw input for a day"""
    try:
        # First try reading a filename from CLI
        file = fileinput.filename()
    except RuntimeError:
        # Fallback to day derived from current running script
        if day is None:
            m = re.search('day([0-9]+)', sys.argv[0])
            day = int(m.group(1))

        if not example:
            file = f'input/day{day}.txt'
        else:
            file = f'input/day{day}_example.txt'

    with open(file) as f:
        data = f.read().strip()
    return data


def lines(*args, **kwargs):
    """Read input file lines"""
    return input(*args, **kwargs).split('\n')


class Point(namedtuple("Point", "x y")):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    mh = manhattan_distance


def dijkstra(graph, start, neighbours):
    graph = set(graph)  # require set for fast lookups to check for invalid neighbour nodes
    dist, prev = {}, {}
    Q = []
    for v in graph:
        dist[v] = 999999
        heapq.heappush(Q, (999999, v))
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    visited = set()
    while Q:
        _, u = heapq.heappop(Q)
        if u in visited:  # heapq doesn't support changing priority, track and skip visited items
            continue
        visited.add(u)

        for v, cost in neighbours(u):
            if v in visited or v not in graph:
                continue

            alt = dist[u] + cost
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v))

    return dist, prev


def dijkstra_path_to(prev, end):
    path = []
    current = end
    while current in prev:
        path.append(current)
        current = prev[current]
    return list(reversed(path))
