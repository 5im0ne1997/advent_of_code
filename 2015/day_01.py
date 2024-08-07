from pathlib import Path
from collections import Counter

with open(Path('2015','day_01.txt')) as input_file:
    moves = [c for c in input_file.read()]
    moves_count = Counter(moves)
    print(f"Solution1: {moves_count['('] - moves_count[')']}")
    position = 0
    solution2 = 0
    for move in moves:
        solution2 += 1
        if move == '(':
            position += 1
        else:
            position -= 1
        if position == -1:
            print(f"Solution2: {solution2}")
            break