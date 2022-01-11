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

M, N = map(int, input().split())
for nums in range(M, N+1):
  if isprime(nums):
    print(nums)
  else:
    continue
