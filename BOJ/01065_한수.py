def hansu(n :int):
  if n < 100:
    return n

  else:
    count = 0
    for nums in range(100, n+1):
      tmp = list(map(int, str(nums)))
      cmp = tmp[1] - tmp[0]

      for i in range(2, len(tmp)):
        t_cmp = tmp[i] - tmp[i-1]
        if cmp == t_cmp:
          if i == len(tmp)-1:
            count += 1
          else:
            continue
        else:
          break

    return 99+count

N = int(input())
print(hansu(N))
