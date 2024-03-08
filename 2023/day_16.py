from pathlib import Path
from copy import deepcopy

with open(Path("2023","day_16.txt")) as file:
    input_file = [[c for c in row] for row in file.read().split("\n")]

steps = {'>': (0, 1),
         '<': (0, -1),
         'v': (1, 0),
         '^': (-1, 0)}

mirros = {('\\', '<'): '^',
          ('/', '<'): 'v',
          ('/', '>'): '^',
          ('\\', '>'): 'v',
          ('\\', 'v'): '>',
          ('/', 'v'): '<',
          ('/', '^'): '>',
          ('\\', '^'): '<'}

splitters = {('|', '<'): ('^', 'v'),
             ('|', '>'): ('^', 'v'),
             ('-', 'v'): ('<', '>'),
             ('-', '^'): ('<', '>'),
             ('|', 'v'): 'v',
             ('|', '^'): '^',
             ('-', '<'): '<',
             ('-', '>'): '>'}

R = len(input_file)
C = len(input_file[0])
temp_beam = []
solution = []
for x in range(R):
    solution.append([])
    for y in range(C):
        solution[x].append([])
temp_solution = deepcopy(solution)
def move(beam: list):
    global temp_solution
    global temp_beam
    x, y = steps[beam[0]]
    next_x = beam[1] + x
    next_y = beam[2] + y
    next_beam = []
    if (0 <= next_x < C) and (0 <= next_y < R):
        next_step = input_file[next_x][next_y]
        if (next_step,beam[0]) in mirros:
            next_beam.append((mirros[(next_step,beam[0])], next_x,next_y ))
        elif (next_step,beam[0]) in splitters:
            for d in splitters[next_step,beam[0]]:
                next_beam.append((d, next_x,next_y ))
        else:
            next_beam.append((beam[0], next_x,next_y ))

        for b in next_beam:
            if b[0] not in temp_solution[b[1]][b[2]]:
                temp_solution[b[1]][b[2]].append(b[0])
                temp_beam.append(b)
    
t = 0
sum2 = []
for direction in ['>','^','<','v']:
    step2 = []
    if direction == '>':
        for r in range(R):
            step2.append(('>', r , -1))
    elif direction == '^':
        for c in range(C):
            step2.append(('^', R , c))
    elif direction == '<':
        for r in range(R):
            step2.append(('<', C , r))
    elif direction == 'v':
        for c in range(C):
            step2.append(('v', -1 , c))
    for first in step2:
        beams = [first]
        t += 1
        while len(beams) > 0:
            temp_beam = []
            for step in beams:
                move(step)
            beams = deepcopy(temp_beam)
        sum1 = 0
        for r in range(R):
            for c in range(C):
                if len(temp_solution[r][c]) > 0:
                    sum1 += 1
                    
        if t == 1:
            print(sum1)
        sum2.append(sum1)
        temp_solution = deepcopy(solution)
    pass

print(max(sum2))