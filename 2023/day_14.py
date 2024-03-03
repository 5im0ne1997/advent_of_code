from pathlib import Path

with open(Path("2023","day_14.txt")) as file:
    input = [[r for r in line] for line in file.read().split("\n")]


R = len(input)
C = len(input[0])

sum1 = 0
for cycle in range(1000000000):
    print(cycle)
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
                        if cycle == 0:
                            sum1 += R - previous
                        flag = False
    if cycle == 0:
        print(sum1)

    for r in range(R):
        for c in range(C):
            if input[r][c] == 'O':
                flag = True
                west = c - 1
                previous = c
                while flag:
                    if (0 <= west) and (input[r][west] != '#') and (input[r][west] != 'O'):
                        input[r][west] = 'O'
                        input[r][previous] = '.'
                        west -= 1
                        previous -= 1
                    else:
                        flag = False

    for r in range(R):
        r = R - r - 1
        for c in range(C):
            if input[r][c] == 'O':
                flag = True
                south = r + 1
                previous = r
                while flag:
                    if (R > south) and (input[south][c] != '#') and (input[south][c] != 'O'):
                        input[south][c] = 'O'
                        input[previous][c] = '.'
                        south += 1
                        previous += 1
                    else:
                        flag = False

    for r in range(R):
        for c in range(C):
            c = C - c -1
            if input[r][c] == 'O':
                flag = True
                east = r + 1
                previous = r
                while flag:
                    if (C > east) and (input[r][east] != '#') and (input[r][east] != 'O'):
                        input[r][east] = 'O'
                        input[r][previous] = '.'
                        east += 1
                        previous += 1
                    else:
                        flag = False

sum2 = 0

for r in range(R):
    for c in range(C):
        if input[r][c] == 'O':
            sum2 += R - r

print(sum2)