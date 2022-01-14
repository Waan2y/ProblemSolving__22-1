import sys

while True:
  a, b = map(int , sys.stdin.readline().split())

  if a == 0 and b == 0:
    break

  elif a == 0 or b == 0:
    print("neither")

  else:
    if b % a == 0:
      print("factor")

    elif a % b == 0:
      print("multiple")

    else:
      print("neither")
