import re
p='(?=(I'+'OI'*int(input())+'))'
input();s=input()
print(len(re.findall(p,s)))