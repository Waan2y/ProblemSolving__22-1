import sys

score = []
for _ in range(5):
  tmp = int(sys.stdin.readline())

  if tmp < 40:
    tmp = 40
  score.append(tmp)

print(sum(score) // 5)
