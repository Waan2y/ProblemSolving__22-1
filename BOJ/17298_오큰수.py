# 수열과 stack를 최신화 하지 않고
# index로 받아서 stack에 저장
import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))

tA = [0]           # 검사할 수의 index 목록 ( stack로 맨 오른쪽 수부터 검사할 거임 )
ans = [-1] * N     # 정답 list 모두 오큰수 없음으로 초기화

for i in range(1, N):               # 전체 수열 순회
  while tA and A[tA[-1]] < A[i]:    # 검사할 수가 존재하고, 검사할 수의 오큰수를 만났음
    ans[tA.pop()] = A[i]            # 정답 list에 오큰수 입력
  tA.append(i)                      # 검사할 수가 없거나 검사할 수의 오큰수가 없음
                                    # 현재 index의 수를 검사할 수 목록에 추가
print(*ans)                         # answer
