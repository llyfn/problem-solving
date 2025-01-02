_,*l=map(int,open(0))
p=[1]*100
for i in range(97):p[i+3]=p[i+1]+p[i]
for i in l:print(p[i-1])
