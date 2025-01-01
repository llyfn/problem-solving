a,b=input(),input();p,q=len(a),len(b)
d=[['']*(q+1)for _ in range(p+1)]
for i in range(p):
    for j in range(q): d[i+1][j+1]=d[i][j]+a[i]if a[i]==b[j]else max(d[i+1][j],d[i][j+1],key=len)
print(d[p][q])