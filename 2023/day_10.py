from pathlib import Path

inputfile = Path("2023", "day_10.txt")
with open(inputfile) as file:
    input = [[c for c in line] for line in file.read().split("\n")]

for i, c in enumerate(input):
    for ii, cc in enumerate(input[i]):
        if cc == "S":
            s_position = (i, ii)

pipes = (
{"|": ("u","d")},
{"-": ("r","l")},
{"L": ("u","r")},
{"J": ("u","l")},
{"7": ("d","l")},
{"F": ("d","r")}
)

