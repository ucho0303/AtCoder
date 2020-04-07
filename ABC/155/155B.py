n = int(input())
x = list(map(int,input().split()))
x = [i for i in x if i%2 == 0]
ans = 'APPROVED'
for i in x:
    if i%3 != 0 and i%5 != 0:
        ans = 'DENIED'
print(ans)