import aoc
from aoc import Point

# Read grid input
grid = set()
for y, line in enumerate(aoc.lines(example=False)):
    for x, roll in enumerate(line):
        if roll == '@':
            grid.add(Point(x, y))

# Calculate adjacent position offsets
adj = [Point(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]

# Build neighbour relation link structure
rolls = {}  # map[roll] = {neighbour rolls}
for roll in grid:
    rolls[roll] = set()
    for offset in adj:
        if roll + offset in grid:
            rolls[roll].add(roll + offset)

# Count rolls with less than 4 adjacent rolls
part1 = 0
for roll in rolls.values():
    if len(roll) < 4:
        part1 += 1

print(part1)

# Calculate maximum rolls which can be removed
part2 = 0
todo = list(rolls)
while todo:
    roll = todo.pop()
    if roll not in rolls:
        continue

    adj_count = [roll + p in rolls for p in adj].count(True)
    if adj_count < 4:
        part2 += 1
        todo.extend(rolls[roll])
        del rolls[roll]

print(part2)
