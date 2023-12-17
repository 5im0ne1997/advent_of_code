with open("day_6.txt") as file:
    all_lines = file.read()

part1 = 1
part2 = 0
time , distance = all_lines.split("\n")
time = time.split(":")[1].split()
time2 = ''
for i in time:
    time2 = f"{time2}{i}"
distance = distance.split(":")[1].split()
distance2 = ''
for i in distance:
    distance2 = f"{distance2}{i}"

game = []
for g in range(len(time)):
    game.append((time[g], distance[g]))
game.append((time2, distance2))

g = 0
for t, d in game:
    g += 1
    t = int(t)
    d = int(d)
    win = 0
    for pb in range(t):
        tl = t - pb
        dt = tl * pb
        if dt > d:
            win += 1
    if g < len(game):
        part1 = part1 * win
    else:
        part2 = win
print(part1)
print(part2)
pass