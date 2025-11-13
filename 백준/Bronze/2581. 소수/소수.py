m,n=int(input()),int(input())
p=[]
for i in range(m,n+1):
 for j in range(2,i):
  if i%j<1:break
 else:
  if i>1:p+=i,
print(f'{sum(p)}\n{p[0]}'if p else-1)