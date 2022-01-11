x = int(input())
y = int(input())
Q = 0

if x>0:
  if y>0:
    Q = 1
  else:
    Q = 4
else:
  if y>0:
    Q = 2
  else:
    Q = 3

print(Q)
