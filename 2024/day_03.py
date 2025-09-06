def solution(input_memory: str):
    mul_found = False
    position_mul_found = 0
    first_oper = ""
    second_opr = ""
    separator_found = False
    mul_close = False

    sum_1 = 0

    for i, ch in enumerate(input_memory):
        if input_memory[i:].startswith("mul(") and not mul_found:
            mul_found = True
            position_mul_found = 0
        elif mul_found and position_mul_found < 3:
            position_mul_found += 1
        elif mul_found and position_mul_found == 3:
            if ch.isdigit():
                if not separator_found:
                    first_oper = first_oper + ch
                else:
                    second_opr = second_opr + ch
            elif ch == "," and first_oper:
                separator_found = True
            elif ch == ")" and first_oper and second_opr and separator_found:
                mul_close = True
            else:
                mul_found = False

        if mul_found and first_oper and separator_found and second_opr and mul_close:
            sum_1 += int(first_oper) * int(second_opr)
            mul_found = False

        if not mul_found:
            position_mul_found = 0
            first_oper = ""
            second_opr = ""
            separator_found = False
            mul_close = False

    print(f"Solution part 1 is {sum_1}")


if __name__ == "__main__":

    with open("input.txt", mode="r", encoding="UTF-8") as file:
        corrupted_memory = file.read().strip()

    solution(input_memory=corrupted_memory)
