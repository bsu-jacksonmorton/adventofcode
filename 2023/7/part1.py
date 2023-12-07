from collections import Counter
from functools import cmp_to_key

HAND_TYPES = {
        "FIVE OF A KIND": 7,
        "FOUR OF A KIND": 6,
        "FULL HOUSE": 5,
        "THREE OF A KIND": 4,
        "TWO PAIR": 3,
        "ONE PAIR": 2,
        "HIGH CARD": 1
        }
CARD_TYPES = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1
        }
class Hand():
    def __init__(self, cards, hand_type, bid):
        self.cards = cards 
        self.type = hand_type
        self.bid = int(bid)
    def __repr__(self):
        return f'Hand("{self.cards}", "{self.type}", "{self.bid}")'
    def comparator(a,b):
        if a.type == b.type:
            for i in range(len(a.cards)):
                if a.cards[i] != b.cards[i]:
                    if CARD_TYPES[a.cards[i]] < CARD_TYPES[b.cards[i]]:
                        return -1
                    else:
                        return 1
        else:
            return HAND_TYPES[a.type] - HAND_TYPES[b.type]

f = open("input-data.txt", "r")
ans = 0
hands = []
for line in f:
    cards_, bid = line.split()
    hand = Counter(list(cards_))
    print("number of keys ->", len(hand.keys()))
    match len(hand.keys()):
        case 1:
            hands.append(Hand(cards_, "FIVE OF A KIND", bid))
        case 2:
            keys = list(hand.keys())
            # check for five of a kind
            if hand[keys[0]] == 4 or hand[keys[1]] == 4:
                hands.append(Hand(cards_, "FOUR OF A KIND", bid))
            # it must be a full house
            else:
                hands.append(Hand(cards_, "FULL HOUSE", bid))
        case 3:
            keys = list(hand.keys())
            if hand[keys[0]] == 3 or hand[keys[1]] == 3 or hand[keys[2]] == 3:
                hands.append(Hand(cards_, "THREE OF A KIND", bid))
            else:
                hands.append(Hand(cards_, "TWO PAIR", bid))
        case 4:
            hands.append(Hand(cards_, "ONE PAIR", bid))
        case 5:
            hands.append(Hand(cards_, "HIGH CARD", bid))

hands = sorted(hands, key=cmp_to_key(Hand.comparator))
for i in range(len(hands)):
    ans += (i + 1) * hands[i].bid
print(ans)
