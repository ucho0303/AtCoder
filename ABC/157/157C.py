n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(list(map(int,input().split())))
ans = -1
if n == 1:
    for i in range(10):
        i = str(i)
        flag = True
        for j in range(m):
            if i[l[j][0]-1] != str(l[j][1]) :
                flag = False
        if flag:
            ans = int(i)
            break
else:
    for i in range(10**(n-1),10**n):
        i = str(i)
        flag = True
        for j in range(m):
            if i[l[j][0]-1] != str(l[j][1]) :
                flag = False
        if flag:
            ans = int(i)
            break
print(ans)
