#     ***   my first answer : AC   ***     #
# set은 중복이 없다.
def solution(nums):
  pokémon = set(nums)           # make set
  diff_pokémon = len(pokémon)  # nums of diff pokémons
  icanget = int(len(nums)/2)    # nums I can get

  # ans = diff pokémons < I can get ?
  answer = diff_pokémon if diff_pokémon < icanget else icanget
  return answer


#     ***   another answer   ***     #
# 아직 갈 길이 멀다.
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
