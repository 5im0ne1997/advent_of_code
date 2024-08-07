from pathlib import Path
from collections import defaultdict

move_type = {'^': (1,0),
             'v': (-1,0),
             '<': (0,-1),
             '>': (0,1)}

visited_house_1 = defaultdict(int)
santa_position_1 = (0,0)
visited_house_1[santa_position_1] += 1

visited_house_2 = defaultdict(int)
santa_position_2 = (0,0)
robosanta_position_2 = (0,0)
visited_house_2[santa_position_2] += 1

with open(Path('2015','day_03.txt')) as input_file:
    moves = [m for m in input_file.read()]
    for index, move in enumerate(moves):
        santa_position_1 = (santa_position_1[0] + move_type[move][0],santa_position_1[1] + move_type[move][1])
        visited_house_1[santa_position_1] += 1
        if index % 2 == 0:
            santa_position_2 = (santa_position_2[0] + move_type[move][0],santa_position_2[1] + move_type[move][1])
            visited_house_2[santa_position_2] += 1
        else:
            robosanta_position_2 = (robosanta_position_2[0] + move_type[move][0],robosanta_position_2[1] + move_type[move][1])
            visited_house_2[robosanta_position_2] += 1
    print(f"Solution1: {len(visited_house_1)}")
    print(f"Solution2: {len(visited_house_2)}")