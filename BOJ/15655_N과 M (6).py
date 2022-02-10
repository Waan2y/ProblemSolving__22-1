import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for ans in sorted(list(combinations(arr, M))):
  print(*ans)
