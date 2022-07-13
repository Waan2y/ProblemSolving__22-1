import sys

n = int(sys.stdin.readline())           # n 일 때, p 길이 : 2n+1
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

answer = 0

i = 0
cnt = 0
flag = 0

while i < m:
  if flag == 0:
    if s[i] == 'I':
      cnt += 1
      flag = 1
    else:
      cnt = 0

  elif flag == 1:
    if s[i] == 'O':
      cnt += 1
      flag = 0
    else:
      cnt = 1
  if cnt == (2*n+1):
    answer += 1
    cnt -= 2

  i += 1


print(answer)
