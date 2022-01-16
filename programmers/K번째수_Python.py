#*     ***   my first answer : AC   ***     *#
# 단순히 구현하면 된다
def solution(array, commands):
    answer = []                            # answer

    for i in commands:                     # loop : commands
        tmp = []                           # list to use temporarily
        tmp = array
        tmp = tmp[i[0] - 1 : i[1]]         # slicing tmp
        tmp.sort()                         # sorting
        answer.append(tmp[i[2] - 1])       # make answer

    return answer


#*     ***   another answer 1  ***     *#
# 한번에 i, j, k로 입력받아 for문 없이도 만들 수 있다
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer


#*     ***   another answer 2  ***     *#
# 바로 list로 return 해도 된다
# sorted 가 array를 수정하지 않는 걸 이렇게 이용할 수도 있다
# 이런 방법의 구현도 가능 하다니 ..
def solution(array, commands):
    return [sorted(array[s-1:e])[i-1] for s, e, i in commands]
