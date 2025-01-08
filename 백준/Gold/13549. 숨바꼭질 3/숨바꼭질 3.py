def f(i,j):return i-j if i>=j else 1 if j==1 else 1+min(f(i,j+1),f(i,j-1))if j&1 else min(f(i,j//2),j-i)
print(f(*map(int,input().split())))