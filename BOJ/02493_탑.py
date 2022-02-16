import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().rstrip().split()))
tmp = []
ans = [0] * N

for i in range(N-1, -1, -1):
  while True:
    if tmp and tops[i] > tops[tmp[-1]]:
      ans[tmp.pop()] = i+1
    else:
      tmp.append(i)
      break

print(*ans)
