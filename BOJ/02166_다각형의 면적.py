import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
  arr.append(tuple(map(int, input().rstrip().split())))
arr.append(arr[0])                          # 신발끈 공식에 사용하기 위해
                                            # 배열의 가장 처음 두 점을 마지막에 추가
                                            # 오른쪽 아래방향 대각선 곱의 총합
ans1 = 0
for i in range(N):
  ans1 += (arr[i][0] * arr[i+1][1])
                                            # 왼쪽 아래방향 대각선 곱의 총합
ans2 = 0
for i in range(N):
  ans2 += (arr[i+1][0] * arr[i][1])
                                            # 두 값 차의 절댓값 x 1/2
ans = ans1 - ans2 if ans1 > ans2 else ans2 - ans1
ans = (abs(ans)/2)
print(round(ans,1))
