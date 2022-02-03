import sys
EXP = sys.stdin.readline().rstrip()
sticks = []
ans = 0
i = 0

while i < len(EXP):
  if EXP[i] == '(':                 # (
    if EXP[i+1] == ')':             # () 레이저
      for j in range(len(sticks)):  # sticks 내부 값
        sticks[j] += 1              # 전부 증가
      i += 1                        # () 다음칸으로

    else:                           # ( 막대기 시작
      sticks.append(1)              # sticks 갯수 증가

  else:                             # ) 막대기 끝
    ans += sticks.pop()             # 현재값 pop
  i += 1

print(ans)
