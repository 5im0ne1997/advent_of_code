from pathlib import Path
from itertools import batched
from collections import defaultdict
from copy import deepcopy

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

crates_2 = deepcopy(crates)

for move in moves:
    number = int(move[1])
    move_from = int(move[3])
    move_to  = int(move[5])
    first_part, second_part = [crates[move_from][:len(crates[move_from]) - number], crates[move_from][len(crates[move_from]) - number:]]
    first_part_2, second_part_2 = [crates_2[move_from][:len(crates_2[move_from]) - number], crates_2[move_from][len(crates_2[move_from]) - number:]]
    crates[move_from] = first_part
    crates_2[move_from] = first_part_2
    if len(second_part) > 1:
        second_part.reverse()
    crates[move_to] = crates[move_to] + second_part
    crates_2[move_to] = crates_2[move_to] + second_part_2
    


part1 = ''
part2 = ''

for crate in crates.values():
    part1 = f"{part1}{crate[-1]}"
for crate in crates_2.values():
    part2 = f"{part2}{crate[-1]}"

print(part1)
print(part2)