from collections import defaultdict

import aoc

devices = {}
for line in aoc.lines(example=False):
    device, outputs = line.split(':')
    outputs = outputs.strip().split()
    devices[device] = outputs

# Part 1 - Find the number of paths between device 'you' and device 'out'
paths = defaultdict(int)
todo = ['you']
while todo:
    dev = todo.pop()
    paths[dev] = paths[dev] + 1
    if dev in devices:
        todo.extend(devices[dev])

part1 = paths['out']
print(part1)
