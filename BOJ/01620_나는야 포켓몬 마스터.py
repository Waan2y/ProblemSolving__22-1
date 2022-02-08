import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

book_poketmon = {}
book_num = {}
for i in range(1, N+1):                             # 입력 전부 dict로 저장
  poketmon_name = sys.stdin.readline().rstrip()
  book_poketmon[poketmon_name] = i                  # 이름 - 번호 도감
  book_num[i] = poketmon_name                       # 번호 - 이름 도감

for _ in range(M):
  tmp = sys.stdin.readline().rstrip()
  if tmp.isdigit():              # 도감 번호 ?
    print(book_num[int(tmp)])    # 번호 - 이름에서 출력
  else:                          # 포켓몬 이름 ?
    print(book_poketmon[tmp])    # 이름 - 번호에서 출력
