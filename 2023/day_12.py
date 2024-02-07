from pathlib import Path
from copy import deepcopy

def resolve(ds, dg):
    ds = ds
    dg = dg
    solution = {}
    if len(solution) == 0:
        #solution = {("matching string", index dg, number of #): "previous c"}
        solution = {(".", 0, 0, 0): "."}
    for c in ds:
        temp = deepcopy(solution)
        for s in temp.items():
            #s = ((".", 0, 0), ".")
            if c == "?" and s[1][0] == '.':
                del solution[s[0]]
                solution[(f"{s[0][0]}#", s[0][1] + 1, 1)] = '#'
                solution[(f"{s[0][0]}.", s[0][1], s[0][2])] = '.'
            elif c == "?" and s[1][0] == '#':
                del solution[s[0]]
                if s[0][1] <= len(dg):
                    if s[0][2] == int(dg[s[0][1]-1]):
                        solution[(f"{s[0][0]}.", s[0][1], 0)] = '.'
                    elif s[0][2] <= int(dg[s[0][1]-1]):
                        solution[(f"{s[0][0]}#", s[0][1], s[0][2] +1 )] = '#'
            elif c == "#" and s[1][0] == '.':
                del solution[s[0]]
                solution[(f"{s[0][0]}#", s[0][1] + 1, 1)] = '#'
            elif c == "#" and s[1][0] == '#':
                del solution[s[0]]
                if s[0][1] <= len(dg):
                    if s[0][2] <= int(dg[s[0][1]-1]):
                        solution[(f"{s[0][0]}#", s[0][1], s[0][2] +1 )] = '#'
            elif c == '.' and s[1][0] == '.':
                del solution[s[0]]
                solution[(f"{s[0][0]}.", s[0][1], s[0][2])] = '.'
            elif  c == '.' and s[1][0] == '#':
                del solution[s[0]]
                if s[0][1] <= len(dg):
                    if s[0][2] == int(dg[s[0][1] - 1]):
                        solution[(f"{s[0][0]}.", s[0][1], 0)] = '.'
    return len(solution)
                    


sum1 = 0
with open(Path("2023","day_12.txt")) as file:
    for line in file.read().split("\n"):
        ds, dg = line.split(" ")
        ds = f"{ds}."
        dg = dg.split(",")
        sum1 += resolve(ds, dg)
        pass
    print(sum1)