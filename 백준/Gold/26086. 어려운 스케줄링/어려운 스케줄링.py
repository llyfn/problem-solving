from collections import*
I=lambda:map(int,input().split())
N,Q,K=I()
C=[[*I()]for _ in[0]*Q]
l=0
for i,c in enumerate(C):
 if c[0]==1:l=i+1
s=deque(sorted(i[1]for i in C[:l]if i[0]<1))
f=0
for c in C[l:]:
 if c[0]:f^=1
 else:[s.appendleft,s.append][f](c[1])
print(s[(K-1,-K)[f]])