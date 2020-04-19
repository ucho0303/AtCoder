n = int(input())
a = []
for i in range(n):
    a.append(list(input().split())+[i+1])
    a[i][1] = int(a[i][1])*(-1)
a = sorted(a)
for i in range(n):
    print(a[i][2])