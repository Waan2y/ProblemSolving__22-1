from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Q = deque()
for _ in range(N):
  cmd = list(input().rstrip().split())

  if cmd[0] == "push":
    Q.appendleft(int(cmd[1]))
  elif cmd[0] == "pop":
    if Q:
      print(Q.pop())
    else:
      print(-1)
  elif cmd[0] == "size":
    print(len(Q))
  elif cmd[0] == "empty":
    if not Q:
      print(1)
    else:
      print(0)
  elif cmd[0] == "front":
    if Q:
      print(Q[-1])
    else:
      print(-1)
  else:
    if Q:
      print(Q[0])
    else:
      print(-1)
