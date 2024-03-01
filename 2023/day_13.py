from pathlib import Path
from collections import defaultdict
from itertools import batched

def resolve(input,vertical):
    if vertical == True:
        multip = 1
    else:
        multip = 100
    sum = 0
    middle = defaultdict(list)
    for iDiGroup in enumerate(input):
        previous_line = (0, "")
        for iDiLine in enumerate(iDiGroup[1]):
            if iDiLine[1] == previous_line[1]:
                middle[iDiGroup[0]].append(previous_line)
                middle[iDiGroup[0]].append(iDiLine)
            else:
                previous_line = iDiLine

    for mirror in middle.items():
        group = input[mirror[0]]
        flag = True
        while flag:
            for test in batched(mirror[1], 2):
                mirrored = 2
                first = test[0][0]
                last = test[1][0]
                flag_2 = True
                while flag_2:
                    if (0 <= int(first) -1) and (int(last) +1 < len(group)):
                        if group[int(first) -1] == group[int(last) +1]:
                            mirrored += 1
                            first -= 1
                            last += 1
                        else:
                            mirrored = 0
                            flag_2 = False
                    else:
                        flag_2 = False
                if mirrored != 0:
                    flag = False
            flag = False
        sum += multip*mirrored
    return sum

with open(Path("2023","day_13.txt")) as file:
    input = [group.split("\n") for group in file.read().split("\n\n")]

sum1 = 0
sum1 += resolve(input, False)

input_invert = list()
for group in enumerate(input):
    temp = list()
    for i in range(len(group[1][0])):
        temp.append("")
    input_invert.append(temp)
    for l in group[1]:
        for c in enumerate(l):
            input_invert[group[0]][c[0]] = f"{input_invert[group[0]][c[0]]}{c[1]}"

sum1 += resolve(input_invert, True)
print(sum1)
