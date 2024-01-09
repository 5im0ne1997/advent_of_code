from collections import defaultdict


with open("day_3.txt", "rt") as file:
    all_lines = [[c for c in line if c != '\n'] for line in file.readlines()]

file_lenght = len(all_lines)
line_lenght = len(all_lines[0])

sum1 = 0
sum2 = 0

gear_number = defaultdict(list)

for i_line in range(file_lenght):
    number = 0
    is_part = False
    gears = set()
    for i_digit in range(line_lenght+1):
        if (i_digit < line_lenght) and all_lines[i_line][i_digit].isdigit():
            number = (number * 10) + int(all_lines[i_line][i_digit])
            for lineline in [-1,0,1]:
                for digitdigit in [-1,0,1]:
                    if (0<=(i_line+lineline)<file_lenght) and (0<=(i_digit+digitdigit)<line_lenght):
                        check = all_lines[i_line+lineline][i_digit+digitdigit]
                        if (not check.isdigit()) and (check != '.'):
                            is_part = True
                        if check == '*':
                            gears.add((i_line+lineline,i_digit+digitdigit))
        elif number > 0:
            if is_part:
                sum1 += number
            for gear in gears:
                    gear_number[gear].append(number)
            is_part = False
            number = 0
            gears = set()

print(sum1)

for key,value in gear_number.items():
    if len(value)==2:
        sum2 += value[0]*value[1]

print(sum2)