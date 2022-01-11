import sys

while True:
  ans = [0] *4
  s = list(sys.stdin.readline())
  if not s:
    break;

  for k in s:
    if 97 <= ord(k) and ord(k) <= 122:
      ans[0] += 1
    elif 65 <= ord(k) and ord(k) <= 90:
      ans[1] += 1
    elif 48 <= ord(k) and ord(k) <= 57:
      ans[2] += 1
    elif ord(k) == 32:
      ans[3] += 1
  print(*ans)
