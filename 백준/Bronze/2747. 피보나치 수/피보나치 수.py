f=[0]*46
f[0]=f[1]=1
for i in range(2,45):f[i]=f[i-1]+f[i-2]
print(f[int(input())-1])