s = input()
s1 = s[:int((len(s)-1)/2)]
s2 = s[int((len(s)+2)/2):]
if s1 == s2 and s1 == s1[::-1] and s2 == s2[::-1] :
    print('Yes')
else :
    print('No')
