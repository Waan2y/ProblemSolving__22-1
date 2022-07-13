'''
그냥수 0 1 2 3 4 5
누적합 0 1 3 6 10 14
i-j 누적합 : ls[j] = 1 to j 합 - ls[i-1]
'''
import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
ls = [0]
for i in range(1, n+1):
  ls.append(ls[i-1] + l[i-1])

for _ in range(0, m):
  i, j = map(int, sys.stdin.readline().split())
  sys.stdout.write(str(ls[j] - ls[i-1]) + '\n')
