def solution1(group_a: list[int], group_b: list[int]):

    group_a.sort()
    group_b.sort()

    summ = 0

    for i, _ in enumerate(group_a):
        summ += abs(group_a[i] - group_b[i])

    print(f"Solution part 1 is {summ}")

def solution2(group_a: list[int], group_b: list[int]):
    summ = 0
    for number in group_a:
        summ += int(number) * group_b.count(number)
    
    print(f"Solution part 2 is {summ}")


if __name__ == "__main__":
    with open("input.txt", mode="r", encoding="UTF-8") as file:
        group_a = []
        group_b = []
        for line in file.read().strip().split("\n"):
            splitted_line = line.split("   ")
            group_a.append(int(splitted_line[0]))
            group_b.append(int(splitted_line[1]))

    solution1(group_a, group_b)
    solution2(group_a, group_b)
