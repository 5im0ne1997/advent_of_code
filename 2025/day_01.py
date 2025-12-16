import pathlib
import copy

with open(pathlib.Path('2025','day_01.txt')) as file:
    input_file = file.read().splitlines()

moves = [(line[:1],int(line[1:])) for line in input_file]

position = 50
solution_1 = 0

for direction, distance in moves:
    temp_position = copy.copy(position)
    if direction == 'L':
        temp_position -= distance
        
    elif direction == 'R':
        temp_position += distance
    if temp_position > 99:
            position = temp_position - 100
    elif temp_position < 0:
        position = temp_position + 100
    else:
        position = copy.copy(temp_position)
    if position == 0:
        solution_1 += 1

print(solution_1)
