import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for ans in sorted(list(permutations(arr, M))):
  print(*ans)
