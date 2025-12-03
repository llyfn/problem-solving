s,_,*t=open(0).read().split()
t={*map(int,t)}
q=['']
p=''
for i in range(len(s))[::-1]:
 c,h=s[i],q[-1]
 if i+1in t or c<(p if c==h else h):
  if c!=h:p=h
  q+=c,
print(*q[:0:-1],sep='')
