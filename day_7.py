from collections import Counter
from collections import defaultdict

class Game:
    def __init__(self, input, ispart2):
        with open(input) as file:
            all_lines = file.read()
        all_heands = all_lines.split("\n")
        self.heands = list()
        self.ispart2 = ispart2
        for i in all_heands:
            h, d = i.split()
            h = h.replace("A", "E")
            h = h.replace("K", "D")
            h = h.replace("Q", "C")
            if self.ispart2:
                h = h.replace("J", "1")
            else:
                h = h.replace("J", "B")
            h = h.replace("T", "A")
            self.heands.append([h, d])
        self.heandtypes = defaultdict(list)
        self.solution = 0

    def findheandtype(self):
        for heand in self.heands:
            cardcount = dict(Counter(heand[0]).items())
            heandtype = list()
            for c in cardcount.values():
                heandtype.append(c)
            heandtype.sort(reverse=True)
            match heandtype:
                case [1,1,1,1,1]:
                    if self.ispart2 and "1" in cardcount:
                        ht = 2
                    else:
                        ht = 1
                case [2,1,1,1]:
                    if self.ispart2 and "1" in cardcount:
                        ht = 4
                    else:
                        ht = 2
                case [2,2,1]:
                    if self.ispart2 and "1" in cardcount:
                        if cardcount["1"] == 2:
                            ht = 6
                        elif cardcount["1"] == 1:
                            ht = 5
                    else:
                        ht = 3
                case [3,1,1]:
                    if self.ispart2 and "1" in cardcount:
                        ht = 6
                    else:
                        ht = 4
                case [3,2]:
                    if self.ispart2 and "1" in cardcount:
                        ht = 7
                    else:
                        ht = 5
                case [4,1]:
                    if self.ispart2 and "1" in cardcount:
                        ht = 7
                    else:
                        ht = 6
                case [5]:
                    ht = 7
            self.heandtypes[ht].append(heand)
        
    def resolve(self):
        self.findheandtype()
        for game in self.heandtypes:
            self.heandtypes[game].sort()
        self.heandtypes = dict(sorted(self.heandtypes.items()))
        count = 0
        for heandtype in self.heandtypes.values():
            for heand in heandtype:
                count += 1
                self.solution += int(heand[1]) * int(count)


day7part1 = Game("day_7.txt", False)
day7part1.resolve()
print(day7part1.solution)

day7part2 = Game("day_7.txt", True)
day7part2.resolve()
print(day7part2.solution)
