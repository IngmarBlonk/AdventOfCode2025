import math
from collections import namedtuple
from itertools import combinations
import aoc

example = False
PAIRS = 10 if example else 1000

Point = namedtuple("Point", "x y z id")

boxes = []
for i, line in enumerate(aoc.lines(example=example)):
    x, y, z = map(int, line.split(','))
    boxes.append(Point(x, y, z, i))

def dist(p1, p2):
    return math.sqrt(
        math.pow(p1.x - p2.x, 2) +
        math.pow(p1.y - p2.y, 2) +
        math.pow(p1.z - p2.z, 2)
    )

circuit_boxes = {b: [b] for b in boxes}
circuits = list(circuit_boxes.values())
for b1, b2 in sorted(combinations(boxes, 2), key=lambda c: dist(*c))[:PAIRS]:
    # print("connecting", b1.id, b2.id)
    if circuit_boxes[b1] is not circuit_boxes[b2]:
        merged_circuit = circuit_boxes[b2]
        circuit_boxes[b1].extend(merged_circuit)
        # print("REMOVING", b2.id, merged_circuit)
        for b in merged_circuit:
            # print("UPDATE", b.id)
            circuit_boxes[b] = circuit_boxes[b1]
        circuits.remove(merged_circuit)
    # else:
    #     print("SKIP")

# for circuit in sorted(circuits, key=len, reverse=True)[:10]:
#     print(len(circuit), circuit)

p1 = math.prod(sorted(map(len, circuits), reverse=True)[:3])
print(p1)
