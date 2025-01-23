I=lambda:map(int,input().split())
n,=I()
s=[[*I()]for _ in range(n)]
print(round(abs(sum([x*w-y*z for (x,y),(z,w) in zip(s,s[1:]+s[:1])])/2),1))
