import sys
I=sys.stdin.readline
o={'+':lambda x,y:x+y,'*':lambda x,y:x*y}
for _ in[0]*int(I()):
 p=2
 for i in[0]*int(I()):
  a,b,c,d=I().split()
  q=0
  for j in range(7):
   if p>>j&1:q|=1<<o[a](j,int(b))%7|1<<o[c](j,int(d))%7
  p=q
 print('UN'*(~p&1)+'LUCKY')