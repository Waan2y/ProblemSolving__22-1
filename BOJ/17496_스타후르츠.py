N, T, C, P = map(int, input().split())
cnt = 0
i = 1

while i <= N:
  i += T
  cnt += C

print((cnt-C)*P)
