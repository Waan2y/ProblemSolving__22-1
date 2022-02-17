import sys
from itertools import combinations

while True:
  exp = list(map(int,sys.stdin.readline().rstrip().split()))
  if exp[0] == 0:
    break
  else:
    S = exp[1:]
    for comb in sorted(list(combinations(S, 6))):
      print(*comb)
  sys.stdout.write('\n')
