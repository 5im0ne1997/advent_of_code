from pathlib import Path

moves = [move for move in open(Path("2021","day_02.txt")).read().split("\n")]

h_pos = 0
d_pos = 0

aim_pos = 0
h2_pos = 0
d2_pos = 0

for move in moves:
    direction, distance = move.split(" ")

    match direction:
        case "forward":
            h_pos += int(distance)
            h2_pos += int(distance)
            d2_pos += int(distance) * aim_pos
        case "down":
            d_pos += int(distance)
            aim_pos += int(distance)
        case "up":
            d_pos -= int(distance)
            aim_pos -= int(distance)

print(f"Solution 1: {h_pos * d_pos}")
print(f"Solution 2: {h2_pos * d2_pos}")