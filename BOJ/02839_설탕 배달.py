n = int(input())

answer = 0
div_3 = n // 3
mod_3 = n % 3

if mod_3 == 1:
  if div_3 >= 3:
    div_3 -= 3
    answer += 2
  else:
    div_3 = 0
    answer = -1

  while(div_3 >= 5):
    div_3 -= 5
    answer += 3

elif mod_3 == 2:
  div_3 -= 1
  answer += 1

  while(div_3 >= 5):
    div_3 -= 5
    answer += 3

else:
  while(div_3 >= 5):
    div_3 -= 5
    answer += 3

answer += div_3
print(answer)
