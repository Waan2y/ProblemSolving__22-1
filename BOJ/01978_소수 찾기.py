import math

def isprime(n :int):
  if n == 1:
    return False
  else:
    tmp = int(math.sqrt(n))
    for div in range(2, tmp+1):
      if n % div == 0:
        return False
    return True

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
  if isprime(i):
    cnt += 1
  else:
    continue

print(cnt)
