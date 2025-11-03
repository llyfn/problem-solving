n=int(input())
c=*sorted([[*map(int, input().split())]for _ in[0]*n],key=lambda x:x[2]),[0,0,9999999]
m=[[]for _ in[0]*-~n]
v=[0]*(n + 1)
for i in range(n):
 j=i+1
 while (c[j][0]-c[i][0])**2+(c[j][1]-c[i][1])**2>(c[j][2]-c[i][2])**2:j+=1
 m[i]+=[j];m[j]+=[i]
r=[0]
def d(i):
 v[i]=1
 h=0,0,*sorted([d(j)+1for j in m[i]if not v[j]])
 r[0]=max(r[0],h[-1]+h[-2])
 return h[-1]
d(n)
print(r[0])