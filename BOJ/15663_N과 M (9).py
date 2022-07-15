import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
num_list.sort()

a = dict()
for comb in permutations(num_list, m):
  a[comb] = 1
for i in a.keys():
  print(*i)
