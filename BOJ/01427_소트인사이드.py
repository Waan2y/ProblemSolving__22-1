import sys
nums = list()

nums = list(sys.stdin.readline())
del(nums[len(nums)-1])
nums.sort()
nums.reverse()

for i in nums:
  sys.stdout.write(str(i))

sys.stdout.write('\n')
