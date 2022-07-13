import sys

m = int(sys.stdin.readline())
calc_sum = 0
calc_xor = 0

while(m):

  cmd = list(map(int, sys.stdin.readline().split()))
  #print(cmd)
  if cmd[0] == 1:
    calc_sum += cmd[1]
    calc_xor = calc_xor ^ cmd[1]
  elif cmd[0] == 2:
    calc_sum -= cmd[1]
    calc_xor = calc_xor ^ cmd[1]       # x ^ x == x ^ 0 == x
  elif cmd[0] == 3:
    sys.stdout.write(str(calc_sum) + '\n')
  else:
    sys.stdout.write(str(calc_xor) + '\n')

  m -= 1
