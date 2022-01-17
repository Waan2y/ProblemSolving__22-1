#     ***   my first answer : AC   ***     #
def solution(x, n):
    answer = []

    for i in range(1, n+1):
        tmp = x * i
        answer.append(tmp)
    return answer
