import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

temp = A
sec = 0

iced = 0
ice = 0
notice = 0

while temp != B:
  if temp < 0:
    iced += 1
    temp += 1
  else:
    notice += 1
    temp += 1

if iced != 0 and notice != 0:
  ice = 1
sec = (iced * C) + (ice * D) + (notice * E)
print(sec)
