correct_set = [1, 1, 2, 2, 2, 8]
now_set = list(map(int, input().split()))

for i in range(6):
  tmp = correct_set[i] - now_set[i]
  print(tmp, end = ' ')
