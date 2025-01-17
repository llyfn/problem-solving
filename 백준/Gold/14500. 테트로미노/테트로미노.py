import sys
I=lambda:map(int,sys.stdin.readline().split())
n,m=I()
a=[[*I()]for _ in range(n)]
M=0
d0=[[(0,0),(0,1),(0,2),(0,3)]]
d1=[[(0,0),(0,1),(0,2),(1,0)],[(0,0),(0,1),(0,2),(1,1)],[(0,0),(0,1),(0,2),(1,2)],[(0,0),(1,0),(1,1),(1,2)],[(0,1),(1,0),(1,1),(1,2)],[(0,2),(1,0),(1,1),(1,2)],[(0,0),(0,1),(1,1),(1,2)],[(0,1),(0,2),(1,0),(1,1)]]
d2=[[(0,0),(0,1),(1,0),(1,1)]]
d3=[[(0,0),(1,0),(2,0),(0,1)],[(0,0),(1,0),(2,0),(1,1)],[(0,0),(1,0),(2,0),(2,1)],[(0,0),(0,1),(1,1),(2,1)],[(1,0),(0,1),(1,1),(2,1)],[(2,0),(0,1),(1,1),(2,1)],[(0,0),(1,0),(1,1),(2,1)],[(1,0),(2,0),(0,1),(1,1)]]
d4=[[(0,0),(1,0),(2,0),(3,0)]]
for i in range(n):
    for j in range(m):
        if j+3<m: M=max(M,*[sum([a[i+di][j+dj]for di,dj in d])for d in d0])
        if i+1<n and j+2<m:M=max(M,*[sum([a[i+di][j+dj]for di,dj in d])for d in d1])
        if i+1<n and j+1<m:M=max(M,*[sum([a[i+di][j+dj]for di,dj in d])for d in d2])
        if i+2<n and j+1<m:M=max(M,*[sum([a[i+di][j+dj]for di,dj in d])for d in d3])
        if i+3<n:M=max(M,*[sum([a[i+di][j+dj]for di,dj in d])for d in d4])
print(M)