def solution(grid: list[list[str]]):
    sum_1 = 0
    sum_2 = 0

    for x, line in enumerate(grid):
        for y, ch in enumerate(line):
            found = []
            found_x = []
            if ch == "X":
                for direction in ["right", "bottom-right", "bottom", "bottom-left", "left", "upper-left", "upper", "upper-right"]:
                    string = ch
                    for iteraction in range(1,4):
                        match direction:
                            case "right":
                                if len(line) > y + iteraction:
                                    string = string + line[y+iteraction]
                            case "bottom-right":
                                if len(line) > y + iteraction and len(grid) > x + iteraction:
                                    string = string + grid[x+iteraction][y+iteraction]
                            case "bottom":
                                if len(grid) > x + iteraction:
                                    string = string + grid[x+iteraction][y]
                            case "bottom-left":
                                if 0 <= y - iteraction and len(grid) > x + iteraction:
                                    string = string + grid[x+iteraction][y-iteraction]
                            case "left":
                                if 0 <= y - iteraction:
                                    string = string + line[y-iteraction]
                            case "upper-left":
                                if 0 <= x - iteraction and 0 <= y - iteraction:
                                    string = string + grid[x-iteraction][y-iteraction]
                            case "upper":
                                if 0 <= x - iteraction:
                                    string = string + grid[x - iteraction][y]
                            case "upper-right":
                                if 0 <= x - iteraction and len(line) > y + iteraction:
                                    string = string + grid[x - iteraction][y + iteraction]
                    found.append(string)
            elif ch == "A":
                if (len(line) > y + 1 and len(grid) > x + 1) and (0 <= x - 1 and 0 <= y - 1):
                    found_x.append(sorted([ch, grid[x+1][y+1], grid[x-1][y-1]]))
                if (0 <= y - 1 and len(grid) > x + 1) and (0 <= x - 1 and len(line) > y + 1):
                    found_x.append(sorted([ch, grid[x+1][y-1], grid[x-1][y+1]]))
            else:
                continue
            sum_1 += found.count("XMAS")
            if found_x.count(sorted("MAS")) == 2:
                sum_2 += 1

    print(f"Solution part 1 is {sum_1}")
    print(f"Solution part 2 is {sum_2}")



if __name__ == "__main__":
    with open("input.txt", mode="r", encoding="UTF-8") as file:
        searching_grid = file.read().strip().split("\n")

    solution(searching_grid)
