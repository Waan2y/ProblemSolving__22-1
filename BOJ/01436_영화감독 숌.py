N = int(input())

check = '666'
for_check = 666
count = 1

while 1:
  if count == N:
    print(for_check)
    break;
  else:
    for_check += 1

  if check in str(for_check):
    count += 1
  else:
    pass
