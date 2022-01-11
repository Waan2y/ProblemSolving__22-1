A = int(input())
B = int(input())
C = int(input())

mult_all = A*B*C
list_mult = list(map(int, str(mult_all)))

for i in range(0,10):
  print(list_mult.count(i), end = '\n')
