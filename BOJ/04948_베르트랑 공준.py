import sys
import math

def make_bitset_prime():
  bitset_prime = 0
  for i in range(1, 246913):
    flag = True
    if(i <= 1):
      flag = False
    for j in range(2, int(math.sqrt(i)) +1):
      if i % j == 0:
        flag = False
        break
    if flag:
      bitset_prime |= (1 << i)
  return bitset_prime
bitset_prime = (bin(make_bitset_prime())[::-1])[:-2]

while True:
  N = int(sys.stdin.readline().rstrip())
  if N == 0:
    break
  else:
    print(bitset_prime[N+1:2*N+1].count('1'))

# bitset 에 미리 다 구해놓고 찾았음
# 그냥 list 써도 될거같다
