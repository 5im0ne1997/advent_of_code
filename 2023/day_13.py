from pathlib import Path

with open(Path("2023","day_13.txt")) as file:
    input = [group.split("\n") for group in file.read().split("\n\n")]

for part2 in (False, True):
    sum = 0
    for group in input:
        C = len(group[0])
        R = len(group)
        for c in range(C-1):
            diff = 0
            for deltac in range(C):
                left = c - deltac
                right = c + 1 + deltac
                if 0 <= left < right < C:
                    for r in range(R):
                        if group[r][left] != group[r][right]:
                            diff += 1
            if diff == (1 if part2 else 0):
                sum += c +1
                
        for r in range(R-1):
            diff = 0
            for deltar in range(R):
                up = r - deltar
                down = r + 1 + deltar
                if 0 <= up < down < R:
                    for c in range(C):
                        if group[up][c] != group[down][c]:
                            diff += 1
            if diff == (1 if part2 else 0):
                sum += 100*(r +1)

    print(sum)