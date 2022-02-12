import sys

N = int(sys.stdin.readline().rstrip())
exp = sys.stdin.readline().rstrip()

dic = {}
alphabet_set = [ chr(i) for i in range(65, 91)]
for i in range(N):
  tmp = float(sys.stdin.readline().rstrip())
  dic[alphabet_set[i]] = tmp

answer = []
operator = set(['+', '-', '*', '/'])
for ex in exp:
  if ex in operator:
    tmp1 = answer.pop()
    tmp2 = answer.pop()

    if ex == '+':
      answer.append(tmp1 + tmp2)
    elif ex == '-':
      answer.append(tmp2 - tmp1)
    elif ex == '*':
      answer.append(tmp1 * tmp2)
    else:
      answer.append(tmp2 / tmp1)

  else:
    answer.append(dic[ex])

print("%.2f" %answer.pop())
