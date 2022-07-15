import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n    # idx 까지 만들수 있는 LIS
for i in range(1, n): # 지금순서
  for j in range(0, i): # 이전전부
    if A[i] > A[j]:
      dp[i] = dp[j]+1 if dp[i] < dp[j]+1 else dp[i]


print(max(dp))
