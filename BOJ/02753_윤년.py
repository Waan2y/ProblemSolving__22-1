year = int(input())
answer = 0

if year%400 == 0:
  answer = 1

elif year%4 == 0:
  if year%100 != 0:
    answer = 1
  else:
    answer = 0

else:
  answer = 0

print(answer)
