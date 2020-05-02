n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)
ans = n
l.sort()
for i in range(1,n):
    if l[i] == l[i-1]:
        ans -= 1
print(ans)
