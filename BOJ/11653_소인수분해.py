#       *** First answer : TLE ***      #
# 먼저 소수를 다 찾아놓고 나눠서 소인수분해 하려고 했더니
# 시간초과가 발생했다.
import sys
import math

prime_set = []
def make_prime_set(num : int):
  if num <= 1:
    return
  for i in range(2, int(math.sqrt(num)) +1):
    if num % i == 0:
      return
  prime_set.append(num)

N = int(sys.stdin.readline().rstrip())
for i in range(1, N+1):
  make_prime_set(i)

while(N > 1):
  for i in prime_set:
    if (N % i) == 0:
      sys.stdout.write("%d\n" %i)
      N /= i
      break

#       *** Second answer : AC ***      #
# 그냥 매번 2부터 안 나누어질 때 까지 나누면
# 소수가 아닌건 앞에서 이미 계산되므로
# 소인수분해 가능

import sys
N = int(sys.stdin.readline().rstrip())

i = 2
while(N > 1):
  if (N % i) == 0:
      sys.stdout.write("%d\n" %i)
      N /= i
      i = 2
  else:
    i += 1
