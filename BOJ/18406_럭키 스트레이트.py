N = list(input())
middle_index = int(len(N) / 2)

sum_left = 0
sum_right = 0

for i in range(len(N)):
  if i < middle_index:
    sum_left += int(N[i])
  else:
    sum_right += int(N[i])

if sum_left == sum_right:
  print("LUCKY")
else:
  print("READY")
