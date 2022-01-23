#     ***   my first answer : AC   ***     #
def solution(n):
    answer = 0
    base_3 = []

    while(n > 0):              # make base_3 (reverse)
        base_3.append(n % 3)
        n //= 3

    i = 3 ** (len(base_3) - 1) # make base_3 to base_10
    for tmp in base_3:
        answer += tmp * i
        i /= 3

    return answer
