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
    input2 = [x[:] for x in input]
    step = 1
    position = [s_position[0] + move[firststep[1]][0],s_position[1] + move[firststep[1]][1]]
    next_pipe = (input[position[0]][position[1]], firststep[1])
    flag = True
    while flag:
        if (next_pipe in pipe) and (0<=position[0]<=L) and (0<=position[1]<=C):
            step += 1
            input2[position[0]][position[1]] = next_pipe
            position = [position[0] + move[pipe[next_pipe]][0],position[1] + move[pipe[next_pipe]][1]]
            next_pipe = (input[position[0]][position[1]], pipe[next_pipe])
        else:
            flag = False
    if next_pipe[0] =="S":
        input2[position[0]][position[1]] = next_pipe
        print(int(step / 2))
        break

for i2, c2 in enumerate(input2):
    for ii2, cc2 in enumerate(input2[i2]):
        if (type(input2[i2][ii2]) is not type(tuple())):
            input2[i2][ii2] = "."
for x in ["|","-","F","7","L","J"]:
    s_pipe = ((x,next_pipe[1]),firststep[1])
    for xx in pipe.items():
        if s_pipe == xx:
            input2[s_position[0]][s_position[1]] = s_pipe[0]

step2 = 0
for i2, c2 in enumerate(input2):
    for ii2, cc2 in enumerate(input2[i2]):
        if 0 <= ii2 < C:
            if cc2 == '.':
                flag = 0
                wallcount = 0
                wallcheck = input2[i2][ii2+1:]
                for wall in wallcheck:
                    if type(wall) is type(tuple()):
                        if wall[0] == "|":
                            wallcount += 1
                            flag = 0
                        elif wall[0] == "-":
                            pass
                        elif wall[0] == "F" or wall[0] == "7":
                            flag += 1
                            if flag == 4:
                                wallcount += 1
                                flag = 0
                            elif flag == 2:
                                flag = 0
                        elif wall[0] == "L" or wall[0] == "J":
                            flag += 3
                            if flag == 4:
                                wallcount += 1
                                flag = 0
                            elif flag == 6:
                                flag = 0
                if (wallcount % 2) != 0:
                    step2 += 1

print(step2)