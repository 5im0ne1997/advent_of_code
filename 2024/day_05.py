from collections import defaultdict

if __name__ == "__main__":
    with open("input.txt", mode="r", encoding="UTF-8") as file:
        first_part, second_part = file.read().strip().split("\n\n")
        ordening_rules = defaultdict(list)
        for line in first_part.splitlines():
            a, b = line.split("|")
            ordening_rules[a].append(b)
        page_update = [list(line.split(",")) for line in second_part.splitlines()]
    sum_1 = 0
    for update in page_update:
        correct_update = True
        for index, page in enumerate(update):
            if page in ordening_rules:
                for related_page in ordening_rules[page]:
                    if related_page in update[:index]:
                        correct_update = False
        if correct_update:
            sum_1 += int(update[(len(update) // 2)])
    print(f"Solution 1 is {sum_1}")
