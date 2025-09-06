from itertools import pairwise

def solution(levels: list[list[int]]):
    summ_1 = 0
    summ_2 = 0

    for single_level in levels:
        if is_level_safe(single_level):
            summ_1 += 1
            summ_2 += 1
        else:
            for i, _ in enumerate(single_level):
                single_level_copy = single_level.copy()
                single_level_copy.pop(i)
                if is_level_safe(single_level_copy):
                    summ_2 += 1
                    break

    print(f"Solution part 1 is {summ_1}")
    print(f"Solution part 2 is {summ_2}")

def is_level_safe(level: list[int])-> bool:
    ascending = False
    descending = False
    is_safe = False
    for couple in pairwise(level):
        test = couple[0] - couple[1]
        if test != 0 and (1 <= abs(test) <= 3):
            if test > 0:
                descending = True
            else:
                ascending = True
            if (ascending and descending) or (not ascending and not descending):
                is_safe = False
            else:
                is_safe = True
        else:
            is_safe = False
            break
    return is_safe

if __name__ == "__main__":
    with open("input.txt", mode="r", encoding="UTF-8") as file:
        levels = [[int(level) for level in line.split(" ")] for line in file.read().strip().split("\n")]

    solution(levels)
