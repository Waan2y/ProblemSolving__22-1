#     ***   my first answer : AC   ***     #
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp = list()
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)

    return answer


#     ***   another answer   ***     #
# zip과 반복문을 이런식으로 사용할 수도 있구나
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
