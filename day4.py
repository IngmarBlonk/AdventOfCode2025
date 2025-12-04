import aoc
from aoc import Point

grid = set()
for y, line in enumerate(aoc.lines(example=False)):
    for x, roll in enumerate(line):
        if roll == '@':
            grid.add(Point(x, y))

# Calculate adjacent position offsets
adj = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x or y:
            adj.append(Point(x, y))

# Count rolls with less than 4 adjacent rolls
part1 = 0
for roll in grid:
    adj_count = 0
    for p in adj:
        if roll + p  in grid:
            adj_count += 1

    if adj_count < 4:
        part1 += 1

print(part1)

# Calculate maximum rolls which can be removed
part2 = 0
rolls_remaining = list(grid)
removed = True
while removed:
    removed = False
    for roll in rolls_remaining.copy():
        adj_count = 0
        for p in adj:
            if roll + p in rolls_remaining:
                adj_count += 1
        if adj_count < 4:
            part2 += 1
            rolls_remaining.remove(roll)
            removed = True

print(part2)
