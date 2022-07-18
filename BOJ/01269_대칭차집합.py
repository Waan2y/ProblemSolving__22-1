import sys

nA, nB = map(int, sys.stdin.readline().rstrip().split())
A = set(map(int, sys.stdin.readline().rstrip().split()))
B = set(map(int, sys.stdin.readline().rstrip().split()))
# 포함배제의 원리
answer = (len(A)+len(B))-(len(A&B)*2)
print(answer)
