from pathlib import Path
from collections import defaultdict

with open(Path("2022","day_09.txt")) as file:
    moves = file.read().split("\n")

move_dir = {
    'R': (1, 0),
    'U': (0,1),
    'L': (-1,0),
    'D': (0,-1)
}

H_position = (0,0)
T_position = (0,0)

T_visited_part1 = defaultdict(int)

T_visited_part1[T_position]  += 1

for line in moves:
    direction, count = line.split(" ")
    for move in range(int(count)):
        H_position = (H_position[0] + move_dir[direction][0], H_position[1] + move_dir[direction][1])
        T_delta_x = H_position[0] - T_position[0]
        T_delta_y = H_position[1] - T_position[1]
        if (abs(T_delta_x) > 1):
            T_position = (T_position[0] + move_dir[direction][0], T_position[1] + move_dir[direction][1])
            if T_delta_x > 1:
                T_position = (T_position[0] + move_dir['U'][0], T_position[1] + move_dir['U'][1])
            elif T_delta_x < -1:
                T_position = (T_position[0] + move_dir['D'][0], T_position[1] + move_dir['D'][1])
        elif (abs(T_delta_y) > 1):
            T_position = (T_position[0] + move_dir[direction][0], T_position[1] + move_dir[direction][1])
            if T_delta_y > 1:
                T_position = (T_position[0] + move_dir['R'][0], T_position[1] + move_dir['R'][1])
            elif T_delta_y < -1:
                T_position = (T_position[0] + move_dir['L'][0], T_position[1] + move_dir['L'][1])
        T_visited_part1[T_position]  += 1

print(len(T_visited_part1))