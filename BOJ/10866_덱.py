import sys
from collections import deque

t = int(sys.stdin.readline())
dq = deque()

for i in range(t):

  command = []
  command = list(sys.stdin.readline().split())

  if(command[0] == "push_front"):
    dq.appendleft(command[1])

  elif(command[0] == "push_back"):
    dq.append(command[1])

  elif(command[0] == "pop_front"):
    if dq:
      print(dq.popleft())
    else:
      print(-1)

  elif(command[0] == "pop_back"):
    if dq:
      print(dq.pop())
    else:
      print(-1)

  elif(command[0] == "size"):
    print(len(dq))

  elif(command[0] == "empty"):
    if dq:
      print(0)
    else:
      print(1)

  elif(command[0] == "front"):
    if dq:
      print(dq[0])
    else:
      print(-1)

  elif(command[0] == "back"):
    if dq:
      print(dq[len(dq)-1])
    else:
      print(-1)
