from pathlib import Path

inputfile = Path("2023", "day_10.txt")
with open(inputfile) as file:
    input = [[c for c in line] for line in file.read().split("\n")]

L = len(input)
C = len(input[0])

move = {
    "^": (-1, 0),
    ">": (0, 1),
    "V": (1, 0),
    "<": (0, -1)
}

pipe = {
    ("|", "^"): "^",
    ("|", "V"): "V",
    ("-", ">"): ">",
    ("-", "<"): "<",
    ("F", "<"): "V",
    ("F", "^"): ">",
    ("7", ">"): "V",
    ("7", "^"): "<",
    ("L", "V"): ">",
    ("L", "<"): "^",
    ("J", "V"): "<",
    ("J", ">"): "^"
}

for i, c in enumerate(input):
    for ii, cc in enumerate(input[i]):
        if cc == "S":
            s_position = [i, ii]

for firststep in pipe.items():
    step = 1
    position = [s_position[0] + move[firststep[1]][0],s_position[1] + move[firststep[1]][1]]
    next_pipe = (input[position[0]][position[1]], firststep[1])
    flag = True
    while flag:
        if (next_pipe in pipe) and (0<=position[0]<=L) and (0<=position[1]<=C):
            step += 1
            position = [position[0] + move[pipe[next_pipe]][0],position[1] + move[pipe[next_pipe]][1]]
            next_pipe = (input[position[0]][position[1]], pipe[next_pipe])
        else:
            flag = False
    if next_pipe[0] =="S":
        print(int(step / 2))
        break
