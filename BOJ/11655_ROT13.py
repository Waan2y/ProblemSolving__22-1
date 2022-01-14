S = input()
answer = []

for tmp in S:
  if not (tmp.isalpha()):
    answer.append(tmp)
  else:
    tmp2 = ord(tmp) + 13

    if ord(tmp) <= 90 and tmp2 > 90:
      tmp2 -= 26
    elif 90 < ord(tmp) and tmp2 > 122:
      tmp2 -= 26
    answer.append(chr(tmp2))

print(''.join(answer))
