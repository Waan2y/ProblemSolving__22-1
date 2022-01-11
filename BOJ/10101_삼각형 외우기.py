a = int(input())
b = int(input())
c = int(input())

if (a + b + c) != 180:
  print("Error")

elif a == 60 and a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
  print("Isosceles")
elif a != b and b != c and c != a:
  print("Scalene")
