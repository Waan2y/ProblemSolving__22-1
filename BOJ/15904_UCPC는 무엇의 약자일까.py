s = input()
cmp = ['U', 'C', 'P', 'C']
answer = 1

for i in range(4):
  if cmp[i] in s:
    answer = 1
    idx = s.find(cmp[i])
    s = s[idx+1:]
  else:
    answer = 0
    break

if answer:
  print("I love UCPC")
else:
  print("I hate UCPC")
