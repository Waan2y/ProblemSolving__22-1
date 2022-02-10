import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [ i for i in range(1, N+1)]

for ans in list(combinations(arr, M)):
  print(*ans)
