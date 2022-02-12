import sys
input = sys.stdin.readline

def find_D(D : int, num :list):   # 그냥 완전 탐색
  for i in range(len(num)):
    if i == 0:
      div = (num[0] % D)
    elif div == (num[i] % D):
      continue
    else:
      return False
  print(D)
  return True

N= int(input())
nums = list(map(int, input().rstrip().split()))

D = max(nums) +1        # 수가 전부 같지 않으면, 제일 큰 수 보다 더 큰수로 나눴을 때부터는
                        # 나머지가 같을 수가 없음
while True:
  if find_D(D, nums):
    break
  else:
    D -= 1
