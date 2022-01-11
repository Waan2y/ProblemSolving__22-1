import sys

N, M, K = map(int, sys.stdin.readline().split())
cnt = 0

if(K == 0):
  print("0 0")
else:
  ans_N = K // M
  ans_M = K - M*(K // M)
  print(ans_N, ans_M)
