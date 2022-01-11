import sys
N = int(sys.stdin.readline())
stk = []
_out = -1

for _ in range(N):
  command = list(sys.stdin.readline().split())

  if command[0] == "push":
    stk.append(command[1])
    _out += 1

  elif command[0] == "pop":
    if _out == -1:
      print(-1)
    else:
      print(stk[_out])
      del(stk[_out])
      _out -= 1
  
  elif command[0] == "size":
    print(_out + 1)

  elif command[0] == "empty":
    if not stk:
      print(1)
    else:
      print(0)

  elif command[0] == "top":
    if _out == -1:
      print(-1)
    else:
      print(stk[_out])
