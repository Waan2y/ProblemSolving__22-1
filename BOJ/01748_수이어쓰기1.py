'''
N 범위     : 자리수
1-9       : N               = 1N-0
10-99     : 2(N-10)  +9 +2  = 2N-9
100-999   : 3(N-100) +189 +3 = 3N-108
1000-0000 : 4(N-1000) +2889 +4 = 4N-1107
'''
import sys

N = int(sys.stdin.readline());
new_string = ""

for tmp in range(1, N+1):
  new_string += str(tmp)

sys.stdout.write(str(len(new_string)))



import sys
import math

N = int(sys.stdin.readline());
cal = '0'
digit_N = int(math.log10(N))+1

for tmp_cal in range(1, digit_N):
  cal += str(tmp_cal)

sys.stdout.write(str( (digit_N * N) - (9 * int(cal))))
