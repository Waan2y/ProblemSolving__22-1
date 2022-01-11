N = int(input())
answer = 1

if N == 0:
    answer = 1
else:
    for i in range(1, N+1):
        answer *= i
print(answer)
