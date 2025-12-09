import aoc
from aoc import Point
from itertools import combinations

tiles = []
for line in aoc.lines(example=False):
    x, y = map(int, line.split(','))
    tiles.append(Point(x, y))

def size(t1, t2):
    return (abs(t2.x - t1.x) + 1) * (abs(t2.y - t1.y) + 1)

rectangle_sizes = []
for t1, t2 in combinations(tiles, 2):
    rectangle_sizes.append(size(t1, t2))

part1 = max(rectangle_sizes)
print(part1)
