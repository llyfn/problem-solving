I=lambda:map(int, input().split())
n,=I()
s=[[*I()] for _ in range(n)]
p,q=s[0]
s=zip(s[1:],s[2:])
print('{:.1f}'.format(abs(sum([(x-p)*(w-q)-(z-p)*(y-q) for (x,y),(z,w) in s])/2)))
