import aoc

part1 = 0
part2 = 0

for id_range in aoc.input().split(','):
    a, b = id_range.split('-')
    a, b = int(a), int(b)

    while a <= b:
        s = str(a)

        # Find ID's of which both halves equal
        h1 = s[:len(s) // 2]
        h2 = s[len(s) // 2:]
        if h1 == h2:
            part1 += a

        # Find ID's of which some sequence of digits repeat at least twice
        for end in range(1, len(s) // 2 + 1):
            if len(s) % end == 0:
                token = s[:end]
                multiple = len(s) // len(token)
                if token * multiple == s:
                    part2 += a
                    break

        a += 1

print(part1)
print(part2)
