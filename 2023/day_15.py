from pathlib import Path

with open(Path("2023","day_15.txt")) as file:
    input = file.read().split(",")
    pass

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

pass