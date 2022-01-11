from itertools import permutations

N = int(input())
tmp = []
for i in range(1,N+1):
  tmp.append(i)

answer = list(permutations(tmp, N))

for i in answer:
  print(*i)
