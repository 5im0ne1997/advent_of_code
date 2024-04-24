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

class Tail():

    def __init__(self, T_position: tuple) -> None:
        self.T_position = T_position
        self.direction = ""

    def move(self, before_node_position: tuple, direction: str):
        global move_dir
        T_delta_x = before_node_position[0] - self.T_position[0]
        T_delta_y = before_node_position[1] - self.T_position[1]
        if (abs(T_delta_x) > 1):
            self.T_position = (self.T_position[0] + move_dir[direction][0], self.T_position[1] + move_dir[direction][1])
            self.direction = direction
            if T_delta_y > 0:
                self.T_position = (self.T_position[0] + move_dir['U'][0], self.T_position[1] + move_dir['U'][1])
            elif T_delta_y < 0:
                self.T_position = (self.T_position[0] + move_dir['D'][0], self.T_position[1] + move_dir['D'][1])
        elif (abs(T_delta_y) > 1):
            self.T_position = (self.T_position[0] + move_dir[direction][0], self.T_position[1] + move_dir[direction][1])
            self.direction = direction
            if T_delta_x > 0:
                self.T_position = (self.T_position[0] + move_dir['R'][0], self.T_position[1] + move_dir['R'][1])
            elif T_delta_x < 0:
                self.T_position = (self.T_position[0] + move_dir['L'][0], self.T_position[1] + move_dir['L'][1])
        else:
            self.direction = ""

H_position = (0,0)

T_positions1 = Tail((0,0))
T_visited_part1 = defaultdict(int)
T_visited_part1[T_positions1.T_position]  += 1

T_positions2 = [Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0)), Tail((0,0))]
T_visited_part2 = defaultdict(int)
T_visited_part2[T_positions2[-1].T_position]  += 1

for line in moves:
    direction, count = line.split(" ")
    for move in range(int(count)):
        H_position = (H_position[0] + move_dir[direction][0], H_position[1] + move_dir[direction][1])
        T_positions1.move(H_position, direction)
        T_visited_part1[T_positions1.T_position]  += 1
        before_node_position = H_position
        before_node_direction = direction
        for T_part2 in T_positions2:
            T_part2.move(before_node_position, direction)
            before_node_position = T_part2.T_position
            before_node_direction = T_part2.direction
        T_visited_part2[T_positions2[-1].T_position]  += 1

print(len(T_visited_part1))
print(len(T_visited_part2))