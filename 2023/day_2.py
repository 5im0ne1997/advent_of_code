import pathlib
import re

path = pathlib.Path("2023", "day_2.txt")
sum1 = 0
game_counter = 0

max_cubes = {"red": 12, "green": 13, "blue": 14}

with open(path, "rt") as file:
    for line in file:
        game_counter += 1
        sub_games = re.search(":(.*)", line).group(1)
        for sub_game_cubes in sub_games.split(";"):
            fail=False
            for cubes in sub_game_cubes.split(","):
                cubes_number = re.search(r"(\d+) (\w+)", cubes)
                number = cubes_number.group(1)
                color = cubes_number.group(2)
                if (int(number) > int(max_cubes[color])):
                    fail = True
                    break
            if fail:
                break
        if not fail:
            print(game_counter)
            sum1 += game_counter

print(sum1)
