from pathlib import Path
from functools import cache

@cache
def resolve(ds, dg, previous, index_dg, hash_number, index):
    sum = 0
    dg1 = dg.split(",")
    if index < len(ds):
        c = ds[index]
        if c == "?" and previous == '.':
            if index_dg < len(dg1):
                sum += resolve(ds, dg, "#", index_dg, 1, index +1)
            sum += resolve(ds, dg, ".", index_dg, hash_number, index +1)
        elif c == "?" and previous == '#':
            if hash_number+1 <= int(dg1[index_dg]):
                sum += resolve(ds, dg, "#", index_dg, hash_number + 1, index +1)
            if index_dg < len(dg1) and hash_number == int(dg1[index_dg]):
                sum += resolve(ds, dg, ".", index_dg + 1, 0, index +1)
        elif c == "#" and previous == '.':
            if index_dg < len(dg1):
                sum += resolve(ds, dg, "#", index_dg, 1, index +1)
        elif c == "#" and previous == '#':
            if hash_number+1 <= int(dg1[index_dg]):
                sum += resolve(ds, dg, "#", index_dg, hash_number + 1, index +1)
        elif c == '.' and previous == '.':
            sum += resolve(ds, dg, ".", index_dg, hash_number, index +1)
        elif  c == '.' and previous == '#':
            if index_dg < len(dg1) and hash_number == int(dg1[index_dg]):
                sum += resolve(ds, dg, ".", index_dg + 1, 0, index +1)
    elif index_dg == len(dg1):
        return 1
    return sum
                    
sum1 = 0
sum2 = 0
row = 0
with open(Path("2023","day_12.txt")) as file:
    for line in file.read().split("\n"):
        row += 1
        ds, dg = line.split(" ")
        for part2 in [False, True]:
            print(f"RIGA {row}")
            if part2:
                ds = f"{ds}?{ds}?{ds}?{ds}?{ds}"
                dg = f"{dg},{dg},{dg},{dg},{dg}"
                ds2 = f"{ds}."
                sum2 += resolve(ds2, dg, '.', 0, 0, 0)
            else:
                ds1 = f"{ds}."
                sum1 += resolve(ds1, dg, '.', 0, 0, 0)
        
        pass

print(sum1)
print(sum2)