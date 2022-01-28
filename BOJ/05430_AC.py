# 계속 TLE 나서 생각을 다시 했다.
# R 명령때마다 뒤집었던 게 너무 느린듯
# reverse status 를 bool 값으로 저장하는 방법이 생각나서 구현

import sys

def commands(cmd : str, arr : list):
  tmp = arr
  reverse_flag = False                      # flag : is_reverse ?
  for s in cmd:
    if s == 'R':                            # ** R command **
      reverse_flag = (~reverse_flag)        # reverse flag : 0 -> 1, 1 -> 0
    elif tmp:                               # ** D command and tmp is NOT EMPTY **
      if reverse_flag:                      # is_reverse? : TRUE
        tmp.pop(-1)                         # pop back
      else:                                 # is_reverse? : FALSE
        tmp.pop(0)                          # pop front
    else:                                   # ** tmp is EMPTY **
        print("error")                      # ERROR
        return                              # EXIT

  if reverse_flag:                          # In the end, answer is_reverse? : TRUE
    tmp.reverse()                           # reverse the answer list
  print('[' + ','.join(tmp) + ']')          # print ANSWER !


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  tmp = []
  cmd = sys.stdin.readline().rstrip()
  X = sys.stdin.readline().rstrip()
  tmp = sys.stdin.readline().rstrip()
  ls = [] if tmp == '[]' else list(tmp[1:-1].split(','))  # tmp 에서 괄호 짜르고 ,로 나누기
                                                          # 빈 배열은 따로 처리함
  commands(cmd, ls)
