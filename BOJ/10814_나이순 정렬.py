N = int(input())
members = []

for _ in range(N):
  age, name = input().split()
  members.append( (int(age), name))

members.sort(key = lambda x : x[0])

for data in members:
  print(*data)
