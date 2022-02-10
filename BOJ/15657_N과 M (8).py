import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for ans in sorted(list(combinations_with_replacement(arr, M))):
  print(*ans)
