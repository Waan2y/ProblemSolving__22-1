# a n t i c 는 반드시 포함
# 50개 단어 , set 최대크기 15
# 그냥 brute-force 가능

import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().rstrip().split())

if k < 5:
  for _ in range(n):
    tmp_string = sys.stdin.readline().rstrip()
  print("0")

else:
  words_list_set = []
  words_set = set()

  for _ in range(n):
    tmp_string = sys.stdin.readline().rstrip()
    words_list_set.append(set(tmp_string))
    words_set |= set(tmp_string)
    words_set -= {'a', 'n', 't', 'i', 'c'}

  #print(words_list_set)
  #print(words_set)

  max_val = 0
  if(len(words_set) + 5 <= k):
    print(n)
  else:
    for comb in combinations(words_set, k-5):
      chk_set = set(comb)
      chk_set |= {'a', 'n', 't', 'i', 'c'}

      cnt = 0
      for word in words_list_set:
        if (chk_set & word) == word:
          cnt += 1
        else:
          continue
      max_val = max(cnt, max_val)

    print(max_val)
