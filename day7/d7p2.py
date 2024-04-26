from functools import cmp_to_key

with open('input') as f:
    lines = f.read().strip().splitlines()

class hand:
    def __init__(self, cards: list[str], bid: str) -> None:
        counts = dict()
        for i in cards:
            counts[i] = counts.get(i, 0) + 1

        self.cards = cards
        self.cardMap = counts
        self.bid = int(bid)
        self.score = scoreHand(self.cardMap)

def cardToInt(card: str) -> int:
    if(card=='A'):
        return 14
    elif(card=='K'):
        return 13
    elif(card=='Q'):
        return 12
    elif(card=='J'):
        return 1
    elif(card=='T'):
        return 10
    else:
        return int(card)

def scoreHand(h: dict) -> int:
    numJokers = 0
    if 'J' in h:
        numJokers = h.pop('J')
    if(len(h) == 0):
        return 7
    maxKey = max(zip(h.values(), h.keys()))[1]

    h[maxKey] += numJokers

    n = len(h)
    if(n==1):
        # print("five of a kind")
        return 7
    elif(n==2):
        if 4 in h.values():
            # print("four of a kind")
            return 6
        # print("Full House")
        return 5
    elif(n==3):
        if 3 in h.values():
            # print("Three of a kind")
            return 4
        # print("Two pairs")
        return 3
    elif(n==4):
        # print("Pair")
        return 2
    # print("Nothin")
    return 1
    
def compareHands(h1: hand, h2: hand) -> int:
    if(h1.score > h2.score): return 1
    elif (h1.score < h2.score): return -1
    else:
        for i in range(5):
            if(cardToInt(h1.cards[i]) > cardToInt(h2.cards[i])): return 1
            elif(cardToInt(h1.cards[i]) < cardToInt(h2.cards[i])): return -1
    return -1

hands = []
for line in lines:
    cards, bid = line.split(" ")
    hands.append(hand(list(cards),bid))

sorted_hands = sorted(hands, key=cmp_to_key(compareHands))
ans=0

for i in range(len(sorted_hands)):
    ans += sorted_hands[i].bid * (i+1)

print(ans)
