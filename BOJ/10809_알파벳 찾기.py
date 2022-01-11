S = input()
alphabet_list = list()

for i in range(26):
  alphabet_list.append(-1)

for idx in range(0, len(S)):

  if alphabet_list[ord(S[idx])-97] == -1:
    alphabet_list[ord(S[idx])-97] = idx
  else:
    continue

print(*alphabet_list)
