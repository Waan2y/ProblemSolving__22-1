from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

possible_case = list(combinations(cards,3))
answer = 0

for case in possible_case:
  sum_of_case = sum(case)
  if sum_of_case > M:
    pass

  elif sum_of_case > answer:
    answer = sum_of_case

print(answer)
