import sys
input = sys.stdin.readline

# sigma (0 - n-1)
def sigma(n : int):
  answer = 0
  for i in range(n):
    answer += i
  return answer

# 찾은 규칙
# 연속 구간 시작수 n
# n n+1 n+2 ...
# L*n = N - sigma(L-1)
# n = N - sigma(L-1) / L

N, L = map(int, input().rstrip().split())

N -= sigma(L)
while True:
  if L > 100 or N < 0:
    L = 1
    answer = -1
    break

  elif N % L == 0:
    answer = N // L
    break

  else:
    N -= L
    L += 1

for _ in range(L):
  print(answer, end = " ")
  answer += 1
