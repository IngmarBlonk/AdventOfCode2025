import aoc

part1 = 0
part2 = 0

for bank in aoc.lines(example=False):
    d1 = max(bank[:-1])
    d2 = max(bank[bank.index(d1) + 1:])
    joltage = int(d1 + d2)
    part1 += joltage

    joltage = 0
    for i in reversed(range(12)):
        battery = max(bank[:-i] if i else bank)
        bank = bank[bank.index(battery) + 1:]
        joltage = joltage * 10 + int(battery)
    part2 += joltage

print(part1)
print(part2)
