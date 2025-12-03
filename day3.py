import aoc

def calc_joltage(bank, battery_count):
    joltage = 0
    for i in reversed(range(battery_count)):
        battery = max(bank[:-i] if i else bank)
        bank = bank[bank.index(battery) + 1:]
        joltage = joltage * 10 + int(battery)
    return joltage


part1 = 0
part2 = 0

for bank in aoc.lines(example=False):
    part1 += calc_joltage(bank, 2)
    part2 += calc_joltage(bank, 12)

print(part1)
print(part2)
