a,b = map(int,input().split())
k = int((a+b)/2)
if (a+b)%2 == 0 :
    print(k)
else :
    print('IMPOSSIBLE')