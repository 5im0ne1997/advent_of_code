from pathlib import Path
from itertools import batched
from collections import defaultdict

with open(Path("2022","day_05.txt")) as file:
    stack_input, move_input = file.read().split("\n\n")

moves = [[c for c in move.split(" ")] for move in move_input.split("\n")]
stacks_temp = [stacks for stacks in stack_input.split("\n")]
stacks_temp.reverse()

crates = defaultdict(list)

for line in stacks_temp:
    t = 1
    for crate in batched(line, n=4):
        if crate[1].isupper():
            crates[t].append(crate[1])
        t += 1

for move in moves:
    number = int(move[1])
    move_from = int(move[3])
    move_to  = int(move[5])
    for n in range(number):
        crates[move_to].append(crates[move_from].pop())
step1 = ''

for crate in crates.values():
    step1 = f"{step1}{crate[-1]}"

print(step1)
pass