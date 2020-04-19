n = int(input())
x = list(map(int,input().split()))
x.sort()
print(x[int(n/2)]-x[int(n/2-1)])