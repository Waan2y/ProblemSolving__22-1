import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
ans = []
tmp = 0
for Ai in A:
  tmp += Ai
  ans.append(tmp)
print(sum(ans))
