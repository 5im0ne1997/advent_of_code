from pathlib import Path

with open(Path("2022","day_01.txt")) as file:
    input_file = [[int(cal) for cal in elf.split("\n")] for elf in file.read().split("\n\n")]

step1 = []
for elf in input_file:
    sum1 = 0
    for cal in elf:
        sum1 += cal
    step1.append(sum1)

print(max(step1))

step2 = 0
for top_elf in range(3):
    step2 += max(step1)

    step1.pop(step1.index(max(step1)))

print(step2)
