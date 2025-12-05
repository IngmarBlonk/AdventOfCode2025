import aoc

fresh, available = aoc.input(example=False).split('\n\n')

fresh_ranges = []
for idrange in fresh.split():
    start, end = idrange.split('-')
    fresh_ranges.append(range(int(start), int(end) + 1))

available_ids = [int(id) for id in available.split()]

# Simplify ranges for overlaps
todo = fresh_ranges
fresh_ranges = []
while todo:
    new = todo.pop()
    for have in fresh_ranges:
        if have.start <= new.start <= new.stop <= have.stop:  # new inside have
            new = range(0)
            break
        if new.start <= have.start <= have.stop <= new.stop:  # have inside new
            todo.append(range(have.stop, new.stop))
            new = range(new.start, have.start)
        if new.start <= have.start <= new.stop <= have.stop:  # end of new overlaps start of have
            new = range(new.start, have.start)
        if have.start <= new.start <= have.stop <= new.stop:  # end of have overlaps start of new
            new = range(have.stop, new.stop)

    if new:
        fresh_ranges.append(new)

# Calculate available fresh product count
part1 = 0
for available in available_ids:
    if any((available in fresh for fresh in fresh_ranges)):
        part1 += 1
print(part1)

# Calculate unique fresh product ID count
part2 = sum(len(r) for r in fresh_ranges)
print(part2)
