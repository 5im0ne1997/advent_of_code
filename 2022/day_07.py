from pathlib import Path
from abc import ABC, abstractmethod

with open(Path("2022","day_07.txt")) as file:
    commands = file.read().split("\n")

class FileSystem(ABC):

    def __init__(self, name, parent_directory: str = "") -> None:
        self.name = name
        self.dimension = 0
        self.parent_directory = parent_directory

class Directory(FileSystem):

    def __init__(self, name, parent_directory) -> None:
        super().__init__(name, parent_directory)
        self.content = {}
        

class File(FileSystem):

    def __init__(self, name, parent_directory) -> None:
        super().__init__(name, parent_directory)



