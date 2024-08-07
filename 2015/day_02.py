from pathlib import Path

with open(Path('2015','day_02.txt')) as input_file:
    all_present = [[int(d) for d in p.split('x')] for p in input_file.read().split('\n')]
    solution1 = 0
    solution2 = 0
    for present in all_present:
        present.sort()
        face_area = [present[0] * present[1], present[0] * present[2], present[1] * present[2]]
        solution1 += ((face_area[0] + face_area[1] + face_area[2]) * 2) + min(face_area)
        solution2 += ((present[0] + present[1]) * 2) + (present[0] * present[1] * present[2])
    print(f"Solution1: {solution1}")
    print(f"Solution2: {solution2}")
