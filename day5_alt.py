import aoc

# Parse
fresh, available = aoc.input(example=False).split('\n\n')

fresh_ranges = []
for idrange in fresh.split():
    start, end = idrange.split('-')
    fresh_ranges.append(range(int(start), int(end) + 1))

available_ids = [int(id) for id in available.split()]

# Calculate available fresh product count
part1 = 0
for available in available_ids:
    if any((available in fresh for fresh in fresh_ranges)):
        part1 += 1
print(part1)

# Calculate unique fresh product ID count
part2 = 0
c = 0
for fresh in sorted(fresh_ranges, key=lambda r: r.start):
    if c < fresh.start:
        c = fresh.start
    if c < fresh.stop:
        part2 += fresh.stop - c
        c = fresh.stop
print(part2)
