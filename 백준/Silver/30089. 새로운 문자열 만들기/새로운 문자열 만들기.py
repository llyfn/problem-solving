for _ in[0]*int(input()):
    s=input()
    for i in range(len(s)):
        if s[i:]==s[i:][::-1]:
            if i>0:s+=s[i-1::-1]
            break
    print(s)