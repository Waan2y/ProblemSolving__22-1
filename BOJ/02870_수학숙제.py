import sys

N = int(sys.stdin.readline())
ans = []

for _ in range(N):
  string = sys.stdin.readline().rstrip()
  tmp = ""

  for st in string:
    if st.isdigit():
      tmp += st
    elif tmp:
      ans.append(int(tmp))
      tmp = ""
    else:
      continue

  if tmp:
    ans.append(int(tmp))
ans.sort()

for i in ans:
  sys.stdout.write("%d\n" %i)
