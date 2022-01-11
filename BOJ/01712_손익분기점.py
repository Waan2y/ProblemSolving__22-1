A, B, C = map(int, input().split())
answer = 0

while True:
  tmp = C - B

  if tmp <= 0:
    answer = -1
    break
  else:
    answer = int(A / tmp)+1
    break

print(answer)
