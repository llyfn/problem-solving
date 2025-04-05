import re,collections as c
C=c.Counter
f=lambda x:re.sub(r'[aeiou]','',x)
_,a,b=open(0)
a=a.strip();b=b.strip()
print('YNEOS'[C(a)!=C(b)or f(a)!=f(b)or a[-1]!=b[-1]or a[0]!=b[0]::2])