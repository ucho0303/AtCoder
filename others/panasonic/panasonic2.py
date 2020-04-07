h,w = map(int,input().split())
x = h*w
if h == 1 or w == 1 :
    print(1)
elif x % 2 == 0:
    print(x//2)
else :
    print(x//2+1)