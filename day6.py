import aoc

def calc(solution, num, op):
    if solution is None:
        solution = num
    elif op == '+':
        solution += num
    elif op == '*':
        solution *= num
    else:
        assert False  # unknown op
    return solution

# Parse
homework = aoc.lines(example=False)
maxlen = max(len(line) for line in homework)
numbers = homework[:-1]
ops = homework[-1]
columns = [idx for idx, op in enumerate(ops) if op != ' '] + [maxlen]
ops = ops.split()

# Part 1 - Solve each problem (column) and sum the solutions, numbers are written per line
p1 = 0
for i, (cols, cole) in enumerate(zip(columns, columns[1:])):
    op = ops[i]
    solution = None
    for line in numbers:
        num = line[cols:min(cole, len(line))]
        num = ''.join(num).strip()
        if not num:
            continue
        else:
            solution = calc(solution, int(num), op)

    p1 += solution

print(p1)

# Part 2 - Solve each problem (column) and sum the solutions, numbers are written top-down over multiple lines
p2 = 0
for i, (cols, cole) in enumerate(zip(columns, columns[1:])):
    op = ops[i]
    solution = None
    for b in range(cole - cols):
        num = [line[cols + b] for line in numbers if cols + b < len(line)]
        num = ''.join(num).strip()
        if not num:
            continue
        else:
            solution = calc(solution, int(num), op)

    p2 += solution

print(p2)
