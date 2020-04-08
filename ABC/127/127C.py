n,m = map(int,input().split())
a = []
lmax = 0
rmin = 10**6
for i in range(m):
    a.append(list(map(int,input().split())))
    if a[i][0] > lmax:
        lmax = a[i][0]
    if a[i][1] < rmin:
        rmin = a[i][1]
if rmin-lmax < 0 :
    print(0)
else :   
    print(1+rmin-lmax)
