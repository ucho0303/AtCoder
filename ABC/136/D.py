s = input()
s += 'R'
n = len(s)
ans = []
now = 'R'
r = 1
l = 0
for i in range(1,n):
    if s[i] == now :
        if now == 'R':
            r += 1
        else :
            l += 1
    else :
        if now == 'R' :
            now = 'L'
            l += 1
        else :
            x = (r+l)//2
            if r%2 == 0:
                ans += [0]*(r-1) + [x] + [r+l-x] + [0]*(l-1)
            else :
                ans += [0]*(r-1) + [r+l-x] + [x] + [0]*(l-1)
            r = 1
            l = 0
            now = 'R'
print(*ans)