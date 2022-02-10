import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [ i for i in range(1, N+1)]

for ans in list(combinations_with_replacement(arr, M)):
  print(*ans)
