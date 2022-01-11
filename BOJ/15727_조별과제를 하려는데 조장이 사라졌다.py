L = int(input())
cnt = 0

while L > 0:

  if L >= 5:
    L -= 5
    cnt += 1

  elif L >= 4:
    L -= 4
    cnt += 1

  elif L >= 3:
    L -= 3
    cnt += 1

  elif L >= 2:
    L -= 2
    cnt += 1

  elif L >= 1:
    L -= 1
    cnt += 1

print(cnt)
