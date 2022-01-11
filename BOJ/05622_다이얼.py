s = input()
answer = 0

for ch in s:
  if ord(ch) < 68:
    answer += 3
  elif ord(ch) < 71:
    answer += 4
  elif ord(ch) < 74:
    answer += 5
  elif ord(ch) < 77:
    answer += 6
  elif ord(ch) < 80:
    answer += 7
  elif ord(ch) < 84:
    answer += 8
  elif ord(ch) < 87:
    answer += 9
  else:
    answer += 10

print(answer)
