ㄴimport sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  arr = list(map(int,input().rstrip().split()))
  print(sorted(arr)[-3])
