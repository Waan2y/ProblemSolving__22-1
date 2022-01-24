#     ***   my first answer : AC   ***     #
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = -1
        stmp = ""
        tmp = arr1[i] | arr2[i]

        for j in range(n):
            if (tmp%2) == 1:
                stmp = "#" + stmp
            else:
                stmp = " " + stmp
            tmp = int(tmp/2)

        answer.append(stmp)
    return answer


#     ***   another answer   ***     #
#  bit 연산에 유용한 여러 함수들이 많다
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):    # zip pair (i, j) : (arr1, arr2)
        a12 = str(bin(i|j)[2:])   # make (i,j) to bin and convert str : slicing 0b
        a12=a12.rjust(n,'0')      # make str to n digit
        a12=a12.replace('1','#')  # replace 1 - '#'
        a12=a12.replace('0',' ')  # replace 0 - ' '
        answer.append(a12)        # append to answer
    return answer
