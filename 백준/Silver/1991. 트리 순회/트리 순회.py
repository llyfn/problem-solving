n=int(input())
t=dict()
for _ in range(n):
    p,q,r=input().split()
    t[p]=[q,r]
def pre(a):
    if a in t:print(a,end='');pre(t[a][0]);pre(t[a][1])
def ino(a):
    if a in t:ino(t[a][0]);print(a,end='');ino(t[a][1])
def post(a):
    if a in t:post(t[a][0]);post(t[a][1]);print(a,end='')
pre('A')
print()
ino('A')
print()
post('A')