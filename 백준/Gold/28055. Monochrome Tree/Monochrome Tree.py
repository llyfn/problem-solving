I=[*map(int,open(0).read().split())]
n=I[0]
T=[0,0]+I[1:]
D=[0]*-~n
for x in T:D[x]+=1
S=[1]*-~n
Q=[i for i in range(1,n+1)if D[i]<1]
for u in Q:
 p=T[u]
 if p:S[p]+=S[u];D[p]-=1;D[p]<1and Q.append(p)
a=0
print(0,*[a:=a+x-1for x in sorted(S[1:])])