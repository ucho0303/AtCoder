n = int(input())
s = input()
ans = 0
for i in range(n-2) :
    if s[i] == 'A':
        if s[i+1] == 'B':
            if s[i+2] == 'C':
                ans += 1
            else :
                pass
        else :
            pass
    else :
        pass
print(ans)