s1 = input()
s2 = input()
ans = 0
for i in range(len(s1)) :
    if s1[i] == s2[i] :
        ans += 1
print(ans)
