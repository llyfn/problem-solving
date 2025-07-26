d=[1]
for i in range(1,36):d+=sum(d[j]*d[i-j-1]for j in range(i)),
print(d[int(input())])