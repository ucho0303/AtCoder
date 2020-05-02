x = int(input())
a = 100
ans = 0
for i in range(10**7):
    ans += 1
    a *= 1.01
    a = int(a)
    if a >= x :
        break
print(ans)