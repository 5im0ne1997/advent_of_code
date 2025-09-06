from collections import defaultdict

def check_correct_update(update: list[str]):
    for index, page in enumerate(update):
        if page in ORDENING_RULES:
            for related_page in ORDENING_RULES[page]:
                if related_page in update[:index]:
                    return False
    return True

with open("input.txt", mode="r", encoding="UTF-8") as file:
    first_part, second_part = file.read().strip().split("\n\n")
    ORDENING_RULES = defaultdict(list)
    for line in first_part.splitlines():
        a, b = line.split("|")
        ORDENING_RULES[a].append(b)
    PAGE_UPDATE = [list(line.split(",")) for line in second_part.splitlines()]
SUM_1 = 0
for update in PAGE_UPDATE:
    if check_correct_update(update):
        SUM_1 += int(update[(len(update) // 2)])
print(f"Solution 1 is {SUM_1}")
