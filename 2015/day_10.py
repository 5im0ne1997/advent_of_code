from pathlib import Path
from itertools import groupby

with open(Path('2015','day_10.txt')) as file:
    puzzle_imput = file.read()

count = 0
step_input = puzzle_imput

while count < 50:
    step_input = "".join(map(str,["".join(map(str,[len(list(g)), k])) for k, g in groupby(step_input)]))
    count += 1
    if count == 40:
        print(len(step_input))

print(len(step_input))
