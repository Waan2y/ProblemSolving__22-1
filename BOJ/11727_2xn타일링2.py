'''
D[1] = 1
D[2] = 3
D[3] =

n-1 | 2x1 결정임 무조건
ㅁㅁ | ㅁ
ㅁㅁ | ㅁ

n-2 | 이건 1x2 2개 or 2x2 1개도 가능임
ㅁㅁ | ㅁㅁ
ㅁㅁ | ㅁㅁ

D[n] = D[n-1] + D[n-2]*2 ?
'''

import sys

dp = [0] * 1001
dp[1] = 1
dp[2] = 3
n = int(sys.stdin.readline())

for i in range(3, n+1):
  dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007

print(dp[n])
