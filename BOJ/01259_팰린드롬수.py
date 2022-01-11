while True:
  n = input()
  n_reverse = n[::-1]

  if n == '0':
    break
  elif n == n_reverse:
    print("yes")
  elif n != n_reverse:
    print("no")
