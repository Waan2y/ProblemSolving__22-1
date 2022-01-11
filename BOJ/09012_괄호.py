def chk_ps(t_str:str):
  chk = []
  _out = -1

  for i in t_str:
    if i == '(':
      chk.append('(')
      _out += 1

    elif i == ')' and not chk:
      return "NO"

    elif chk[_out] != '(':
      return "NO"

    else:
      del(chk[_out])
      _out -= 1

  if not chk:
    return "YES"
  else:
    return "NO"

T = int(input())
for _ in range(T):
  tmp = input()
  print(chk_ps(tmp))
