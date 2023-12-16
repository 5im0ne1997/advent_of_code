import re

sum1 = 0
sum2=0
game_counter = 0

max_cubes = {"red": 12, "green": 13, "blue": 14}

with open("day_2.txt", "rt") as file:
    for line in file:
        game_counter += 1
        sub_games = re.search(":(.*)", line).group(1)
        game_max_cubes={"red": 0, "green": 0, "blue": 0}
        for sub_game_cubes in sub_games.split(";"):
            for cubes in sub_game_cubes.split(","):
                cubes_number = re.search(r"(\d+) (\w+)", cubes)
                number = int(cubes_number.group(1))
                color = cubes_number.group(2)
                if (number > game_max_cubes[color]):
                    game_max_cubes[color] = number
        if (game_max_cubes["red"] <= max_cubes["red"]) and  (game_max_cubes["green"] <= max_cubes["green"]) and (game_max_cubes["blue"] <= max_cubes["blue"]):
            sum1 += game_counter
        sum2 += (game_max_cubes["red"] * game_max_cubes["green"]) * game_max_cubes["blue"]
        


print(sum1)
print(sum2)
