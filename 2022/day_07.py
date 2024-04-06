from pathlib import Path
from abc import ABC

with open(Path("2022","day_07.txt")) as file:
    commands = file.read().split("\n")

class FileSystem(ABC):

    def __init__(self, name: str, parent_directory: object = None, dimension: int = 0) -> None:
        self.name = name
        self.dimension = dimension
        if parent_directory == None:
            self.parent_directory = self
        else:
            self.parent_directory = parent_directory
    
    def get_parent(self) -> object:
        return self.parent_directory

class Directory(FileSystem):

    def __init__(self, name: str, parent_directory: object = None, dimension: int = 0) -> None:
        super().__init__(name, parent_directory)
        self.content = {}

    def add_content(self, name: str, content: object) -> None:
        self.content[name] = content
    
    def move_to(self, name: str) -> object:
        return self.content[name]
    
    def set_dimension(self) -> int:
        for content in self.content.values():
            self.dimension += content.set_dimension()
        return self.dimension
    
    def get_part1(self) -> int:
        part1 = 0
        for content in self.content.values():
            part1 += content.get_part1()
        if self.dimension <= 100000:
            part1 += self.dimension
        return part1

    def get_part2(self, needed_free_space: int = 0) -> int:
        part2 = []
        for content in self.content.values():
            smallest = content.get_part2(needed_free_space)
            if smallest >= needed_free_space:
                part2.append(smallest)
        if self.dimension >= needed_free_space:
            part2.append(self.dimension)
        if len(part2) > 0:
            return min(part2)
        else:
            return 0

    
class File(FileSystem):

    def __init__(self, name: str, parent_directory: object = None, dimension: int = 0) -> None:
        super().__init__(name, parent_directory, dimension)
    
    def set_dimension(self) -> int:
        return self.dimension
    
    def get_part1(self) -> int:
        return 0
    
    def get_part2(self, needed_free_space: int = 0) -> int:
        return 0

root = Directory("root")
root.add_content("/", Directory("/", root))
current_position = root

for line in commands:
    line = line.split(" ")
    if line[0] == "$" and line[1] == "cd":
        if line[2] == "..":
            current_position = current_position.get_parent()
        else:
            current_position = current_position.move_to(line[2])
    elif line[0] != "$":
        match line[0]:
            case "dir":
                current_position.add_content(line[1], Directory(line[1], current_position))
            case _:
                current_position.add_content(line[1], File(line[1], current_position, int(line[0])))


root.content["/"].set_dimension()

print(root.content["/"].get_part1())

print(root.get_part2(30000000 - (70000000 - root.content["/"].dimension)))