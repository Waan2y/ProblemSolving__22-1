def solution(lottos, win_nums):
    answer = []   # answer
    coi_min = 0   # count coincidence : min
    coi_max = 0   # count coincidence : max

    # count coincidence
    for i in lottos:            # in lottos
        if i == 0:              # if 0 ?
            coi_max += 1        # coincidence_max ++
            continue
        elif i in win_nums:      # if not 0 && coincidence ?
            coi_min += 1         # coincidence_min ++
        else:
            continue
    coi_max += coi_min   # calculate coincidence_max

    # calculate rank
    rank_max = 7 - coi_max if coi_max != 0 else 6
    rank_min = 7 - coi_min if coi_min != 0 else 6

    # set answer
    answer = [rank_max, rank_min]
    return answer

#      *** 다른 풀이 ***
# rank 를 dic로 할까 했었는데, list를 생각을 못했다
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
