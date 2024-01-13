from pathlib import Path

input = Path("2023","day_11.txt")
with open(input) as file:
    all_lines = file.read().splitlines()

empty_line = set()
empty_column = set()
galaxies = set()
for n_column in range(len(all_lines[0])):
    temp_column = set()
    for n_line, line in enumerate(all_lines):
        if len(set(line)) == 1:
            empty_line.add(n_line)
        temp_column.add(line[n_column])
        if line[n_column] == "#":
            galaxies.add((n_line, n_column))
    if len(temp_column) == 1:
        empty_column.add(n_column)
part1 = 0
part2 = 0
passed_galaxies = list()
for start_galaxy in galaxies:
    passed_galaxies.append(start_galaxy)
    for dest_galaxy in galaxies:
        if dest_galaxy not in passed_galaxies:
            galaxy_line = [start_galaxy[0],dest_galaxy[0]]
            galaxy_line.sort()
            part1 += galaxy_line[1] - galaxy_line[0]
            part2 += galaxy_line[1] - galaxy_line[0]
            for x in empty_line:
                if galaxy_line[0] < x < galaxy_line[1]:
                    part1 += 1
                    part2 += 999999
            galaxy_column = [start_galaxy[1],dest_galaxy[1]]
            galaxy_column.sort()
            part1 += galaxy_column[1] - galaxy_column[0]
            part2 += galaxy_column[1] - galaxy_column[0]
            for x in empty_column:
                if galaxy_column[0] < x < galaxy_column[1]:
                    part1 += 1
                    part2 += 999999
print(part1)
print(part2)