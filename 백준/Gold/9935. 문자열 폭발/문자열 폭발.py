s,e,q=[*input()],[*input()],[]
l=len(e)
for i in s:
    q+=i,
    if q[-l:]==e:del q[-l:]
print(*q if q else 'FRULA',sep='')