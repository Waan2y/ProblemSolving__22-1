import sys

A, I = map(int, sys.stdin.readline().split())
answer = (I - 1) * A + 1
print(answer)
