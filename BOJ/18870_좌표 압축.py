import sys

N = int(sys.stdin.readline())
X = list( map(int, sys.stdin.readline().rstrip().split()))
cX = list(set(X))
cX.sort()

# dic[나] = 나보다 작은애들 갯수
dic = {}
for i in range(len(cX)):
  dic[cX[i]] = i

for Xi in X:
  sys.stdout.write('%d ' %dic[Xi])
