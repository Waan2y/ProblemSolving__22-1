import sys
N = int(sys.stdin.readline())
nums = list()

for _ in range(0, N):
    tmp = int(sys.stdin.readline())
    nums.append(tmp)

nums.sort()
for i in nums:
    print(i)
