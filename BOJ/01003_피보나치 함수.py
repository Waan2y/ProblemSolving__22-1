cnt_0 = [1, 0]
cnt_1 = [0, 1]

for i in range(40):
  cnt_0.append(cnt_0[i] + cnt_0[i+1])
  cnt_1.append(cnt_1[i] + cnt_1[i+1])

T = int(input())
for _ in range(T):
  tmp = int(input())
  print("%d %d" %(cnt_0[tmp], cnt_1[tmp]))
