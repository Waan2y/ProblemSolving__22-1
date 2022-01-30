import math

prime_set = []
def is_prime(num : int):
  if num <= 1:
    return False
  for i in range(2, int(math.sqrt(num)) +1):
    if num % i == 0:
      return False
  return True

M = int(input())
N = int(input())

for i in range(M, N+1):
  if(is_prime(i)):
    prime_set.append(i)

if len(prime_set):
  print(sum(prime_set))
  print(min(prime_set))
else:
  print(-1)
