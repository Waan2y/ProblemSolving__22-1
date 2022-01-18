#*     ***   my first answer : AC   ***     *#
def solution(dartResult):
    answer = 0
    flag = 0
    score = []

    for T in dartResult:
      if T.isdigit():
        num = int(T)
        if(num == 0 and flag):
          num = 10
        flag = num

      else:
        flag = 0;

        if T == 'S':
          score.append(num)
        elif T == 'D':
          score.append(num**2)
        elif T == 'T':
          score.append(num**3)

        elif T == '*':
          tmp1 = score[-1]
          score.pop()
          if score:
            tmp2 = score[-1]
            score.pop()
            score.append(tmp2 *2)
          score.append(tmp1 *2)

        elif T == '#':
          tmp1 = score[-1]
          score.pop()
          score.append(tmp1 * -1)

    return sum(score)


#*     ***   another answer   ***     *#
# 정규표현식은 진짜 유용한 것 같다.
# 익숙하지 않아서 잘 안쓰게되는데 연습해야겠다
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
