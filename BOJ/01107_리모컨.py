#           ***    first answer : WA   ***
# 처음에 중복순열로 자릿수가 같은 수에서 완전 탐색하는 방법으로 구현
# 하지만 자리수에 상관없이 가능한 경우가 있다.
# | ex. 채널 10 까지 버튼 9 로 가기 )          |
# | 이 경우 한 자리수인 9 에서 + 하는 것이 최적  |
# 이 방식은 0 의 포함여부를 생각하는데 상당히 까다롭다
# 결국 아예 잘못된 생각이었다.
temp_combs = list(product(A, repeat = len(str(N))))
for combs in temp_combs:
  print(int(''.join(combs)))
  tmp = abs(N - int(''.join(combs))) + len(str(N))
  ans = ans if tmp > ans else tmp
print(ans)



#           ***    second answer : AC   ***
import sys

N = int(sys.stdin.readline())               # N : 이동할 채널
A = set(a for a in range(0,10))             # A : 사용 가능한 숫자 버튼
ans = N - 100 if N > 100 else 100 - N       # +/- 로만 이동하는 횟수로 answer 초기화

M = int(sys.stdin.readline().rstrip())
if M == 0:      # 고장난 버튼이 없다 ?
  BTNs = set()
else:           # 고장난 버튼이 있다 ?
  BTNs = set(map(int, sys.stdin.readline().rstrip().split()))

for i in BTNs:  # BTN 에서 고장난 버튼 제거
  A.remove(i)
                                 # 완전 탐색
for ch in range(1000001):        # 채널 범위 무한대니까 위에서 내려오는거까지 *2
  for i in range(len(str(ch))):
    if int(str(ch)[i]) not in A: # 만들수 없는 숫자 ?
      break

    elif i == len(str(ch)) -1:   # 만들 수 있는 숫자 ?
      tmp = abs(N - ch) + len(str(ch)) # +/- 이동 횟수 + 숫자 버튼 입력
      ans = ans if tmp > ans else tmp  # +/- 로만 이동할 때와 현재 이동 중 최소가 답

print(ans)
