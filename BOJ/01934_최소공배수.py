import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
  n1, n2 = map(int, sys.stdin.readline().rstrip().split())
  print(int((n1 * n2)/math.gcd(n1, n2)))  # 최소공배수 = 두 수의 곱 / 최대공약수
