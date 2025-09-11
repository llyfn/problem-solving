n=int(input())
t='rabbithorse'
if n<12:print(t[:n]);exit()
m=max(range(2,n-8),key=lambda x:x*~-x*((y:=n-x)//9+1)**(y%9)*(y//9)**(9-y%9))
p=[0]*9
for i in range(n-m):p[i%9]+=1
print('r'*p[0]+'a'*p[1]+'b'*m+'i'*p[2]+'t'*p[3]+'h'*p[4]+'o'*p[5]+'r'*p[6]+'s'*p[7]+'e'*p[8])