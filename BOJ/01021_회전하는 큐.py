import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
P = deque( i for i in range(1, N+1))
Mi = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in Mi:
  if P[0] == i:     # que의 첫 원소가 뽑을 원소임
    P.popleft()     # que에서 pop

  else:                                   # 뽑을 원소가 que 중간에 있음
    go_left = abs(P.index(i))             # 뽑을 원소와 que 맨 앞의 원소간의 거리
    go_right = abs(len(P) - P.index(i))   # 뽑을 원소와 que 맨 뒤의 원소간의 거리

    if go_left < go_right:          # 뽑을 원소가 que 앞에 가까움
      for _ in range(go_left):      # 왼쪽 이동
        P.append(P.popleft())
        cnt += 1
    else:                           # 뽑을 원소가 que 뒤에 가까움
      for _ in range(go_right):     # 왼쪽 이동
        P.appendleft(P.pop())
        cnt += 1
    P.popleft()                     # que의 첫 원소 pop

print(cnt)
