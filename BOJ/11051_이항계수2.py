import sys
from math import factorial

n, k = map(int, sys.stdin.readline().rstrip().split())
c = factorial(n) // (factorial(k) * factorial(n-k))
sys.stdout.write(str(c % 10007))
