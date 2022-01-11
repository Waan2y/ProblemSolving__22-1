import sys

N = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(N):
  tmp = int(sys.stdin.readline())
  nums[tmp] += 1

for i in range(len(nums)):
  if nums[i] == 0:
    continue
  else:
    for _ in range(nums[i]):
      print(i)
