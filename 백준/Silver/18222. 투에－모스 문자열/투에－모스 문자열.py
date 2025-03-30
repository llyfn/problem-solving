f=lambda x:x if x<2else 1-f(x//2)if x&1else f(x//2)
print(f(int(input())-1))