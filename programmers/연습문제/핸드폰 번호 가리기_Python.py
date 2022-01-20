#     ***   my first answer : AC   ***     #
def solution(phone_number):
  ans = ""
  ans = '*' * (len(phone_number) - 4)
  ans += phone_number[-4:]
  return ans


#     ***   another answer   ***     #
# 그냥 바로 return 해도 된다
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
