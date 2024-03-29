from pathlib import Path

with open(Path("2022","day_02.txt")) as file:
    input_file = [game for game in file.read().split("\n")]

shape_to_type = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': ['rock', 0],
    'Y': ['paper', 3],
    'Z': ['scissors', 6]
}

shape_to_point = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

win_point = {
    'rock': {
        'rock': 3,
        'paper': 6,
        'scissors': 0
    },
    'paper':{
        'rock': 0,
        'paper': 3,
        'scissors': 6
    },
    'scissors':{
        'rock': 6,
        'paper': 0,
        'scissors': 3
    }
}

part1 = 0
part2 = 0
for game in input_file:
    opponent, you = game.split(" ")
    opponent_shape = shape_to_type[opponent]
    your_shape = shape_to_type[you]
    part1 += shape_to_point[your_shape[0]] + win_point[opponent_shape][your_shape[0]]

    for shape_2 in win_point[opponent_shape].items():
        if your_shape[1] == shape_2[1]:
            part2 += shape_to_point[shape_2[0]] + shape_2[1]

print(part1)
print(part2)