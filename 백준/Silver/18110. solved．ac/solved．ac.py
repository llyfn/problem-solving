s = sorted([int(input()) for i in range(int(input()))])
k = int(len(s) * .15 + .5)
if k: s = s[k:-k]
print(int(sum(s)/len(s) + .5) if s else 0)