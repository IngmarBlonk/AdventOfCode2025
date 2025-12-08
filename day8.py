import math
from collections import namedtuple
from itertools import combinations
import aoc

example = False  # Example input data switch
PAIRS = 10 if example else 1000

Point = namedtuple("Point", "x y z id")

# Parse box coordinates
boxes = []
for i, line in enumerate(aoc.lines(example=example)):
    x, y, z = map(int, line.split(','))
    boxes.append(Point(x, y, z, i))

def dist(p1, p2):
    """Calculate the straight-line distance between 2 point"""
    return math.sqrt(
        math.pow(p1.x - p2.x, 2) +
        math.pow(p1.y - p2.y, 2) +
        math.pow(p1.z - p2.z, 2)
    )

# Box circuits
circuit_boxes = {b: [b] for b in boxes}
circuits = list(circuit_boxes.values())

# Connect circuits in order of shortest distance
for i, (b1, b2) in enumerate(sorted(combinations(boxes, 2), key=lambda c: dist(*c))):
    if circuit_boxes[b1] is not circuit_boxes[b2]:  # Skip already connected circuits
        merge_circuit = circuit_boxes[b2]

        for b in merge_circuit:
            circuit_boxes[b] = circuit_boxes[b1]

        circuit_boxes[b1].extend(merge_circuit)
        circuits.remove(merge_circuit)

    if i+1 == PAIRS:
        # Part 1 - Product of top 3 circuit sizes after {PAIRS} connections made
        p1 = math.prod(sorted(map(len, circuits), reverse=True)[:3])
        print(p1)
    elif len(circuits) == 1:
        # Part 2 - Wall distance after connecting all into one big circuit
        p2 = b1.x * b2.x
        print(p2)
        break
