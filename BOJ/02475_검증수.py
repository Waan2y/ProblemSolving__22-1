serial = list(map(int, input().split()))
sum = 0

for i in serial:
  sum += i ** 2

print(sum % 10)
