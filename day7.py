import aoc

p1 = 0
beams = set()
for line in aoc.lines(example=False):
    if 'S' in line:
        beams.add(line.index('S'))

    for beam in beams.copy():
        if line[beam] == '^':
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)
            p1 += 1
print(p1)
