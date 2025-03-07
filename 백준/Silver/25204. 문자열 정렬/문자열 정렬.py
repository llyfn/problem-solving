c=lambda a:[200 if i=='-'else 2*ord(i)-65if i.upper()==i else 2*ord(i)-128for i in a]
for _ in range(int(input())):
    s=[input() for _ in range(int(input()))]
    print(*sorted(s,key=c),sep='\n')