import sys

def find_max(start_row, start_col):
  res = 0

  # 여기가 문제같은데 왜 안처되냐 ;;

  # 행 안에서 연속된거
  for row in range(0, N):
    tmp_res = 1
    for col in range(0, N-1):
        if board[row][col] == board[row][col+1]:
          tmp_res += 1
        else:
          tmp_res = 1
        res = res if res > tmp_res else tmp_res


  # 열 안에서 연속된거
  for col in range(0, N):
    tmp_res = 1
    for row in range(0, N-1):
        if board[row][col] == board[row+1][col]:
          tmp_res += 1
        else:
          tmp_res = 1
        res = res if res > tmp_res else tmp_res

  return res


# __ main __
N = int(sys.stdin.readline())
board = []
answer = 0

for _ in range(0, N):
  board.append(list(sys.stdin.readline().rstrip()))


for row in range(0, N):
  for col in range(0, N):
    if col < N-1:
      board[row][col], board[row][col+1] = board[row][col+1], board[row][col]  # 행 안에서 인접한 열 바꾸기

      tmp_ans = find_max(row, col)
      answer = answer if answer > tmp_ans else tmp_ans

      board[row][col], board[row][col+1] = board[row][col+1], board[row][col]  # 원상복구


    if row < N-1:
      board[row][col], board[row+1][col] = board[row+1][col], board[row][col]  # 열 안에서 인접한 행 바꾸기

      tmp_ans = find_max(row, col)
      answer = answer if answer > tmp_ans else tmp_ans

      board[row][col], board[row+1][col] = board[row+1][col], board[row][col]  # 원상복구

print(answer)
