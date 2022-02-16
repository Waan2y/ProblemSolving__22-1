#       ***     first answer : WA   ***
max_ans = 0
min_ans = 999999999
# 처음에는 습관적으로 max 초기값을 0으로 했는데
# 0보다 작은 값만 계산된다면, 존재하지도 않는 0이 최댓값으로 계산되어
# WA 이다.

#       ***     second answer : AC   ***
import sys
from itertools import permutations
import math
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().rstrip().split()))
cnt_oper = list(map(int, input().rstrip().split()))

oper = ""
oper += ('+' * cnt_oper[0])
oper += ('-' * cnt_oper[1])
oper += ('*' * cnt_oper[2])
oper += ('/' * cnt_oper[3])
oper = list(oper)

p_oper = set(permutations(oper, N-1))   # 가능한 모든 연산자 순열
max_ans = -math.inf
min_ans = math.inf
for oper in p_oper:
  ans = num_list[0]
  i = 1
  for op in oper:
    if op == '+':
      ans += num_list[i]
    elif op == '-':
      ans -= num_list[i]
    elif op == '*':
      ans *= num_list[i]
    else:
      if ans < 0:
        ans = ((-1 * ans) // num_list[i]) * -1
      else:
        ans //= num_list[i]
    i += 1

  max_ans = max(max_ans, ans)
  min_ans = min(min_ans, ans)

print(max_ans)
print(min_ans)
