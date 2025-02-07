k,l=open(0)
print(sum(i*(i+1)//2 for i in [i.count('1') for i in l.split('0')]))