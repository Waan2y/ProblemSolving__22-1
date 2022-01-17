#     ***   my first answer : AC   ***     #
import sys
a, b = map(int, sys.stdin.readline().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        sys.stdout.write("*")
    sys.stdout.write("\n")


#     ***   another answer   ***     #
# 더 파이썬스럽다.
a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)
