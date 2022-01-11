from itertools import combinations
import sys

N = int(input())
list_of_group = list()
rank = list()

for _ in range(N):
  weight, height = map(int, sys.stdin.readline().split())
  list_of_group.append((weight, height))

for i in range(N):
  tmp_rank = 1

  for j in range(N):
    if list_of_group[i][0] < list_of_group[j][0]:
      if list_of_group[i][1] < list_of_group[j][1]:
        tmp_rank += 1
      else:
        pass
    else:
      pass
  rank.append(tmp_rank)

for answer in rank:
  print(answer, end = ' ')
