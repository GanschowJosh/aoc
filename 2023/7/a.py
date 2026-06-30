from collections import Counter

with open(input(), "r") as f:
  lines = f.readlines()

hands = []
for line in lines:
  cards, bid = line.split()
  hands.append((cards, int(bid)))

card_order = "23456789TJQKA"
card_rank = {ch: i for i, ch in enumerate(card_order)}

def hand_type(cards):
  c = sorted(Counter(cards).values(), reverse=True)

  if c == [5]:
    return 6
  if c == [4, 1]:
    return 5
  if c == [3, 2]:
    return 4
  if c == [3, 1, 1]:
    return 3
  if c == [2, 2, 1]:
    return 2
  if c == [2, 1, 1, 1]:
    return 1
  return 0

def hand_key(hand):
  cards, bid = hand
  return (
    hand_type(cards),
    [card_rank[ch] for ch in cards]
  )

hands.sort(key=hand_key)

total = 0
for i, (cards, bid) in enumerate(hands, start=1):
  total += i * bid

print(total)