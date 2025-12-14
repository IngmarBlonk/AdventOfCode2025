import aoc

def parse(*, example):
    *shapes_str, regions_str = aoc.input(example=example).split('\n\n')

    shapes = []
    for shape in shapes_str:
        shape = shape[1:]  # cut off index indicator
        shapes.append(shape.count('#'))

    regions = []
    for line in regions_str.split('\n'):
        size, packages = line.split(': ')
        width, height = map(int, size.split('x'))
        packages = map(int, packages.split())
        regions.append((width, height, packages))

    return shapes, regions


# Part 1 - Find the number regions where the packages fit in the area
shapes, regions = parse(example=False)
part1 = 0
efficiency = 0.85  # Estimated from example; real input also works with 1.0
for width, height, packages in regions:
    space_needed = sum(shapes[i] * count for i, count in enumerate(packages))
    if width * height * efficiency >= space_needed:
        part1 += 1
print(part1)
