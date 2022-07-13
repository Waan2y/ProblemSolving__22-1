'''
input :
n k
n개 동전으로 k원 만들기

'''
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

coins = deque()
for _ in range(n):
  tmp = int(sys.stdin.readline())
  if tmp > k:
    continue
  else:
    coins.appendleft(tmp)

ans = 0
for coin in coins:
  if coin > k:
    continue
  else:
    qt = (k // coin)
    k -= (qt * coin)
    ans += qt

print(ans)
