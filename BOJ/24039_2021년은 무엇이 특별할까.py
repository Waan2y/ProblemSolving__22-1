from math import sqrt
prime = []

def is_prime(n : int):
  for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
      return False
  return True

for i in range(2, 110):
  if is_prime(i):
    prime.append(i)
  else:
    continue;

N = int(input())

i = 0
tmp = 0

while True:
  tmp = prime[i] * prime[i+1]

  if N >= tmp:
    i += 1
  else:
    break

print(tmp)
