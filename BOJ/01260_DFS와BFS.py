import sys
from collections import deque

def DFS(graph :list, v :int, visited :list):
  visited[v] = True
  sys.stdout.write(str(v) + ' ')

  for node in graph[v]:
    if visited[node] == False:
      DFS(graph, node, visited)

def BFS(graph :list, v :int, visited :list):
  queue = deque([v])
  visited[v] = True

  while queue:
    node = queue.popleft()
    sys.stdout.write(str(node) + ' ')
    for n in graph[node]:
      if visited[n] == False:
        queue.append(n)
        visited[n] = True



n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(0, n+1)]  # 1-n 개 node의 연결 정보 저장

for _ in range(0, m):
  tnode1, tnode2 = map(int, sys.stdin.readline().rstrip().split())
  graph[tnode1].append(tnode2)
  graph[tnode2].append(tnode1)
graph = list(sorted(g) for g in graph)  # 여러 정점 중에는 숫자가 작은거 부터 방문하니까 정렬해줌

graph1 = graph[:]
graph2 = graph[:]
visited1 = [False] * (n+1)
visited2 = visited1[:]

DFS(graph1, v, visited1)
sys.stdout.write('\n')
BFS(graph2, v, visited2)
