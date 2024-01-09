from pathlib import Path
from itertools import pairwise

class Game:

    def __init__(self, input, ispart2):
        with open(input) as file:
            self.all_lines = [[number for number in line.split(" ")] for line in file.read().split("\n")]
        self.sum = 0
        self.ispart2 = ispart2

    def solution(self):
        for line in self.all_lines:
            if self.ispart2:
                line.reverse()
            flag = True
            while flag:
                newline = list()
                self.sum += int(line[-1])
                for a,b in list(pairwise(line)):
                    newline.append(int(b) - int(a))
                
                test = 0 in set(newline)
                if len(set(newline)) == 1 and 0 in set(newline):
                    flag = False
                line = newline
        print(self.sum)

inputfile = Path("2023", "day_9.txt")
day9part1 = Game(inputfile, False)
day9part1.solution()

day9part2 = Game(inputfile, True)
day9part2.solution()
