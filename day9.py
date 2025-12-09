from collections import namedtuple
import aoc
from aoc import Point
from itertools import combinations

class Rect(namedtuple("Rect", "left top right bottom")):
    @property
    def size(self):
        return (self.right - self.left + 1) * (self.bottom - self.top + 1)

    def intersects(self, t1, t2):
        if t1.x != t2.x:
            left = min(t1.x, t2.x)
            right = max(t1.x, t2.x)
            y = t1.y
            return (self.top <= y <= self.bottom) and (left <= self.left <= right or left <= self.right <= right or (left <= self.left and right >= self.right))
        else:
            top = min(t1.y, t2.y)
            bottom = max(t1.y, t2.y)
            x = t1.x
            return (self.left <= x <= self.right) and (top <= self.top <= bottom or top <= self.bottom <= bottom or (top <= self.top and bottom >= self.bottom))

    @property
    def corners(self):
        return (
            Point(self.left, self.top),
            Point(self.right, self.top),
            Point(self.right, self.bottom),
            Point(self.left, self.bottom))

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

# Part 2 - Find maximum rectangle fully enclosed by path between tiles
rectangles = sorted(rectangles, key=lambda r: r.size, reverse=True)
for rect in rectangles:
    lines = zip(tiles, tiles[1:] + tiles[:1])
    for t1, t2 in lines:
        # Check for intersection, but exclude the lines creating the corners
        if rect.intersects(t1, t2) and not (t1 in rect.corners or t2 in rect.corners):
            break
    else:
        part2 = rect.size
        print(part2)
        break
