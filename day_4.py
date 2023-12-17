import re

sum1 = 0
sum2 = 0
card = 0
all_cards = {}
with open("day_4.txt") as file:
    for line in file.readlines():
        card += 1
        win = 0
        win_n = 0
        if card in all_cards:
            all_cards[card] += 1
        else:
            all_cards[card] = 1
        numbers = re.search(r"^.*: (.*) \| (.*)", line)
        winning_number = re.findall(r"\d+" ,numbers.group(1))
        number_you_have = re.findall(r"\d+" ,numbers.group(2))
        for number in number_you_have:
            if number in winning_number:
                if win == 0:
                    win = 1
                else:
                    win = win * 2
                win_n += 1
        if win_n > 0:
            for n in range(win_n):
                if (card + n + 1) in all_cards:
                    all_cards[card + n + 1] += all_cards[card]
                else:
                    all_cards[card + n + 1] = all_cards[card]


        sum1 += win

for c, w_c in all_cards.items():
    sum2 += w_c

print(sum1)
print(sum2)