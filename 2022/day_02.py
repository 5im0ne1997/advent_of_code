from pathlib import Path

with open(Path("2022","day_02.txt")) as file:
    input_file = [game for game in file.read().split("\n")]

shape_to_type= {
    'A': ['rock', 1],
    'B': ['paper', 2],
    'C': ['scissors', 3],
    'X': ['rock', 1],
    'Y': ['paper', 2],
    'Z': ['scissors', 3]
}

win_point = {
    'rock': {
        'rock': 3,
        'paper': 0,
        'scissors': 6
    },
    'paper':{
        'rock': 6,
        'paper': 3,
        'scissors': 0
    },
    'scissors':{
        'rock': 0,
        'paper': 6,
        'scissors': 3
    }
}
part1 = 0
for game in input_file:
    opponent, you = game.split(" ")
    opponent_shape = shape_to_type[opponent]
    your_shape = shape_to_type[you]
    part1 += your_shape[1] + win_point[your_shape[0]][opponent_shape[0]]

print(part1)