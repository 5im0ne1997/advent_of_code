from pathlib import Path

with open(Path('2025','day_02.txt')) as file:
    id_list = file.read().split(',')

solution_1 = 0

for product_id_range in id_list:
    min_range, max_range = product_id_range.split('-')
    for test_id in range(int(min_range), int(max_range) + 1):
        test_id_len = len(str(test_id))
        if str(test_id)[:test_id_len//2] == str(test_id)[test_id_len//2:]:
            solution_1 += test_id

print(solution_1)
