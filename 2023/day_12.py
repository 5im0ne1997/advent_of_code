from pathlib import Path
import re
import copy
import math

def resolve(ds: str,dg: str, solution: str = ''):
    sum = 0
    solution = re.sub(r"\.+",".", solution)
    if 0 < len(ds):
        if ds[0] == '?':
            sum += resolve(ds[1:],dg, f"{solution}.")
            sum += resolve(ds[1:],dg, f"{solution}#")
        else:
            sum += resolve(ds[1:],dg, f"{solution}{ds[0]}")
    else:
        solution = f"{solution}."
        dg1 = dg.split(",")
        pattern = '.*'
        for i in dg1:
            pattern = f"{pattern}{'#'*int(i)}.+"
        pattern = re.sub(r"\.","\\.",pattern)
        test = re.fullmatch(f"^{pattern}", solution)
        if test:
            sum +=1

    return sum
         
part1 = 0
part2 = 0
line_counter = 0
input = Path("2023","day_12.txt")
with open(input) as file:
    for line in file.read().split("\n"):
        line_counter += 1
        print(f"RIGA: {line_counter}")
        ds, dg = line.split(" ")
        ds = re.sub(r"\.+",".", ds)
        ds_start = copy.copy(ds)
        dg_start = copy.copy(dg)
        sum1 = resolve(ds,dg)
        print(sum1)
        sum2 = resolve(f"{ds}?{ds}",f"{dg},{dg}")
        print(sum2)
        part1 += sum1
        part2 += ((sum2 / sum1)**4)*sum1

print(part1)
print(int(part2))