room = int(input())
i = 0
tmp = 1

while True:
  tmp += 6 * i
  if room > tmp:
    i += 1
  elif room <= tmp:
    break;

print(i+1)
