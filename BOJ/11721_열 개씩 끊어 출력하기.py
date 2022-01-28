import sys
string = sys.stdin.readline().rstrip()

cnt = 0
tmp_s = ""

for i in string:
  cnt += 1
  tmp_s += i

  if cnt == 10:
    print(tmp_s)
    cnt = 0
    tmp_s = ""

if tmp_s:
  print(tmp_s)
