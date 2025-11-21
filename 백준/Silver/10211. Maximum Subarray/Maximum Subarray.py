for s in[*open(0)][2::2]:
 c=m=-1e9
 for i in map(int,s.split()):m=max(m,c:=max(i,c+i))
 print(m)