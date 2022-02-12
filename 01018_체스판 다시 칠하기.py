import sys
input = sys.stdin.readline

board_1 = [ "WBWBWBWB",     # 맨 왼쪽 위 칸이 흰색인 체스판 : 1 체스판
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW" ]

board_2 = [ "BWBWBWBW",    # 맨 왼쪽 위 칸이 검은색인 체스판 : 2 체스판
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB" ]

N, M = map(int, input().rstrip().split())   # N x M 보드

board = []                                  # 입력받을 보드
for _ in range(N):                          # 입력
  board.append(input().rstrip())
                                            # N-7 번 오른쪽 이동.
                                            # M-7 번 아래로 이동 하며 탐색
ans_cnt = 9999999999
for tmp_j in range(M-7):                    # 아래 이동 후 시작점 : 0 - (M-8)
  for tmp_i in range(N-7):                  # 오른쪽 이동 후 시작점 : 0 - (M-8)
    cnt_1 = 0                               # 1 체스판으로 만들라면 칠해야 될 횟수
    cnt_2 = 0                               # 2 체스판으로 만들라면 칠해야될 횟수

    for i in range(8):                      # 현재 보드와 체스판 비교
      for j in range(8):
        if board_1[i][j] != board[tmp_i+i][tmp_j+j]:
          cnt_1 += 1
        if board_2[i][j] != board[tmp_i+i][tmp_j+j]:
          cnt_2 += 1

    ans_cnt = ans_cnt if ans_cnt < min(cnt_1, cnt_2) else min(cnt_1, cnt_2)  # 최소 횟수
print(ans_cnt)
