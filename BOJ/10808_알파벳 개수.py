import sys
s = list(sys.stdin.readline().rstrip())
ans = [0]*26

for k in s:
  ans[ord(k)-97] += 1

print(*ans)
