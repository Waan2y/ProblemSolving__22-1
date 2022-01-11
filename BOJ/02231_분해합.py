N = int(input())
ans = 0

for target in range(N+1):
  sum_digit = sum(map(int, str(target)))
  sum_all = target + sum_digit

  if(sum_all == N):
    ans = target
    break
  else:
    continue

print(ans)
