import aoc

# Parse
homework = aoc.lines(example=False)
numbers = {}
for line in homework[:-1]:
    for i, number in enumerate(line.split()):
        numbers.setdefault(i, []).append(int(number))

# Part 1 - Solve each problem and sum the solutions
p1 = 0
for i, op in enumerate(homework[-1].split()):
    solution = numbers[i][0]
    for num in numbers[i][1:]:
        if op == '+':
            solution += num
        elif op == '*':
            solution *= num
        else:
            assert False
    p1 += solution

print(p1)
