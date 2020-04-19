n = int(input())
a = list(map(int,input().split()))
b = [i for i in range(1,n+1)]
x = 0
for i in range(n) :
    if a[i] != b[i] :
        x += 1
if x == 2 or x == 0:
    print('YES')
else :
    print('NO')
