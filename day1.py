import aoc

lines = aoc.lines()

part1 = 0
part2 = 0

dial = 50
for line in lines:
    direction = 1 if line[0] == 'R' else -1
    clicks = int(line[1:]) * direction

    passes = abs(clicks) // 100
    r = clicks - passes * 100 * direction
    if dial == 0:
        pass  # Don't count the start from 0 which was counted in previous rotation
    elif dial + r <= 0:
        passes += 1
    elif dial + r >= 100:
        passes += 1

    part2 += passes  # Count dial passes over 0 WHILE rotating

    dial = (dial + clicks) % 100

    if dial == 0:
        part1 += 1  # Count dial equalling 0 AFTER rotating

print(part1)
print(part2)
