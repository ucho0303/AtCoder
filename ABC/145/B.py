N = int(input())
S = input()
n = int(N/2)
s1 = S[:n]
s2 = S[n:]
if s1 == s2 :
    print('Yes')
else :
    print('No')
print(s1)
print(s2)
