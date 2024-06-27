from pathlib import Path
from copy import deepcopy, copy

class Grid():
    
    def __init__(self) -> None:
        self.grid = list()
        self.empty_line = ['.','.','.','.','.','.','.']
        self.rock_line = 0

    def new_rock(self, rock: list) -> None:
        for line in range(3):
            self.grid.append(copy(self.empty_line))
        self.rock_line = len(self.grid)
        for height in range(len(rock)):
            self.grid.append(copy(rock[height]))
    
    def move_rock(self, move: str) -> bool:
        if self.rock_line <= 1:
            temp_grid = deepcopy(self.grid)
        else:
            temp_grid = deepcopy(self.grid[self.rock_line-1:])
        temp2_grid = deepcopy(temp_grid)
        stop = False
        lateral_move = True

        for index_l, line in enumerate(temp_grid):
            temp_line = deepcopy(self.empty_line)
            for index_r, rock in enumerate(line):
                if rock == 'X':
                    match move:
                        case '<':
                            if 0 <= index_r - 1 and temp_grid[index_l][index_r - 1] != '#' and lateral_move == True:
                                temp_line[index_r - 1] = 'X'
                            else:
                                lateral_move = False
                                temp2_grid = deepcopy(temp_grid)

                        case '>':
                            if index_r + 1 <= len(line) - 1 and temp_grid[index_l][index_r + 1] != '#' and lateral_move == True:
                                temp_line[index_r + 1] = 'X'
                            else:
                                lateral_move = False
                                temp2_grid = deepcopy(temp_grid)
                    
                elif rock == '#':
                    temp_line[index_r] = '#'

            if stop == False and lateral_move == True:
                temp2_grid[index_l] = deepcopy(temp_line)

        temp_grid = deepcopy(temp2_grid)
        for index_l, line in enumerate(temp_grid):
            for index_r, rock in enumerate(line):
                if rock == 'X':
                    if stop == False:
                        if 0 <= index_l-1 and temp_grid[index_l - 1][index_r] != '#':
                            temp2_grid[index_l - 1][index_r] = 'X'
                            temp2_grid[index_l][index_r] = '.'
                        else:
                            stop = True
                            temp2_grid = deepcopy(temp_grid)

        if  stop == True:  
            for index_l, line in enumerate(temp_grid):
                for index_r, rock in enumerate(line):
                    if rock == 'X':
                        temp2_grid[index_l][index_r] = '#'
            if self.rock_line <= 1:
                self.grid = deepcopy(temp2_grid)
            else:
                self.grid[self.rock_line-1:] = deepcopy(temp2_grid)

        else:
            self.rock_line -= 1
            self.grid[self.rock_line:] = deepcopy(temp2_grid)

        empty = True
        while empty == True:
            if self.grid[-1] == self.empty_line:
                self.grid.pop()
            else:
                empty = False
    
        return stop

            



all_rocks = [[['.','.','X','X','X','X','.']],
             
             [['.','.','.','X','.','.','.'],
              ['.','.','X','X','X','.','.'],
              ['.','.','.','X','.','.','.']],

             [['.','.','X','X','X','.','.'],
              ['.','.','.','.','X','.','.'],
              ['.','.','.','.','X','.','.']],

             [['.','.','X','.','.','.','.'],
              ['.','.','X','.','.','.','.'],
              ['.','.','X','.','.','.','.'],
              ['.','.','X','.','.','.','.']],

             [['.','.','X','X','.','.','.'],
              ['.','.','X','X','.','.','.']]]

rock_solution = {}

with open(Path("2022","day_17.txt")) as all_moves:
    all_moves = [move for move in all_moves.read()]
    grid = Grid()
    rock_number = 1
    rock_index = 0
    grid.new_rock(all_rocks[rock_index])
    while rock_number < 1000000000001:
        for move in all_moves:
            result = grid.move_rock(move)
            if result == True:
                if rock_index < 4:
                    rock_index += 1
                else:
                    rock_index = 0
                rock_number += 1
                if rock_number == 2023:
                    print(f"Solution 1 = {len(grid.grid)}")
                    grid.new_rock(all_rocks[rock_index])
                elif rock_number == 1000000000001:
                    print(f"Solution 2 = {len(grid.grid)}")
                    break
                else:
                    grid.new_rock(all_rocks[rock_index])


pass