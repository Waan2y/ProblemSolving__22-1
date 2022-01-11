t = int(input())

for _ in range(t):
  case = input()
  count = 0
  answer = 0

  for i in case:
    if i == 'O':
      count += 1
      answer += count

    else:
      count = 0

  print(answer)
