l,r = map(int,input().split())
a = 2019
for i in range(l,r+1) :
    if a == 0:
        break
    else :
        for j in range(i+1,r+1) :
            x = (i*j)%2019
            if x == 0 :
                a = x
                break
            else :
                if x<=a:
                    a = x
print(a)