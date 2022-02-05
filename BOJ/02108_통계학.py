import sys
from collections import Counter

N = int(sys.stdin.readline())
arr_ints = []

for _ in range(N):
  arr_ints.append(int(sys.stdin.readline().rstrip()))
arr_ints.sort()  # 일단 정렬해놓고 시작
# 산술평균
print(round(sum(arr_ints) / N))
#중앙값
print(arr_ints[(N-1)//2])
# 최빈값
ans = Counter(arr_ints).most_common(2)   # 일단 최빈값 두개 dict로 저장
if len(ans) == 1:                        # 최빈값이 1개 ?
  print(ans[0][0])                       # 그게 정답
else:
  if ans[0][1] == ans[1][1]:             # 두 수의 빈도가 같다 ?
    print(ans[1][0])                     # 두번째 수가 정답
  else:
    print(ans[0][0])                     # 두 수의 빈도가 다르면 첫번째 수가 정답
# 범위
if N != 1:
  print(arr_ints[-1] - arr_ints[0])
else:
  print(0)
