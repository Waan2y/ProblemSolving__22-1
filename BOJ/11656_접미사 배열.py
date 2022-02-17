import sys

S = sys.stdin.readline().rstrip()
S_set = []

for i in range(len(S)):
  S_set.append(S[i:])
S_set.sort()

for s in S_set:
  sys.stdout.write("%s\n" %s)
