import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque( i for i in range(1, N+1))

while len(cards) != 1:
  cards.popleft()                   # 맨 위 카드 제거
  cards.append(cards.popleft())     # 그 다음 카드 맨 아래로

print(*cards)
