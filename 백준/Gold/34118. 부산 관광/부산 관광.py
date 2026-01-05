I=input;J=int;R=range
n=J(I())
a,b=[[*map(J,I()),0]for _ in'  ']
p,q,r,s=map(J,I().split())
d=[[9**9]*(n+5)for _ in[9**9]*(n+5)]
d[0][0]=0
def f(x,y,z):d[x][y]=min(d[x][y],z)
for i in R(n+1):
 for j in R(n+1):
  c=d[i][j]
  for x,y,z in(1,0,a[i]),(0,1,b[j]):
   if z:
    f(i+x,j+y,c+p)
    for k in R(4):f(i+x*k,j+y*k,c+q)
    for k in R(6):f(i+x*k,j+y*k,c+r)
   else:f(i+x,j+y,c)
  if i==j:[f(i+x,j+y,c+s)for x in R(5)for y in R(5)]
print(d[n][n])