import sys

sum = 0
div = 0

data = [ () for _ in range(0, 20) ]

for i in range(0, 20):
    data[i] = tuple(map(str, sys.stdin.readline().split()))

for t in data:
  if t[2] == 'A+':
    sum += float(t[1]) * 4.5
    div += float(t[1])
  elif t[2] == 'A0':
    sum += float(t[1]) * 4.0
    div += float(t[1])
  elif t[2] == 'B+':
    sum += float(t[1]) * 3.5
    div += float(t[1])
  elif t[2] == 'B0':
    sum += float(t[1]) * 3.0
    div += float(t[1])
  elif t[2] == 'C+':
    sum += float(t[1]) * 2.5
    div += float(t[1])
  elif t[2] == 'C0':
    sum += float(t[1]) * 2.0
    div += float(t[1])
  elif t[2] == 'D+':
    sum += float(t[1]) * 1.5
    div += float(t[1])
  elif t[2] == 'D0':
    sum += float(t[1]) * 1.0
    div += float(t[1])
  elif t[2] == 'F':
    sum += float(t[1]) * 0.0
    div += float(t[1])
  else:
    pass


print(sum/div)
