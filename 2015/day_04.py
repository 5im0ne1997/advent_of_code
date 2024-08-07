from hashlib import md5
from pathlib import Path

with open(Path("2015","day_04.txt")) as input_file:
    secret_key = input_file.read()
    solution = 0
    counter = 0
    resolved1 = False
    resolved2 = False
    while True :
        secret_MD5 = md5(f"{secret_key}{counter}".encode())
        if secret_MD5.hexdigest().startswith("00000") and not resolved1:
            print(f"Solution 1: {counter}")
            resolved1 = True
        if secret_MD5.hexdigest().startswith("000000") and not resolved2:
            print(f"Solution 2: {counter}")
            resolved2 = True
        counter += 1
        if resolved1 and resolved2:
            break
        