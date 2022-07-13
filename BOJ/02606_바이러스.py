import sys

def infect_virus(i : int):
  for Nodes in connect_coms[i]:  # i번 pc 와 연결된 pc list 원소(Nodes)
    if check_coms[Nodes] == 1:   # if 해당 Node 는 이미 감염
      continue                   # 그냥 진행
    else:                        # 아직 감염 안됨
      check_coms[Nodes] = 1          # 해당 Node 감염시키고
      infect_virus(Nodes)            # 해당 Node 와 연결된 컴퓨터 재귀로 감염

n_com = int(sys.stdin.readline())
n_branch = int(sys.stdin.readline())

connect_coms = [ [] for _ in range(0, n_com+1)]

for i in range(0, n_branch):
  t1, t2 = map(int, sys.stdin.readline().split())
  connect_coms[t1].append(t2)
  connect_coms[t2].append(t1)

check_coms = [ 0 for _ in range(0, n_com+1)]
check_coms[1] = 1  # 1번 컴퓨터가 감염 시작점 임

for i in range(1, n_com+1):   # 전체 컴퓨터 순회
  if check_coms[i] == 1:      # i 번째 pc가 감염 ?
    infect_virus(i)           # i 번째 pc 와 연결된 pc로 전염


print(sum(check_coms) -1)
