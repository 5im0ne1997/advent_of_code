import pathlib

path=pathlib.Path("2023","day_1.txt")

sum1 = 0
sum2 = 0

with open(path) as file:
    for line in file.readlines():
        list1 = []
        list2 = []
        for index, character in enumerate(line):
            if character.isdigit():
                list1.append(character)
                list2.append(character)
            for val, number  in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[index:].startswith(number):
                    list2.append(str(val+1))            
        sum1 += int(f"{list1[0]}{list1[-1]}")
        sum2 += int(f"{list2[0]}{list2[-1]}")

print(sum1)
print(sum2)