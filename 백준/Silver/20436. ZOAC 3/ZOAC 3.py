K=['zxcvbnm','asdfghjkl','qwertyuiop']
D={c:(i,j)for i,r in enumerate(K)for j,c in enumerate(r)}
(p,q),_,(r,s),_,*l,_=map(D.get,open(0).read())
S=0
for x,y in l:exec('S+=abs(%s-x)+abs(%s-y)+1;%s,%s=x,y'%(('r','s','r','s'),('p','q','p','q'))[y<4or x>0and y<5])
print(S)