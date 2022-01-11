T = int(input())

for _ in range(T):
  repu, strg = input().split()
  repu = int(repu)

  for i in range(len(strg)):
    print(repu * strg[i], end="")
  print()
