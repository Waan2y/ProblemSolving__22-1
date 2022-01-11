s = input()
cnt = len(s)

cnt -= s.count("c=")
cnt -= s.count("c-")
cnt -= s.count("d-")
cnt -= s.count("lj")
cnt -= s.count("nj")
cnt -= s.count("s=")
cnt -= s.count("z=")
cnt -= s.count("dz=")

print(cnt)
