import pathlib
import re

path = pathlib.Path("2023", "day_3.txt")

with open(path, "rt") as file:
    all_lines = [[c for c in line if c != '\n'] for line in file.readlines()]

file_lenght = (len(all_lines) -1)
line_lenght = (len(all_lines[0]) -1) 

sum1 = 0
search = re.compile(r"[^0-9.]")

for index_line , line in enumerate(all_lines):
    number = 0
    flag = False
    is_last = False
    for index_digit, digit in enumerate(line):
        if re.match(r"[0-9]", digit):
            number = (number * 10) + int(digit)
            if (index_line > 0) and (index_line < file_lenght):
                if search.match(all_lines[index_line-1][index_digit]) or search.match(all_lines[index_line+1][index_digit]): #in alto e in basso
                    flag = True
                if index_digit > 0:
                    if search.match(all_lines[index_line-1][index_digit-1]) or search.match(all_lines[index_line][index_digit-1]) or search.match(all_lines[index_line+1][index_digit-1]): #in alto a sinistra, sinistra e in basso a sinistra
                        flag = True                    
                if index_digit < line_lenght:
                    if search.match(all_lines[index_line-1][index_digit+1]) or search.match(all_lines[index_line][index_digit+1]) or search.match(all_lines[index_line+1][index_digit+1]): #in alto a destra, destra e in basso a destra
                        flag = True
            else:
                if index_line == 0:
                    if search.match(all_lines[index_line+1][index_digit]): #in basso
                        flag = True
                    if index_digit > 0:
                        if search.match(all_lines[index_line+1][index_digit-1]) or search.match(all_lines[index_line][index_digit-1]): #in basso a sinistra e sinistra
                            flag = True                    
                    if index_digit < line_lenght:
                        if search.match(all_lines[index_line+1][index_digit+1]) or search.match(all_lines[index_line][index_digit+1]): #in basso a destra e destra
                            flag = True
                else:
                    if search.match(all_lines[index_line-1][index_digit]): #in alto
                        flag = True
                    if index_digit > 0:
                        if search.match(all_lines[index_line-1][index_digit-1]) or search.match(all_lines[index_line][index_digit-1]): #in alto a sinistra e sinistra
                            flag = True                    
                    if index_digit < line_lenght:
                        if search.match(all_lines[index_line-1][index_digit+1]) or search.match(all_lines[index_line][index_digit+1]): #in alto a destra e destra
                            flag = True
            if index_digit == line_lenght:
                is_last = True
        else:
            if flag:
                sum1 += number
            flag = False
            number = 0
    if flag and is_last:
        sum1 += number      

print(sum1)

