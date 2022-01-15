#     ***   my first answer : AC   ***     #
# string을 다루는 데에는 python이 훨씬 편하고 좋은 느낌이다
# 굳이 answer 에 s를 복사 안해와도 된다
def solution(s):
    answer = s[:]                           # copy s : answer
    answer = answer.replace('zero', '0')    # replace
    answer = answer.replace('one', '1')     #   ..
    answer = answer.replace('two', '2')     #   ..
    answer = answer.replace('three', '3')   #   ..
    answer = answer.replace('four', '4')    #   ..
    answer = answer.replace('five', '5')    #   ..
    answer = answer.replace('six', '6')     #   ..
    answer = answer.replace('seven', '7')   #   ..
    answer = answer.replace('eight', '8')   #   ..
    answer = answer.replace('nine', '9')    #   ..
    return int(answer)                      # convert string to int


#     ***   another answer   ***     #
# dic 나 array로 미리 선언해서 하는게 반복문 쓸 수 있어서
# 더 빠르게 짤 수 있을 듯,, 그런가 ? 보기는 더 좋다
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s                               # copy s : answer
    for key, value in num_dic.items():       # loop for set argument
        answer = answer.replace(key, value)  # replace
    return int(answer)                       # convert string to int
