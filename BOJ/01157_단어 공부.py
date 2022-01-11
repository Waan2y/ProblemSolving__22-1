s = input()
alphaber_list = list()
for _ in range(26):
  alphaber_list.append(0)

max_index = list()
tmp = 0

for i in range(len(s)):
  tmp = ord(s[i])
  if tmp <= 90:
    tmp = tmp - 65
  else:
    tmp = tmp - 97
  alphaber_list[tmp] += 1

for i in range(26):
  if alphaber_list[i] == max(alphaber_list):
    max_index.append(i)
  else:
    continue

if len(max_index) != 1:
  print('?')
else:
  print(chr(max_index[0] + 65))
