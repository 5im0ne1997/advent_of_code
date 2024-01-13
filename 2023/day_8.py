from pathlib import Path
import re
from math import lcm

class Game:

    def __init__(self, input, ispart2):
        self.result = dict()
        self.ispart2 = ispart2
        self.startpositions = list()
        with open(input) as file:
            all_line = file.read()
        self.instructions, map = all_line.split("\n\n")
        map = map.split("\n")
        self.map = dict()
        for x in map:
            start, rl = x.split(" = ")
            rl = re.findall(r"\w+", rl)
            self.map[start] = (rl[0], rl[1])

    def findallstartpositions(self):
        if self.ispart2:
            for step in self.map.keys():
                if step.endswith("A"):
                    self.startpositions.append(step)

    def solution(self):
        if self.ispart2:
            self.findallstartpositions()
        else:
            self.startpositions.append('AAA')
        for index, position in enumerate(self.startpositions):
            self.result[index] = 0
            while True:
                if self.ispart2 and position.endswith("Z"):
                    break
                elif position == "ZZZ":
                    break
                for i in self.instructions:
                    self.result[index] += 1
                    if i == 'L':
                        step = 0
                    else:
                        step = 1
                    position = self.map[position][step]
                    if self.ispart2 and position.endswith("Z"):
                        break
                    elif position == "ZZZ":
                        break
        if self.ispart2:
            results = list(self.result.values())
            return lcm(*results)
        else:
            return self.result[0]
        


inputfile = Path("2023", "day_8.txt")

day8part1 = Game(inputfile, False)
print(day8part1.solution())

day8part2 = Game(inputfile, True)
print(day8part2.solution())

pass