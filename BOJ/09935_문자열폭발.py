import sys

string = list(sys.stdin.readline().rstrip())
string = string[::-1]
bomb = list(sys.stdin.readline().rstrip())

ls = len(string)
lb = len(bomb)

answer = []
for _ in range(0, lb-1):
  answer.append(string.pop())

while True:
  if(len(string)):
    answer.append(string.pop())
    if(answer[-lb:] == bomb):
      for _ in range(0, lb):
        answer.pop()
  else:
    break

if(len(answer)):
  print(''.join(answer))
else:
  print("FRULA")
