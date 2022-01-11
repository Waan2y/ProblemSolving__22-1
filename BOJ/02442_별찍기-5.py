N = int(input())

cnt = N-1
for i in range(1, N+1):
  print(" " *cnt, end = '')
  print("*" * (2*i -1))
  cnt -= 1
