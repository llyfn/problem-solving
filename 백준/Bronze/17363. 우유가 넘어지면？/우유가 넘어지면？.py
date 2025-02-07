n,m=map(int,input().split())
for i in [*zip(*[input()for _ in range(n)])][::-1]:print(''.join(i).translate(str.maketrans({45:124,124:45,47:92,92:47,94:60,60:118,118:62,62:94})))
