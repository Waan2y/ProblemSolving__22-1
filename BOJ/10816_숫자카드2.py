import sys

n = int(sys.stdin.readline())
card_set = dict()
cards = list(map(int,sys.stdin.readline().rstrip().split()))

for card in cards:
  card = str(card)
  if card in card_set.keys():
    card_set[card] += 1
  else:
    card_set[card] = 1

m = int(sys.stdin.readline())
answer_set = []
card_keys = list(map(int,sys.stdin.readline().rstrip().split()))

for keys in card_keys:
  keys = str(keys)
  if keys in card_set.keys():
    answer_set.append(card_set[keys])
  else:
    answer_set.append(0)

print(*answer_set)
