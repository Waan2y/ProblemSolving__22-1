import sys
import math

def Fact(i:int):
  ans = 1
  for i in range(i, 1, -1):
    ans *= i                  # ans = (i)!
  return str(ans)[::-1]       # ans를 reverse 함.
                              # 뒤에서부터 0이 아닌 수 찾을 거니까
                              # 미리 뒤집어 놓고 앞에서부터 찾을거
N = int(sys.stdin.readline())
val = Fact(N)
cnt = 0

for i in val:   # (i)!.reverse 전체 순회
  if i != '0':  # 0 아닌 숫자 나왔다
    break       # 여기 까지
  else:         # 0 이다
    cnt += 1    # 0 개수++

print(cnt)
