import sys
N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())
tmp = list(map(int,sys.stdin.readline().rstrip().split()))

for x in tmp:
  if x in A:    # set 은 hash table 이니까 탐색시간 O(1)
    print(1)
  else:
    print(0)
