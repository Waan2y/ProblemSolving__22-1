import sys

def rev_board(board:list, start:int, end:int):
 return board[:start] + list(reversed(board[start:end+1])) + board[end+1:]

def rev_board2(board:list, start:int, end:int):
 return board[:end] + list(reversed(board[end:start+1])) + board[start+1:]


n = int(sys.stdin.readline().rstrip())
#print("n : ", n)

board = list(map(int, sys.stdin.readline().rstrip().split()))
board_2 = board[:]
#print(board)

start = 0
end = 0
cnt = 0
not_an_answer = False  # 앞에서 부터 찾는게 답인지 ?
ans_list = []
i = 0

while True:
  if i < n:
    if board[i] != i+1:    # 처음으로 다른 구간
      start = i            # 지금이 뒤집기 시작
      for j in range(start, n): # 나머지 돌면서
        if board[j] == start+1: # 뒤집기 끝
          end = j               # 여기가 끝
          break
      if cnt < 2:
        ans_list.append(start+1)
        ans_list.append(end+1)
        board = rev_board(board, start, end)
        #print(board)
        start = 0
        end = 0
        cnt += 1
      else:
        ans_list.clear()
        not_an_answer = True
        break
    else:
      i += 1
  else:
    break

if len(ans_list) == 0:
  if cnt == 0:
    sys.stdout.write('1 1' + '\n')
    sys.stdout.write('1 1')
  else:
    pass
elif len(ans_list) == 2:
  sys.stdout.write(str(ans_list[0]) + ' ' + str(ans_list[1]) + '\n')
  sys.stdout.write('1 1')
else:
  sys.stdout.write(str(ans_list[0]) + ' ' + str(ans_list[1]) + '\n')
  sys.stdout.write(str(ans_list[2]) + ' ' + str(ans_list[3]))


i = n-1
cnt2 = 0
ans_list_2 = []
if not_an_answer:
  #print(board_2)
  while True:
    if i >= 0:
      if board_2[i] != i+1:    # 처음으로 다른 구간
        start = i            # 지금이 뒤집기 시작
        for j in range(start-1, -1, -1): # 나머지 돌면서
          #print("j: ", j)
          if board_2[j] == start+1: # 뒤집기 끝
            end = j               # 여기가 끝
            break
        if cnt2 < 2:
          ans_list_2.append(end+1)
          ans_list_2.append(start+1)
          board_2 = rev_board2(board_2, start, end)
          #print(board_2)
          start = 0
          end = 0
          cnt2 += 1
        else:
          break
      else:
        i -= 1
    else:
      break

if len(ans_list_2) == 0:
  pass
else:
  sys.stdout.write(str(ans_list_2[0]) + ' ' + str(ans_list_2[1]) + '\n')
  sys.stdout.write(str(ans_list_2[2]) + ' ' + str(ans_list_2[3]))
