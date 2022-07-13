import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().rstrip().split())
num_set = set(map(int, sys.stdin.readline().rstrip().split()))
num_set = sorted(num_set)

answer = set(combinations_with_replacement(num_set, m))
answer = sorted(answer)

for ans in answer:
  print(*ans)
