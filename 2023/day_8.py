from pathlib import Path
import re
from collections import defaultdict

class Game:

    def __init__(self, input, ispart2):
        self.result = 0
        self.ispart2 = ispart2
        with open(input) as file:
            all_line = file.read()
        self.instructions, map = all_line.split("\n\n")
        map = map.split("\n")
        self.map = defaultdict(tuple)
        for x in map:
            start, rl = x.split(" = ")
            rl = re.findall(r"\w+", rl)
            self.map[start] = (rl[0], rl[1])

    def solution(self):
        position = 'AAA'
        while position != 'ZZZ':
            for i in self.instructions:
                self.result += 1
                if i == 'L':
                    step = 0
                else:
                    step = 1
                position = self.map[position][step]
                if position == 'ZZZ':
                    break
        return self.result
        


inputfile = Path("2023", "day_8.txt")
day8part1 = Game(inputfile, False)
print(day8part1.solution())

pass