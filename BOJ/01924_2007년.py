import sys
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, sys.stdin.readline().split())
day_gap = y -1

for i in range(x):
  day_gap += month[i]

print(days[day_gap % 7])
