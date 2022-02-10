import sys
from itertools import product

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for ans in sorted(list(product(arr, repeat = M))):
  print(*ans)
