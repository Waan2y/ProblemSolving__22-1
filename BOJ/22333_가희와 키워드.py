import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

notepad = set()                 # 메모장
for _ in range(N):              # 키워드 수 만큼
  str_tmp = input().rstrip()    # 키워드 입력
  notepad.add(str_tmp)          # set 에 저장

for _ in range(M):
  list_tmp = list( map(str,input().rstrip().split(',')))  # 새로운 글의 키워드
  for tmp in list_tmp:                                    # 새로운 글의 키워드 전체 순회
    if tmp in notepad:                                    # 메모장에 있으면 ?
      notepad.remove(tmp)                                 # 해당 키워드 삭제
  print(len(notepad))
