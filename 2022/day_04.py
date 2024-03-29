from pathlib import Path

with open(Path("2022", "day_04.txt")) as file:
    input_file = [line for line in file.read().split("\n")]

sum1 = 0
sum2 = 0
for line in input_file:
    first, second = line.split(",")
    if int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]):
        sum1 += 1
        sum2 += 1
    elif int(second.split("-")[0]) >= int(first.split("-")[0]) and int(second.split("-")[1]) <= int(first.split("-")[1]):
        sum1 += 1
        sum2 += 1
    elif int(second.split("-")[0]) <= int(first.split("-")[0]) <= int(second.split("-")[1]):
        sum2 += 1
    elif int(second.split("-")[0]) <= int(first.split("-")[1]) <= int(second.split("-")[1]):
        sum2 += 1
    elif int(first.split("-")[0]) <= int(second.split("-")[0]) <= int(first.split("-")[1]):
        sum2 += 1
    elif int(first.split("-")[0]) <= int(second.split("-")[1]) <= int(first.split("-")[1]):
        sum2 += 1

print(sum1)
print(sum2)