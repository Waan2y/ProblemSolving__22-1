# O(n^2) 까지 가능

import sys

def is_consistent(l :list):
  for i in range(0, len(l)-1):
    j = i+1
    while(j < len(l)):
      if l[i] == l[j][:len(l[i])]:
        return "NO"
      else:
        j += 1
  return "YES"

t = int(sys.stdin.readline())
for _ in range(0, t):
  n = int(sys.stdin.readline())
  number_list = []

  for _ in range(0, n):
    tmp = sys.stdin.readline().rstrip()
    number_list.append(tmp)
  number_list.sort()
  print(is_consistent(number_list))
