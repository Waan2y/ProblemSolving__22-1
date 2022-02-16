import sys
input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
  board.append(input().rstrip())

def find_heart(board : list, N : int):    # 심장의 좌표
  for x in range(N):
    for y in range(N):
      if board[x][y] == '*':
        return [x+1, y]
heart = find_heart(board, N)

left_arm = 0                              # 왼팔 길이 계산
x = heart[0]
y = heart[1] -1
while y >= 0 and board[x][y] == '*':
  left_arm += 1
  y -= 1

right_arm = 0                             # 오른팔 길이 계산
x = heart[0]
y = heart[1] +1
while y < N and board[x][y] == '*':
  right_arm += 1
  y += 1

body = 0                                  # 허리 길이 계산
x = heart[0] +1
y = heart[1]
while board[x][y] == '*':
  body += 1
  x += 1

end_of_body = [x, y]

left_leg = 0                              # 왼다리 길이 계산
x = end_of_body[0]
y = end_of_body[1] -1
while x < N and board[x][y] == '*':
  left_leg += 1
  x += 1


right_leg = 0                             # 오른다리 길이 계산
x = end_of_body[0]
y = end_of_body[1] +1
while x < N and board[x][y] == '*':
  right_leg += 1
  x += 1

print("%d %d" %(heart[0]+1, heart[1]+1))
print("%d %d %d %d %d" %(left_arm, right_arm, body, left_leg, right_leg))
