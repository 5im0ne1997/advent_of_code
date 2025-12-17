import pathlib
import copy

with open(pathlib.Path('2025','day_01.txt')) as file:
    input_file = file.read().splitlines()

moves = [(line[:1],int(line[1:])) for line in input_file]

position = 50
solution_1 = 0

for direction, distance in moves:
    if direction == 'L':
        position -= distance
    elif direction == 'R':
        position += distance
    position = position % 100
    if position == 0:
        solution_1 += 1

print(solution_1)
