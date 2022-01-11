S = int(input())
N = 1
mult = 0

while(mult <= 2*S):
  mult = N * (N +1)
  N += 1

print(N - 2)
