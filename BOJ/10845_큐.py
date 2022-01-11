import sys

t = int(sys.stdin.readline())
que = []

for i in range(t):
  command = []
  command = list(sys.stdin.readline().split())

  if(command[0] == "push"):
    que.append(command[1])

  elif(command[0] == "pop"):
    if que:
      print(que[0])
      que.remove(que[0])
    else:
      print(-1)

  elif(command[0] == "size"):
    print(len(que))

  elif(command[0] == "empty"):
    if que:
      print(0)
    else:
      print(1)

  elif(command[0] == "front"):
    if que:
      print(que[0])
    else:
      print(-1)

  elif(command[0] == "back"):
    if que:
      print(que[len(que)-1])
    else:
      print(-1)
