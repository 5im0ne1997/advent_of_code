from pathlib import Path

with open(Path("2015","day_08.txt")) as input_file:
    strings = [r for r in input_file.read().split("\n")]

solution_1 = 0
for row in strings:
    solution_1 += len(row) - len(row.encode().decode('unicode_escape')[1:-1])

print(f"Solution 1: {solution_1}")