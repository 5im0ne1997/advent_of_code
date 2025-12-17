import pathlib
from copy import copy

with open(pathlib.Path('2025','day_01.txt')) as file:
    input_file = file.read().splitlines()

moves = [(line[:1],int(line[1:])) for line in input_file]

position = 50
previous_position = copy(position)
solution_1 = 0
solution_2 = 0

for direction, distance in moves:
    if direction == 'L':
        position -= distance
    elif direction == 'R':
        position += distance
    if position != 100 and previous_position != 0:
        solution_2 += abs(position // 100)
    position = position % 100
    if position == 0:
        solution_1 += 1
        solution_2 += 1
    previous_position = copy(position)

print(solution_1)
print(solution_2)
