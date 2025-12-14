from collections import defaultdict
import aoc

def paths_from(from_device):
    """Count the number of paths from a specific node to any node in the graph"""

    # Count input edges per node
    indegree = defaultdict(int)
    for dev in devices:
        indegree[dev] = 0
    for dev, outputs in devices.items():
        for out in outputs:
            indegree[out] += 1

    # Topological sort (Kahn's algorithm)
    todo = [dev for dev, count in indegree.items() if count == 0]
    topological_order = []
    while todo:
        dev = todo.pop()
        topological_order.append(dev)
        if dev in devices:
            for output in devices[dev]:
                indegree[output] -= 1
                if indegree[output] == 0:
                    todo.append(output)

    # Count paths in topologic order
    paths = defaultdict(int)
    paths[from_device] = 1
    for dev in topological_order:
        if dev in devices:
            for output in devices[dev]:
                paths[output] += paths[dev]

    return paths


# Parse input
devices = {}
for line in aoc.lines(example=False):
    device, outputs = line.split(':')
    outputs = outputs.strip().split()
    devices[device] = outputs

# Part 1 - Find the number of paths between device 'you' and device 'out'
paths = paths_from('you')
part1 = paths['out']
print(part1)

# Part 2 - Find the number of paths between 'svr' and 'out' via 'dac' and 'fft' in any order
svr_paths = paths_from('svr')
dac_paths = paths_from('dac')
fft_paths = paths_from('fft')
part2 = (svr_paths['dac'] * dac_paths['fft'] * fft_paths['out'] +
         svr_paths['fft'] * fft_paths['dac'] * dac_paths['out'])
print(part2)
