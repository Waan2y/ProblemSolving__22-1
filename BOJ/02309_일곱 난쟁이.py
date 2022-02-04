import sys
from itertools import combinations

K = []
ans = []
for _ in range(9):
  K.append( int(sys.stdin.readline()))

combs_K = list(combinations(K, 7))
for c in combs_K:
  if sum(c) == 100:
    ans = list(c)

ans.sort()
for i in ans:
  print(i)
