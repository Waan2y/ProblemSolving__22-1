import sys
N, M = map(int, sys.stdin.readline().split())
print(M*N - 1)

# N x M 을 M개의 N x 1 로 만드는
# 횟수 : M - 1
# N x 1 을 1 x 1로 만드는
# 횟수 : N - 1  ( 이걸 M 번 해야함 )
# 총 횟수 : (M - 1) + M(N - 1)
