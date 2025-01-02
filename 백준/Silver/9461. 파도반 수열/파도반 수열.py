_,*l=map(int,open(0))
p=[1]*3+[0]*100
for i in range(3,100):p[i]=p[i-2]+p[i-3]
for i in l:print(p[i-1])
