i=input;i();a=[*i()]
l={'AC':'A','AG':'C','AT':'G','GC':'T','GT':'A','CT':'G'}
x=a.pop()
while a:y=a.pop();x=[l.get(x+y)or l.get(y+x),x][x==y]
print(x)