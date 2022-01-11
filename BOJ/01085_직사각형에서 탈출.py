x, y, w, h = map(int, input().split())

cmp = list()
cmp.append(w - x)
cmp.append(h - y)
cmp.append(x)
cmp.append(y)

print(min(cmp))
