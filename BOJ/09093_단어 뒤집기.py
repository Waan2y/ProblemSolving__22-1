t = int(input())

for _ in range(t):
  s = list(input().split())
  for i in range(len(s)):
    print(s[i][::-1], end = ' ')
