import aoc

part1 = 0
part2 = 0

for id_range in aoc.input().split(','):
    a, b = id_range.split('-')
    a, b = int(a), int(b)

    while a <= b:
        s = str(a)

        h1 = s[:len(s) // 2]
        h2 = s[len(s) // 2:]
        if h1 == h2:
            part1 += a

        token_ranges = ((i, j) for i in range(len(s) // 2) for j in range(1, len(s) // 2 + 1))
        for i, j in token_ranges:
            if i < j and (len(s) % (j-i)) == 0:
                token = s[i:j]
                multiple = len(s) // len(token)
                if token * multiple == s:
                    part2 += a
                    break

        a += 1

print(part1)
print(part2)
