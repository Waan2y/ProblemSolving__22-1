import sys

L, P = map(int, sys.stdin.readline().split())
article = list(map(int, sys.stdin.readline().split()))

for i in range(5):
  print(article[i] - L*P, end = " ")
