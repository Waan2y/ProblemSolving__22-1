T = int(input())

for i in range(0,T):
  A, B = input().split()
  A, B = int(A), int(B)
  print("Case #%d: %d" %(i+1, A+B))
