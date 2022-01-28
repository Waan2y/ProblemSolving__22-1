# 규칙
# 기준은 (1, N) or (N,1)
# i 번째 기준점은
# i가 홀수일 때, (i, 1) 짝수일 때, (1, i)
# 이후 순서가 진행됨에 따라 i는 1씩 감소, 1은 1씩 증가 함
import sys

x = int(sys.stdin.readline().rstrip())  # x 번째 분수 찾기

i = 0
n = 1
while x >= n:     # x이하 제일 가까운 기준 찾기
    i += 1
    n += i
n -= i            # 찾은 기준은 n 번째 분수이고, i 번째 기준임
n = x - n         # x 와 n 사이의 간격

if (i % 2) != 0:
  a, b = i-n, 1+n
else:
  a, b = 1+n, i-n

print(a,b, sep='/')
