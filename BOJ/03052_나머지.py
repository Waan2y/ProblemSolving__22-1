numbers = list()

for _ in range(10):
  tmp = int(input()) % 42
  numbers.append(tmp)

numbers = set(numbers)
print(len(numbers))
