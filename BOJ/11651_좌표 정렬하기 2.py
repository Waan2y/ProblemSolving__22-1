import sys

N = int(sys.stdin.readline())
loc = []

for _ in range(N):
  loc.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
loc.sort(key = lambda l: (l[1], l[0]))

for l in loc:
  print(l[0], l[1], sep = ' ')
