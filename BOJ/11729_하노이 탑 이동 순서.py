def hanoi_move(n : int, _from : int, _to : int):
  rest = 6 - (_from + _to)

  if n == 1:
    print("%d %d" %(_from, _to))

  else:
    hanoi_move(n-1, _from, rest)
    hanoi_move(1, _from, _to)
    hanoi_move(n-1, rest, _to)


N = int(input())
print(2**N -1)
hanoi_move(N, 1, 3)
