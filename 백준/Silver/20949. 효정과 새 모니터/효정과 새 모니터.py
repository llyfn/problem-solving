_,*l=map(int,open(0).read().split())
for i in sorted([(-v[0]**2-v[1]**2,i+1)for i,v in enumerate(zip(l[::2],l[1::2]))]):print(i[1])