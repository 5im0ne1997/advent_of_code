import pathlib
import re

path = pathlib.Path("2023", "day_3.txt")

all_lines = []
with open(path, "rt") as file:
    for index_line, line in enumerate(file):
        all_lines.append([])
        for index_digit, digit in enumerate(line):
            all_lines[index_line].append(digit)

sum1 = 0
for index_line , line in enumerate(all_lines):
    number = ''
    flag = False
    for index_digit, digit in enumerate(line):
        if re.match(r"\d", digit):
            try:
                ul = all_lines[index_line-1][index_digit-1]
            except:
                ul = '.'
            try:
                u = all_lines[index_line-1][index_digit]
            except:
                u = '.'
            try:
                ur = all_lines[index_line-1][index_digit+1]
            except:
                ur = '.'
            try:
                dl = all_lines[index_line+1][index_digit-1]
            except:
                dl = '.'
            try:
                d = all_lines[index_line+1][index_digit]
            except:
                d = '.'
            try:
                dr = all_lines[index_line+1][index_digit+1]
            except:
                d = '.'
            try:
                r = all_lines[index_line][index_digit+1]
            except:
                r = '.'
            try:
                l = all_lines[index_line][index_digit-1]
            except:
                l = '.'
            
            for i in [ul, u, ur, r, dr, d, dl, l]:
                if re.match(r"[^\d.]", i):
                    flag = True
            number = int(f"{number}{digit}")
        else:
            if flag:
                #print(number)
                sum1 += number
            number = ''
            flag = False

print(sum1)
                
import re
from collections import defaultdict
D = open(path).read().strip()
lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)

            


