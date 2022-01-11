C = int(input())

for _ in range(C):
  scores = list(map(int, input().split()))
  std_nums = scores[0]
  del scores[0]
  avg_over_count = 0

  scores_average = sum(scores) / std_nums

  for i in scores:
    if i > scores_average:
      avg_over_count += 1
    else:
      continue;

  ans = avg_over_count / std_nums * 100
  print( '%.3f%%' %ans)
