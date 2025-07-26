n=int(input())
r=[input()for _ in[0]*n]
c=[''.join(i)for i in zip(*r)]
k=lambda x:sum(sum(len(s)>1for s in i.split('X'))for i in x)
print(k(r),k(c))