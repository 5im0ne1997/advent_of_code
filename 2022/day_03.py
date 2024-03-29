from pathlib import Path
from itertools import batched

with open(Path("2022", "day_03.txt")) as file:
    input_file = [line for line in file.read().split("\n")]

part1 = 0
for line in input_file:
    first_part, second_part = [line[:len(line)//2], line[len(line)//2:]]
    for c in first_part:
        if c in second_part:
            if c.isupper():
                part1 += ord(c) - 38
            else:
                part1 += ord(c) - 96
            break
print(part1)

part2 = 0
for group in batched(input_file, n=3):

    for c in group[0]:
        if c in group[1] and c in group[2]:
            if c.isupper():
                part2 += ord(c) - 38
            else:
                part2 += ord(c) - 96
            break

print(part2)