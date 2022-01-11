N = int(input())
nums = list()

for _ in range(0, N):
    tmp = int(input())
    nums.append(tmp)

nums.sort()

for i in nums:
    print(i)
