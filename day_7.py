from collections import Counter

with open("day_7.txt") as file:
    all_lines = file.read()

all_heands = all_lines.split("\n")
heands = list()
for i in all_heands:
    h, d = i.split()
    heands.append([h, d])

class Part1:
    def __init__(self, heand):
        self.heand = heand[0]
        self.bid = heand[1]

    def findheandtype(self):
        heandtype = list(Counter(self.heand).values())
        if heandtype == [1,1,1,1,1]:
            print(1)
        elif heandtype == [2,1,1,1]:
            print(2)

    
for heand in heands:
    Part1(heand).findheandtype()

