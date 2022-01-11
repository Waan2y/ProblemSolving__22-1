import math

while True:
  sides = list(map(int, input().split()))

  max_idx = sides.index(max(sides))

  if sides == [0, 0, 0]:
    break

  if max_idx == 0:
    if sides[0] ** 2 == sides[1] ** 2 + sides[2] ** 2:
      print("right")
    else:
      print("wrong")

  elif max_idx == 1:
      if sides[1] ** 2 == sides[0] ** 2 + sides[2] ** 2:
        print("right")
      else:
        print("wrong")

  elif max_idx == 2:
      if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print("right")
      else:
        print("wrong")
