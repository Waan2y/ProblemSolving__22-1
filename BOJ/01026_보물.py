import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
while A:                        # A 전체 돌거임
  ans += (max(A) * min(B))      # A 는 순서가 바뀔수 있으니, max(A) 값과
  A.remove(max(A))              # min(B) 를 곱한 값들을 더하면 답
  B.remove(min(B))
print(ans)
