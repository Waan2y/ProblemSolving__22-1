# 각 면은 바라보는 방향에서 각각
# 0 1 2
# 3 4 5
# 6 7 8
# 모양의 배열 index를 가짐

import sys
input = sys.stdin.readline

def print_cube(U : list):
  for i in (0, 3, 6):
    for j in range(3):
      sys.stdout.write(U[i+j])
    sys.stdout.write('\n')

T = int(input())
for _ in range(T):  # 각 면 만들기
  U = ['w'] *9
  L = ['g'] *9
  D = ['y'] *9
  R = ['b'] *9
  F = ['r'] *9
  B = ['o'] *9

  n = int(input())
  cmd = list(input().rstrip().split())

  for i in range(n):        # 이후 각 명령마다 구현함
    if cmd[i][0] == 'U':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = F[0], F[1], F[2]
        F[0], F[1], F[2] = R[0], R[1], R[2]
        R[0], R[1], R[2] = B[0], B[1], B[2]
        B[0], B[1], B[2] = L[0], L[1], L[2]
        L[0], L[1], L[2] = tmp1, tmp2, tmp3
        U = [ U[6], U[3], U[0], U[7], U[4], U[1], U[8], U[5], U[2]]

      else:
        tmp1, tmp2, tmp3 = F[0], F[1], F[2]
        F[0], F[1], F[2] = L[0], L[1], L[2]
        L[0], L[1], L[2] = B[0], B[1], B[2]
        B[0], B[1], B[2] = R[0], R[1], R[2]
        R[0], R[1], R[2] = tmp1, tmp2, tmp3
        U = [ U[2], U[5], U[8], U[1], U[4], U[7], U[0], U[3], U[6]]

    elif cmd[i][0] == 'D':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = F[6], F[7], F[8]
        F[6], F[7], F[8] = L[6], L[7], L[8]
        L[6], L[7], L[8] = B[6], B[7], B[8]
        B[6], B[7], B[8] = R[6], R[7], R[8]
        R[6], R[7], R[8] = tmp1, tmp2, tmp3
        D = [ D[6], D[3], D[0], D[7], D[4], D[1], D[8], D[5], D[2]]
      else:
        tmp1, tmp2, tmp3 = F[6], F[7], F[8]
        F[6], F[7], F[8] = R[6], R[7], R[8]
        R[6], R[7], R[8] = B[6], B[7], B[8]
        B[6], B[7], B[8] = L[6], L[7], L[8]
        L[6], L[7], L[8] = tmp1, tmp2, tmp3
        D = [ D[2], D[5], D[8], D[1], D[4], D[7], D[0], D[3], D[6]]

    elif cmd[i][0] == 'F':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = U[6], U[7], U[8]
        U[6], U[7], U[8] = L[8], L[5], L[2]
        L[8], L[5], L[2] = D[2], D[1], D[0]
        D[2], D[1], D[0] = R[0], R[3], R[6]
        R[0], R[3], R[6] = tmp1, tmp2, tmp3
        F = [ F[6], F[3], F[0], F[7], F[4], F[1], F[8], F[5], F[2]]
      else:
        tmp1, tmp2, tmp3 = U[6], U[7], U[8]
        U[6], U[7], U[8] = R[0], R[3], R[6]
        R[0], R[3], R[6] = D[2], D[1], D[0]
        D[2], D[1], D[0] = L[8], L[5], L[2]
        L[8], L[5], L[2] = tmp1, tmp2, tmp3
        F = [ F[2], F[5], F[8], F[1], F[4], F[7], F[0], F[3], F[6]]

    elif cmd[i][0] == 'B':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = U[0], U[1], U[2]
        U[0], U[1], U[2] = R[2], R[5], R[8]
        R[2], R[5], R[8] = D[8], D[7], D[6]
        D[8], D[7], D[6] = L[6], L[3], L[0]
        L[6], L[3], L[0] = tmp1, tmp2, tmp3
        B = [ B[6], B[3], B[0], B[7], B[4], B[1], B[8], B[5], B[2]]
      else:
        tmp1, tmp2, tmp3 = U[0], U[1], U[2]
        U[0], U[1], U[2] = L[6], L[3], L[0]
        L[6], L[3], L[0] = D[8], D[7], D[6]
        D[8], D[7], D[6] = R[2], R[5], R[8]
        R[2], R[5], R[8] = tmp1, tmp2, tmp3
        B = [ B[2], B[5], B[8], B[1], B[4], B[7], B[0], B[3], B[6]]


    elif cmd[i][0] == 'L':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = F[0], F[3], F[6]
        F[0], F[3], F[6] = U[0], U[3], U[6]
        U[0], U[3], U[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = D[0], D[3], D[6]
        D[0], D[3], D[6] = tmp1, tmp2, tmp3
        L = [ L[6], L[3], L[0], L[7], L[4], L[1], L[8], L[5], L[2]]

      else:
        tmp1, tmp2, tmp3 = F[0], F[3], F[6]
        F[0], F[3], F[6] = D[0], D[3], D[6]
        D[0], D[3], D[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = U[0], U[3], U[6]
        U[0], U[3], U[6] = tmp1, tmp2, tmp3
        L = [ L[2], L[5], L[8], L[1], L[4], L[7], L[0], L[3], L[6]]


    elif cmd[i][0] == 'R':
      if cmd[i][1] == '+':
        tmp1, tmp2, tmp3 = U[8], U[5], U[2]
        U[8], U[5], U[2] = F[8], F[5], F[2]
        F[8], F[5], F[2] = D[8], D[5], D[2]
        D[8], D[5], D[2] = B[0], B[3], B[6]
        B[0], B[3], B[6] = tmp1, tmp2, tmp3
        R = [ R[6], R[3], R[0], R[7], R[4], R[1], R[8], R[5], R[2]]

      else:
        tmp1, tmp2, tmp3 =  U[8], U[5], U[2]
        U[8], U[5], U[2] = B[0], B[3], B[6]
        B[0], B[3], B[6] = D[8], D[5], D[2]
        D[8], D[5], D[2] = F[8], F[5], F[2]
        F[8], F[5], F[2] = tmp1, tmp2, tmp3
        R = [ R[2], R[5], R[8], R[1], R[4], R[7], R[0], R[3], R[6]]

  print_cube(U)
