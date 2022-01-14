import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
  tmp = int(sys.stdin.readline())
  if tmp != 0:
    stack.append(tmp)
  else:
    stack.pop()

print(sum(stack))
