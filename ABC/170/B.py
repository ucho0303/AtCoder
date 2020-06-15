x,y = map(int,input().split())
ans = 'No'
y -= x*2
for i in range(x+1):
    if y == 2*i:
        ans = 'Yes'
print(ans)