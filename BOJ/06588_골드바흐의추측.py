import sys

def is_prime(n :int): # O(log(n))
  is_prime = True
  for div in range(2, int(n**(1/2))+1):
    if n%div == 0:
      is_prime = False
      break
    else:
      continue
  return is_prime

while True: # nlog(n) 이니까 가능
  n = int(sys.stdin.readline())
  if n == 0:
    break
  else:
    a = 3 # 최소 3부터 시작
    while True:
      b = n - a
      #print(a, b)
      if is_prime(b):
        sys.stdout.write(str(n) + " = " + str(a) + " + " + str(b) + '\n')
        break
      else:
        a += 1
        while not is_prime(a):
          a += 1
