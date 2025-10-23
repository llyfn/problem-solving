K=['zxcvbnm','asdfghjkl','qwertyuiop']
D={c:(i,j)for i,r in enumerate(K)for j,c in enumerate(r)}
(p,q),_,(r,s),_,*l,_=map(D.get,open(0).read())
S=0;F=[[r,s],[p,q]]
for x,y in l:i=y<5and(y<4or x>0);X,Y=F[i];S+=abs(X-x)+abs(Y-y)+1;F[i]=[x,y]
print(S)