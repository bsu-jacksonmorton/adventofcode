import re
f = open("input-data.txt", "r")
ans = 0
card_instances = [0] * 187 
current_card_counter = 0
for card in f:
    card = re.sub("Card [0-9]*: ", "", card)
    w_numbers, my_numbers = card.split(" | ")
    w_numbers = re.sub("  ", " ", w_numbers).split()
    my_numbers = re.sub("  ", " ", my_numbers).split()
    matches = [num for num in w_numbers if num in my_numbers]
    for i in range(len(matches)):
        card_instances[current_card_counter + i + 1] += (1 + card_instances[current_card_counter])
    card_instances[current_card_counter] += 1

    print("current card num", current_card_counter + 1, card_instances)
    current_card_counter += 1
print(sum(card_instances))
f.close()
