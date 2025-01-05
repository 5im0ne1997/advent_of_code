from pathlib import Path

with open(Path("2015","day_08.txt")) as input_file:
    strings = [r for r in input_file.read().split("\n")]

solution_1 = 0
solution_2 = 0
for row in strings:
    solution_1 += len(row) - len(row.encode().decode('unicode_escape')[1:-1])
    new_encode = '"'
    for c in row:
        if c == '"':
            new_encode = new_encode + '\\"'
        elif c == "\\":
            new_encode = new_encode + '\\\\'
        else:
            new_encode = new_encode + c
    new_encode = new_encode + '"'
    solution_2 += len(new_encode) - len(row)

print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}")