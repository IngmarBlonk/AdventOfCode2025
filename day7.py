import aoc
from collections import defaultdict

p1 = 0
timelines = defaultdict(int)
for line in aoc.lines(example=False):
    if 'S' in line:
        timelines[line.index('S')] = 1

    for beam in timelines.copy():
        if line[beam] == '^':
            if timelines[beam]:
                p1 += 1
            timelines[beam - 1] = timelines[beam - 1] + timelines[beam]
            timelines[beam + 1] = timelines[beam + 1] + timelines[beam]
            timelines[beam] = 0

print(p1)  # count number of splits
p2 = sum(timelines.values())
print(p2)  # count number of particle timelines
