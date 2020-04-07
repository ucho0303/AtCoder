n = int(input())
h = list(map(int,input().split()))
x = 0
for i in range(1,n) :
    a = h[-i]
    b = h[-i-1]
    if a >= b :
        pass
    elif b-a == 1 :
        h[-i-1] -= 1
    else :
        print('No')
        x += 1
        break
if x == 0 :
    print('Yes')