from pathlib import Path
from collections import defaultdict

with open(Path("2023","day_15.txt")) as file:
    input = file.read().split(",")

all_string = {}
for string in input:
    if string in all_string:
        all_string[string] += 1
    else:
        all_string[string] = 1

sum1 = 0
for row in all_string.items():
    temp_sum = 0
    for c in row[0]:
        temp_sum += ord(c)
        temp_sum = temp_sum * 17
        temp_sum = temp_sum % 256
    sum1 += temp_sum * row[1]

print(sum1)
t = 0
boxes = defaultdict(list)
for lens in input:
    t += 1
    print(t)
    box_number = 0
    lens_tag = ['', 0]
    for c in lens:
        if c == '=':
            lens_tag[1] = lens[-1]
            break
        elif c == '-':
            lens_tag[1] = c
        else:
            box_number += ord(c)
            box_number = box_number * 17
            box_number = box_number % 256
            lens_tag[0] = f'{lens_tag[0]}{c}'
    lens_tag = tuple(lens_tag)
    if box_number in boxes:
        if lens_tag[1] == '-':
            for l in enumerate(boxes[box_number]):
                if l[1][0] == lens_tag[0]:
                    boxes[box_number].pop(l[0])
                    break
        else:
            added = False
            for l in enumerate(boxes[box_number]):
                if l[1][0] == lens_tag[0]:
                    added = True
                    boxes[box_number][l[0]] = lens_tag
                    break
            if added == False:
                boxes[box_number].append(lens_tag)
    elif lens_tag[1] != '-':
        boxes[box_number].append(lens_tag)
pass
sum2 = 0
for boxes in boxes.items():
    box_number = boxes[0]
    for lens in enumerate(boxes[1]):
        sum2 += ((box_number + 1) * (lens[0] + 1) * int(lens[1][1]))
print(sum2)

pass