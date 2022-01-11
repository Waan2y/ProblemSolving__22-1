N = int(input())
scores = list(map(int, input().split()))
new_scores = list()

for i in range(len(scores)):
  new_scores.append(scores[i] / max(scores) * 100)

print(sum(new_scores)/len(new_scores))
