import re
while (i:=input())!='#':print(len(re.findall(r'[aeiou]',i,re.I)))