N = input()
cmp = N
count = 1

if(int(N)<10):
  N = '0' +N

while True:
  if int(cmp) <10:
    cmp = '0' +cmp

  numbers = list(map(int,cmp))

  sum_num = sum(numbers)
  sum_num = list(map(int,str(sum_num)))

  new_str = str(numbers[len(numbers)-1]) + str(sum_num[len(sum_num)-1])
  cmp = new_str

  if cmp == N:
    break
  else:
    count += 1
    continue

print(count)
