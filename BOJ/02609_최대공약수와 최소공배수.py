import sys
import math

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

GCD = math.gcd(n1, n2)     # 최대공약수
print(GCD)
LCM = int((n1*n2) / GCD)   # 최소공배수 = 두 수의 곱 / 최대공약수
print(LCM)
