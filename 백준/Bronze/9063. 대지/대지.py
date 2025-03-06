_,*l=map(int,open(0).read().split())
print((max(l[::2])-min(l[::2]))*(max(l[1::2])-min(l[1::2])))