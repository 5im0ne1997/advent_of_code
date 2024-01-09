from pathlib import Path

class Game:

    def __init__(self, input):
        with open(input) as file:
            self.all_lines = [[number for number in line.split(" ")] for line in file.read().split("\n")]
        
        

inputfile = Path("2023", "day_9.txt")
day9part1 = Game(inputfile)

pass