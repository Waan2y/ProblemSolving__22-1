#     ***   my first answer : AC   ***     #
def solution(x):
    answer = True
    s_x = str(x)        # convert int to string
    tmp = 0

    for i in s_x:      # calc sum(digits)
        tmp += int(i)

    answer = True if (x % tmp == 0) else False
    return answer


#     ***   another answer   ***     #
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
