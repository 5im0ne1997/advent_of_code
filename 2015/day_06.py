from pathlib import Path
import re

with open(Path("2015","day_06.txt")) as input_file:
    istructions = [row for row in input_file.read().split("\n")]

lights_grid = [[False for r in range(1000)] for l in range(1000)]
lights_grid_2 = [[0 for r in range(1000)] for l in range(1000)]
solution1 = 0
solution2 = 0
for ist in istructions:
    type, start, end = re.match(r"(^.+) (\d.+) .+. (.+\d$)", ist).groups()
    start = (int(start.split(',')[0]),int(start.split(',')[1]))
    dif_x = int(end.split(',')[0]) - start[0]
    dif_y = int(end.split(',')[1]) - start[1]
    for x in range(dif_x + 1):
        for y in range(dif_y + 1):
            match type:
                case "turn on":
                    if not lights_grid[start[0] + x][start[1] + y]:
                        solution1 += 1
                    lights_grid[start[0] + x][start[1] + y] = True
                    lights_grid_2[start[0] + x][start[1] + y] += 1
                    solution2 += 1
                case "turn off":
                    if lights_grid[start[0] + x][start[1] + y]:
                        solution1 -= 1
                    lights_grid[start[0] + x][start[1] + y] = False
                    if lights_grid_2[start[0] + x][start[1] + y] > 0:
                        lights_grid_2[start[0] + x][start[1] + y] -= 1
                        solution2 -= 1
                case "toggle":
                    if not lights_grid[start[0] + x][start[1] + y]:
                        solution1 += 1
                    elif lights_grid[start[0] + x][start[1] + y]:
                        solution1 -= 1
                    lights_grid[start[0] + x][start[1] + y] = not lights_grid[start[0] + x][start[1] + y]
                    lights_grid_2[start[0] + x][start[1] + y] += 2
                    solution2 += 2

print(f"Solution 1: {solution1}")
print(f"Solution 2: {solution2}")