#     ***   my answer : AC   ***     #
# C++ 의 second answer 과 같은 방법으로 구현
def solution(participant, completion):
    answer = ''                  # answer
    participant.sort()           # sort participant
    completion.sort()            # sort completion
    completion.append("0")       # append "0" at completion

    for i in range(len(participant)):
        if participant[i] != completion[i]:  # if not same?
            return participant[i]            # It is answer

#     ***   another answer   ***     #
# Counter 객체를 사용하니 엄청 단순하게 구현된다
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
