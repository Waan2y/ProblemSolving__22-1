import sys

N = int(sys.stdin.readline())

dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
  dp[i] = dp[i-1] + 1
  if not (i % 2):
    dp[i] = min(dp[i], dp[i // 2] + 1)
  if not (i % 3):
    dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
