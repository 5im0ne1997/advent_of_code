from pathlib import Path

with open(Path("2022","day_06.txt")) as file:
    buffer = file.readline()

part1 = False
part2 = False

for index_buffer, character in enumerate(buffer):
    marker_start_of_packet = character
    marker_start_of_message = character
    index_of_start_packet = 0
    index_of_start_message = 0
    if not part1:
        for index in range(1,4):
            if buffer[index_buffer + index] not in marker_start_of_packet:
                marker_start_of_packet = marker_start_of_packet + buffer[index_buffer + index]
                index_of_start_packet += 1
        if len(marker_start_of_packet) == 4:
            print(f"Solution1: {index_buffer + index_of_start_packet + 1}")
            part1 = True
    if not part2:
        for index in range(1,14):
            if buffer[index_buffer + index] not in marker_start_of_message:
                marker_start_of_message = marker_start_of_message + buffer[index_buffer + index]
                index_of_start_message += 1
        if len(marker_start_of_message) == 14:
            print(f"Solution2: {index_buffer + index_of_start_message + 1}")
            part2 = True
    
