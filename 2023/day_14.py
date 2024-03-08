from pathlib import Path
from copy import deepcopy

with open(Path("2023","day_14.txt")) as file:
    input = [[r for r in line] for line in file.read().split("\n")]


R = len(input)
C = len(input[0])

sum1 = 0
cycle = 1000000000
t = 0
cycled_grids = {}
while t != cycle:
    t += 1
    for x in range(4):
        for r in range(R):
            for c in range(C):
                if input[r][c] == 'O':
                    flag = True
                    nord = r - 1
                    previous = r
                    while flag:
                        if (0 <= nord) and (input[nord][c] != '#') and (input[nord][c] != 'O'):
                            input[nord][c] = 'O'
                            input[previous][c] = '.'
                            nord -= 1
                            previous -= 1
                        else:
                            if x == 0 and t == 1:
                                sum1 += R - previous
                            flag = False
        if x == 0 and t == 1:
            print(sum1)

        rows = len(input)
        cols = len(input[0])
        # Crea una nuova matrice vuota ruotata
        rotated_input = [['' for _ in range(rows)] for _ in range(cols)]
        # Itera attraverso la matrice originale e copia i valori nella matrice ruotata
        for i in range(rows):
            for j in range(cols):
                rotated_input[j][rows - i - 1] = input[i][j]
        input = deepcopy(rotated_input)
    
    grid = tuple(tuple(row) for row in input)
    if grid in cycled_grids:
        cycle_lenght = t - cycled_grids[grid]
        missed_cycle = (cycle - t) // cycle_lenght
        t += missed_cycle * cycle_lenght
    cycled_grids[grid] = t


sum2 = 0

for r in range(R):
    for c in range(C):
        if input[r][c] == 'O':
            sum2 += R - r

print(sum2)