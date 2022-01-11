fibo = [0] * 46
fibo[1] = 1
i = 0

while(i < 44):
  fibo[i+2] = fibo[i] + fibo[i+1]
  i += 1

n = int(input())
print(fibo[n])
