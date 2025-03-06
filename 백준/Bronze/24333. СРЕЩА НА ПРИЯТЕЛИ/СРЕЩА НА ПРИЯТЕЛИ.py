a,b,c,d,e=map(int,input().split())
l,r=max(a,c),min(b,d)
print(max(r-l+1-r//e+(l-1)//e,0))