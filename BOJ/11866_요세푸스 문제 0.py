# 삭제되는 애는 pop 하고
# 나머지는 원형 que 처럼
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
P = deque( i for i in range(1, N+1))

i = 0
sys.stdout.write('<')
while len(P) != 1:
  if i == K:
    sys.stdout.write('%d, ' %P.pop())
    i = 0
  else:
    P.append(P.popleft())
    i += 1
sys.stdout.write('%d>' %P[0])
