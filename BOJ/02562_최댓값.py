ans_max = 0
ans_cnt = 0

for i in range(9):
  tmp = int(input())
  if tmp > ans_max:
    ans_max = tmp
    ans_cnt = i +1
  else:
    continue

print(ans_max, ans_cnt, sep = '\n')
