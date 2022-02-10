import sys
from itertools import product

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [ i for i in range(1, N+1)]

for ans in list(product(arr, repeat = M)):
  print(*ans)
