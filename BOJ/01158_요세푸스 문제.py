# 삭제되는 애는 pop 하고
# 나머지는 원형 que 처럼

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

tmp_list = [ str(i) for i in range(1, N+1)]
P = deque(tmp_list)

ans = []
cnt = 0
while True:
  if len(P) == 1:
    ans.append(P.popleft())
    break
  elif cnt == K-1:
    ans.append(P.popleft())
    cnt = 0
  else:
    P.append(P.popleft())
    cnt += 1

sys.stdout.write("<%s>\n" %', '.join(ans))
