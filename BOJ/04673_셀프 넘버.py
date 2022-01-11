def D(n: int):
  tmp = list(map(int, str(n)))
  return n + sum(tmp)

all_nums = list()


for i in range(0, 10001):
  all_nums.append(i)

for i in range(0, 10001):
  d_n = 0
  if D(i) > 10000:
    continue
  else:
    d_n = D(i)
    all_nums[d_n] = 0

for i in range(10001):
  if all_nums[i] != 0:
    print(all_nums[i])
  else:
    continue
