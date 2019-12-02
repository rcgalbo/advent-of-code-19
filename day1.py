# day 1
from math import floor

# part 1
def calculate_fuel(mass: int) -> int:
    return floor(mass / 3) - 2

assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

with open('day1_input.txt') as modules:
    fuel = [calculate_fuel(int(mass)) for mass in modules.readlines()]

print(sum(fuel))

# part 2
def calculate_fuels_fuel(mass: int) -> int:

    fuels = [calculate_fuel(mass)]

    while (fuel := calculate_fuel(fuels[-1])) > 0:
        fuels.append(fuel)

    return sum(fuels)

assert calculate_fuels_fuel(14) == 2
assert calculate_fuels_fuel(1969) == 966
assert calculate_fuels_fuel(100756) == 50346

with open('day1_input.txt') as modules:
    fuels_fuel = [calculate_fuels_fuel(int(mass)) for mass in modules.readlines()]

print(sum(fuels_fuel))