x,n = map(int,input().split())
if n == 0:
    print(x)
else:
    p = list(map(int,input().split()))
    p.sort()
    for i in range(100):
        if x-i not in p:
            print(x-i)
            break
        elif x+i not in p:
            print(x+i)
            break

        


