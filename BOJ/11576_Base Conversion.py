import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int,input().rstrip().split())
m = int(input())
num_base_A = list(map(int, input().rstrip().split()))
num_base_A.reverse()

# A진법수 10진법으로
num_base_10 = 0
i = 0
for n in num_base_A:
    num_base_10 += (n * (A**i))
    i += 1

# 10진법수 B진법으로
num_base_B = deque()
i = 0
while num_base_10 != 0:
  num_base_B.appendleft(num_base_10 % B)
  num_base_10 //=  B

print(*num_base_B)
