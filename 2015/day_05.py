from pathlib import Path
import re

with open(Path("2015","day_05.txt")) as input_file:
    strings = [s for s in input_file.read().split("\n")]

solution1 = 0
solution2 = 0
for nice_string in strings:
    if len(re.findall(r"ab|cd|pq|xy", nice_string)) == 0:
        if len(re.findall(r"[aeiou]", nice_string)) >= 3:
            if len(re.findall(r"(.)\1", nice_string)) > 0:
                solution1 += 1
    if len(re.findall(r"(..).*\1", nice_string)) > 0:
        if len(re.findall(r"(.).\1", nice_string)) > 0:
            solution2 += 1

print(f"Solution 1: {solution1}")
print(f"Solution 2: {solution2}")