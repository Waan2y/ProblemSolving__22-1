A = list(map(int, input().split()))

answer = sum(A) - max(A) - min(A)
print(answer)
