import sys

bits = 0    # set S

M = int(sys.stdin.readline())
for _ in range(M):
  cmd = sys.stdin.readline().rstrip()

  if ' ' in cmd:                 # check command
    cmd1, x = cmd.split()        #     ..
  else:                          #     ..
    cmd1 = cmd                   #     ..

  if(cmd1 == "add"):
    bits |= (1<<int(x))

  elif(cmd1 == "remove"):
    bits &= ~(1<<int(x))

  elif(cmd1 == "check"):
    if(bits & (1<<int(x))):
      sys.stdout.write("1\n")
    else:
      sys.stdout.write("0\n")

  elif(cmd1 == "toggle"):
    bits ^= (1<<int(x))

  elif(cmd1 == "all"):      #    (1<<n) : n bit 가 1
    bits = ((1<<21) -1)     # (1<<n) -1 : n bit 아래 모든 bit 1

  else:
    bits = 0
