# 15의 배수 == 마지막자리 5 and 모든 자리수 합 3의 배수
# 찾은 규칙 : 마지막 자리는 무조건 5로 고정하고 남은 자리에는 1, 5 밖에 못오니까
#            각각 경우에서 자리수 합이 3의 배수가 될 때 1 갯수와 5 갯수로 경우의 수 계산해서 더함
#            이때 각각 경우의 수가 이항계수 임

import sys
from math import factorial as ft
input = sys.stdin.readline

def nCr(n:int, r:int):
  return ft(n) // (ft(r) * ft(n-r))

N = int(input())
count_1 = N-1
answer = 0

if N == 1:
  print(0)
else:
  for count_5 in range(N):
    if (count_1 + ( 5 * (count_5 +1))) % 3 == 0:
      answer += nCr(N-1, count_5)
      count_1 -= 1
    else:
      count_1 -= 1
  print(answer % 1000000007)
