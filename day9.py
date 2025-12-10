import aoc
from aoc import Point
from collections import namedtuple
from itertools import combinations

class Rect(namedtuple("Rect", "left bottom right top")):
    @property
    def size(self):
        return (self.right - self.left + 1) * (self.top - self.bottom + 1)

# Parse tiles
tiles = []
for line in aoc.lines(example=False):
    x, y = map(int, line.split(','))
    tiles.append(Point(x, y))

# Build rectangles
rectangles = []
for t1, t2 in combinations(tiles, 2):
    rect = Rect(min(t1.x, t2.x), min(t1.y, t2.y), max(t1.x, t2.x), max(t1.y, t2.y))
    rectangles.append(rect)

# Part 1 - Find maximum rectangle area with tiles as corner
part1 = max(rect.size for rect in rectangles)
print(part1)

# Compress grid space
xs = sorted(set(tile.x for tile in tiles))
ys = sorted(set(tile.y for tile in tiles))

grid = {}
compressed_tiles = set()
for t1, t2 in zip(tiles, tiles[1:] + tiles[:1]):
    t1 = Point(xs.index(t1.x), ys.index(t1.y))
    t2 = Point(xs.index(t2.x), ys.index(t2.y))
    compressed_tiles.add(t1)
    for x in range(min(t1.x, t2.x), max(t1.x, t2.x) + 1):
        for y in range(min(t1.y, t2.y), max(t1.y, t2.y) + 1):
            grid[Point(x, y)] = 'X'

# Flood fill the area outside the tile loop
todo = [Point(-1, -1)]  # Use 1 out of bound to prevent cutoff by tiles at border
while todo:
    pos = todo.pop()

    # Remain in bounds of grid and check if tile not already known
    if pos in grid or not (-1 <= pos.x <= len(xs) and -1 <= pos.y <= len(ys)):
        continue

    grid[pos] = '.'

    for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        todo.append(pos + Point(*dir))

# Part 2 - Find maximum rectangle fully enclosed by path between tiles
for rect in sorted(rectangles, reverse=True, key=lambda r: r.size):
    rect_compressed = Rect(xs.index(rect.left), ys.index(rect.bottom), xs.index(rect.right), ys.index(rect.top))
    # Check all rectangle tiles not being outside the loop
    if all(grid.get(Point(x, y)) != '.'
           for x in range(rect_compressed.left, rect_compressed.right + 1)
           for y in range(rect_compressed.bottom, rect_compressed.top + 1)):
        break
else:
    assert False, "No valid rectangle found"

part2 = rect.size
print(part2)
