n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a = sorted(a, key=lambda x: x[1])
ans = 'Yes'
x = 0
for s in a:
    x += s[0]
    if x > s[1] :
        ans = 'No'
        break
print(ans)