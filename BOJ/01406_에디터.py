import sys
from collections import deque

str_1 = deque(sys.stdin.readline().strip())
str_2 = deque()

M = int(sys.stdin.readline())

for i in range(M):
  cmd = list(sys.stdin.readline().split())

  if cmd[0] == 'L' and str_1:
    str_2.appendleft(str_1.pop())

  elif cmd[0] == 'D' and str_2:
    str_1.append(str_2.popleft())

  elif cmd[0] == 'B' and str_1:
    str_1.pop()

  elif cmd[0] == 'P':
    str_1.append(cmd[1])

print(''.join(str_1 + str_2))
