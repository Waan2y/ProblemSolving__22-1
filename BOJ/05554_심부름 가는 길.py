secs = list()

for _ in range(4):
  secs.append(int(input()))

_min = sum(secs) // 60
_sec = sum(secs) % 60

print(_min)
print(_sec)
