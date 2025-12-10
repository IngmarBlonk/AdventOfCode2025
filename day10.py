import aoc
from queue import Queue

# Parse
machines = []
for line in aoc.lines(example=False):
    lights, *buttons, joltage = line.split()

    lights = sum(2**i for i, l in enumerate(lights[1:-1]) if l == '#')

    for i, btn in enumerate(buttons):
        buttons[i] = sum(2 ** int(l) for l in btn[1:-1].split(','))

    machines.append((lights, buttons, joltage))

# Part 1 - Find the least amount of button presses to toggle the lights into the desired state
part1 = 0
for desired_lights, buttons, _ in machines:
    todo = Queue()
    todo.put((0, 0))
    while True:
        cstate, presses = todo.get()
        for btn in buttons:
            state = cstate ^ btn
            if state == desired_lights:
                part1 += presses + 1
                break
            todo.put((state, presses + 1))
        else:
            continue
        break

print(part1)
