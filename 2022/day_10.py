from pathlib import Path

with open(Path("2022","day_10.txt")) as file:
    program = file.read().split("\n")

cycle = 0
X = 1

sum1 = 0
sprite_pos = X - 1  
partial_CRT = ''
CRT_pos = 0


def solution_1(cycle_n):
    global X
    global sum1
    if cycle_n == 20 or cycle_n == 60 or cycle_n == 100 or cycle_n == 140 or cycle_n == 180 or cycle_n == 220:
        sum1 += cycle_n * X

def solution_2(partial_CRT,X):
    global CRT_pos
    sprite_pos = X - 1
    if sprite_pos <= CRT_pos <= (sprite_pos + 2):
        new_CRT = '#'
    else:
        new_CRT = ' '
    if ((CRT_pos+1) % 40) == 0:
        print(f'{partial_CRT}{new_CRT}')
        CRT_pos = 0
        return ''
    CRT_pos += 1
    return f'{partial_CRT}{new_CRT}'
    

for line in program:
    if line == "noop":
        cycle += 1
        solution_1(cycle)
        partial_CRT = solution_2(partial_CRT, X)
    else:
        for n in range(2):
            cycle += 1
            if n == 0:
                solution_1(cycle)
                partial_CRT = solution_2(partial_CRT, X)
            else:
                solution_1(cycle)
                partial_CRT = solution_2(partial_CRT, X)
                X += int(line.split(" ")[1])

print(f'Solution1: {sum1}')
