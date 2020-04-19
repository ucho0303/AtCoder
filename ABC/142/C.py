n = int(input())
a = list(map(int,input().split()))
b = {}
for i in range(n):
    b[a[i]] = i+1
for i in range(1,n+1):
    print(b[i] , end =' ')
print('')
