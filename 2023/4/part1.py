import re
f = open("input-data.txt", "r")
ans = 0
for card in f:
    card = re.sub("Card [0-9]*: ", "", card)
    w_numbers, my_numbers = card.split(" | ")
    w_numbers = re.sub("  ", " ", w_numbers).split()
    my_numbers = re.sub("  ", " ", my_numbers).split()
    points = 0
    matches = [num for num in w_numbers if num in my_numbers]
    print(matches)
    for match in matches:
        if points == 0:
            points = 1
        else:
            points = points * 2
    ans += points

print(ans)
f.close()
