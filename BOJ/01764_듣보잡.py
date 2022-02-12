import sys

N ,M= map(int,sys.stdin.readline().rstrip().split())

no_h = set()
for _ in range(N):
  tmp = sys.stdin.readline().rstrip()
  no_h.add(tmp)

no_s = set()
for _ in range(M):
  tmp = sys.stdin.readline().rstrip()
  no_s.add(tmp)

answer = list(no_h & no_s)
answer.sort()
print(len(answer))
for ans in answer:
  print(ans)
