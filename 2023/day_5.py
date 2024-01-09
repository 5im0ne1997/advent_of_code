with open("day_5.txt") as file:
    all_lines = file.read()

parts = all_lines.split("\n\n")
seed, *maps = parts
seed_1 = seed.split(":")[1].split()
position = 0

for s in seed_1:
    actual_position = int(s)
    for single_map in maps:
        coordinates = single_map.split("\n")[1:]
        for c in coordinates:
            dst, src, rng = c.split()
            dst = int(dst)
            src = int(src)
            rng = int(rng)
            if src <= actual_position <= src+rng-1:
                actual_position = dst+(actual_position-src)
                break
    if position == 0 or position > actual_position:
        position = actual_position


print(position)

position = []
seed_2_temp = seed_1.copy()
for i in range(0, len(seed_1), 2):
    range_seed = int(seed_2_temp.pop())
    start_seed = int(seed_2_temp.pop())
    R = [(start_seed, start_seed + range_seed)]
    for single_map in maps:
        coordinates = single_map.split("\n")[1:]
        A = []
        for c in coordinates:
            dst, src, rng = c.split()
            dst = int(dst)
            src = int(src)
            rng = int(rng)
            src_end = src + rng
            NR = []
            while R:
                (st,ed) = R.pop()
                before = (st,min(ed,src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1]>before[0]:
                    NR.append(before)
                if inter[1]>inter[0]:
                    A.append((inter[0]-src+dst, inter[1]-src+dst))
                if after[1]>after[0]:
                    NR.append(after)
            R = NR
        R = A+R
    position.append(min(R)[0])

print(min(position))


pass



