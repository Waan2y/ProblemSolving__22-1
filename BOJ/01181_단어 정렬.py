import sys

n = int(sys.stdin.readline())
num_set = set()

for i in range(n):
  tmp_s = sys.stdin.readline().rstrip()
  num_set.add( (len(tmp_s), tmp_s))   # num_set : 길이와 문자열 tuple을 받는 set

num_set = list(num_set)
num_set.sort() # tuple은 원래 앞에 원소부터 sort

for i in num_set:
  print(i[1]) # 정렬된 tuple의 string 만 출력
