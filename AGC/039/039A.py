s = input()
n = int(input())
ans = 0
i = 0
while i > len(s)-2 :
    if s[i] == s[i+1] :
        if s[i] == s[i+2] :
            ans += 1
            i += 3
        else :
            ans += 1
            i += 2
    else :
        i += 1
ans *= n
print(ans)
