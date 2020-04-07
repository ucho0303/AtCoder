n = int(input())
a = list(map(int, input().split()))
for i in range(n) :
    a[i] = 1/a[i]
b = sum(a)
print(1/b)